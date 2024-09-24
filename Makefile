
VENV_PATH ?= .venv
VENV_REQUIREMENTS = $(VENV_PATH)/.timestamp
PIP_REQUIREMENTS = $(VENV_PATH)/.requirements-timestamp
DOC_REQUIREMENTS = $(VENV_PATH)/.doc-requirements-timestamp
VENV_BIN = $(VENV_PATH)/bin
PIP_COMMAND = pip3
PYTHON_PATH = $(shell which python3)
PYTHON_VERSION = $(shell printf '%b' "import sys\nprint(f'{sys.version_info.major}.{sys.version_info.minor}')" | $$(which python3))
QGIS_VENV_PATH = $(VENV_PATH)/lib/python$(PYTHON_VERSION)/site-packages/qgis_paths.pth


QGIS_PY_PATH ?= /usr/share/qgis/python

# ********************
# Variable definitions
# ********************

# Package name
PACKAGE = qgis_server_light
LOCATION ?= ./src

# Python source files
SRC_PY = $(shell find $(LOCATION)/$(PACKAGE) -name '*.py')

# Environment variables used for build
BUILD_ENV += \
	DEVELOPMENT=${DEVELOPMENT}

# *******************
# Set up environments
# *******************

$(VENV_REQUIREMENTS):
	$(PYTHON_PATH) -m venv $(VENV_PATH)
	touch $@

$(QGIS_VENV_PATH):
	echo "/usr/share/qgis/python" > $@

$(PIP_REQUIREMENTS): $(VENV_REQUIREMENTS) pyproject.toml $(QGIS_VENV_PATH)
	$(VENV_BIN)/$(PIP_COMMAND) install --upgrade pip wheel setuptools
	$(VENV_BIN)/$(PIP_COMMAND) install .
	touch $@

$(DOC_REQUIREMENTS): $(PIP_REQUIREMENTS)
	$(VENV_BIN)/$(PIP_COMMAND) install .[docs]
	touch $@

# **************
# Common targets
# **************

# Build dependencies
BUILD_DEPS += $(PIP_REQUIREMENTS)


.PHONY: install
install: $(PIP_REQUIREMENTS)

.PHONY: install-docs
install-docs: $(PIP_REQUIREMENTS) $(DOC_REQUIREMENTS)


.PHONY: build
build: $(BUILD_DEPS)
	$(VENV_BIN)/python setup.py bdist_wheel

.PHONY: clean
clean:

.PHONY: clean-all
clean-all: clean
	rm -rf $(VENV_PATH)
	rm -rf src/$(PACKAGE).egg-info

.PHONY: git-attributes
git-attributes:
	git --no-pager diff --check `git log --oneline | tail -1 | cut --fields=1 --delimiter=' '`

.PHONY: test
test: $(PIP_REQUIREMENTS) $(VARS_FILES)
	$(VENV_BIN)/py.test -vv --cov-config .coveragerc --cov $(PACKAGE) --cov-report term-missing:skip-covered tests

.PHONY: doc-html
doc-html: $(DOC_REQUIREMENTS) docs/mkdocs.yml
	rm -rf doc/site
	$(VENV_BIN)/mkdocs build -f docs/mkdocs.yml -d site

.PHONY: doc-serve
doc-serve: $(DOC_REQUIREMENTS) docs/mkdocs.yml
	$(VENV_BIN)/mkdocs serve -f docs/mkdocs.yml

.PHONY: doc-gh-deploy
doc-gh-deploy: $(DOC_REQUIREMENTS) docs/mkdocs.yml
	$(VENV_BIN)/mkdocs gh-deploy -f docs/mkdocs.yml -d site --force

.PHONY: updates
updates: $(PIP_REQUIREMENTS)
	$(VENV_BIN)/pip list --outdated

.PHONY: dev
dev: setup.py build
	$(VENV_BIN)/python $< develop

.PHONY: serve
serve: $(PIP_REQUIREMENTS)
	$(VENV_BIN)/python src/georama/manage.py runserver 0.0.0.0:8000
