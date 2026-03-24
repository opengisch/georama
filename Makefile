
VENV_PATH ?= .venv
VENV_REQUIREMENTS = $(VENV_PATH)/.timestamp
PIP_REQUIREMENTS = $(VENV_PATH)/.requirements-timestamp
DEV_REQUIREMENTS = $(VENV_PATH)/.dev-requirements-timestamp
DEV_XSD_REQUIREMENTS = $(VENV_PATH)/.dev-xsd-requirements-timestamp
DOC_REQUIREMENTS = $(VENV_PATH)/.doc-requirements-timestamp
TEST_REQUIREMENTS = $(VENV_PATH)/.test-requirements-timestamp
CHECK_REQUIREMENTS = $(VENV_PATH)/.check-requirements-timestamp
LOCAL_QGIS_SERVER_LIGHT_REQUIREMENTS = $(VENV_PATH)/.local-qsl-requirements-timestamp
VENV_BIN = $(VENV_PATH)/bin
PIP_COMMAND = pip3
PYTHON_PATH = $(shell which python3)
PYTHON_VERSION = $(shell printf '%b' "import sys\nprint(f'{sys.version_info.major}.{sys.version_info.minor}')" | $$(which python3))
EDITABLE_GEORAMA_PATH = $(VENV_PATH)/lib/python$(PYTHON_VERSION)/site-packages/editable_georama.pth
PINNED_DEPS ?= reqs.txt
PINNED_DEPS_FOR_CI ?= reqs-test.txt # CI-specific requirements file
# you can overwrite this by passing env variable in front of the make call e.g.:
# GDAL_VERSION=4.9.9 make install-dev
GDAL_VERSION ?= $(shell gdal-config --version)

# Define the exact pygeoapi line you want in the CI requirements (branch reference)
PYGEOAPI_BRANCH_SPEC = pygeoapi @ git+https://github.com/opengisch/pygeoapi.git@respect-property-setting-in-ogr-provider

# Define the exact qgis-server-light line you want in the CI requirements (branch reference)
QGIS_SERVER_LIGHT_BRANCH_SPEC = qgis-server-light @ git+https://github.com/opengisch/qgis-server-light.git@master

QGIS_PY_PATH ?= /usr/share/qgis/python

# ********************
# Variable definitions
# ********************

# Package name
PACKAGE = georama
LOCATION ?= ./src

# **************************
# Load .env file if existing
# **************************

ifneq (,$(wildcard .env))
  include .env
  export
endif

# Environment variables used for build
BUILD_ENV += \
    DEVELOPMENT=${DEVELOPMENT}

# *******************
# Set up environments
# *******************

$(VENV_REQUIREMENTS):
	$(PYTHON_PATH) -m venv $(VENV_PATH)
	# we directly install gdal here into the venv since it is relying on the system gdal version
	# and this information we can only fetch in a simple way in a shell like context
	$(VENV_BIN)/$(PIP_COMMAND) install --upgrade pip wheel setuptools gdal==$(GDAL_VERSION)
	touch $@

$(EDITABLE_GEORAMA_PATH):
	echo $(shell pwd)/src > $@

$(PIP_REQUIREMENTS): $(VENV_REQUIREMENTS) pyproject.toml setup.py
	$(VENV_BIN)/$(PIP_COMMAND) install .
	touch $@

$(DEV_REQUIREMENTS): $(PIP_REQUIREMENTS)
	$(VENV_BIN)/pip install -e .[dev]
	touch $@

$(DEV_XSD_REQUIREMENTS): $(PIP_REQUIREMENTS)
	$(VENV_BIN)/pip install -e .[dev_xsd]
	touch $@

$(DOC_REQUIREMENTS): $(PIP_REQUIREMENTS)
	$(VENV_BIN)/$(PIP_COMMAND) install .[docs]
	touch $@

$(TEST_REQUIREMENTS): $(PIP_REQUIREMENTS)
	$(VENV_BIN)/$(PIP_COMMAND) install -e .[test]
	touch $@

$(CHECK_REQUIREMENTS): $(PIP_REQUIREMENTS)
	$(VENV_BIN)/$(PIP_COMMAND) install .[check]
	touch $@

$(LOCAL_QGIS_SERVER_LIGHT_REQUIREMENTS): $(DEV_REQUIREMENTS)
	$(if $(LOCAL_QGIS_SERVER_LIGHT_PATH),,$(error LOCAL_QGIS_SERVER_LIGHT_PATH has to be defined))
	$(VENV_BIN)/$(PIP_COMMAND) install -e file://$(LOCAL_QGIS_SERVER_LIGHT_PATH)\#qgis_server_light --config-settings editable_mode=compat


# **************
# Common targets
# **************

# Build dependencies
BUILD_DEPS += $(PIP_REQUIREMENTS)


.PHONY: install
install: $(PIP_REQUIREMENTS)

.PHONY: install-docs
install-docs: $(DOC_REQUIREMENTS)

.PHONY: install-test
install-test: $(TEST_REQUIREMENTS)

.PHONY: install-dev
install-dev: $(DEV_REQUIREMENTS)

.PHONY: install-dev-xsd
install-dev-xsd: $(DEV_XSD_REQUIREMENTS)

.PHONY: install-dev-local-qsl
install-dev-local-qsl: $(LOCAL_QGIS_SERVER_LIGHT_REQUIREMENTS)

.PHONY: build
build: $(BUILD_DEPS)
	$(VENV_BIN)/python setup.py bdist_wheel

.PHONY: clean
clean:
	find ./src -name "*.pyc" -delete

.PHONY: clean-all
clean-all: clean
	rm -rf .tox
	rm -rf dist
	rm -rf $(VENV_PATH)
	rm -rf build
	rm -rf src/$(PACKAGE).egg-info
	rm -f .coverage
	rm -f .coverage.xml

.PHONY: git-attributes
git-attributes:
	git --no-pager diff --check `git log --oneline | tail -1 | cut --fields=1 --delimiter=' '`

.PHONY: test-core
test-core: $(TEST_REQUIREMENTS) $(VARS_FILES)
	$(VENV_BIN)/pytest -vv tests/unit/core

.PHONY: test-data_integration
test-data_integration: $(TEST_REQUIREMENTS) $(VARS_FILES)
	$(VENV_BIN)/pytest --nomigrations -vv tests/unit/data_integration

.PHONY: test-features
test-features: $(TEST_REQUIREMENTS) $(VARS_FILES)
	$(VENV_BIN)/pytest --nomigrations -vv tests/unit/features

.PHONY: test-maps
test-maps: $(TEST_REQUIREMENTS) $(VARS_FILES)
	$(VENV_BIN)/pytest --nomigrations -vv tests/unit/maps

.PHONY: test-webgis
test-webgis: $(TEST_REQUIREMENTS) $(VARS_FILES)
	$(VENV_BIN)/pytest --nomigrations -vv tests/unit/webgis

.PHONY: tests
tests: test-core test-data_integration test-features test-maps test-webgis

.PHONY: coverage
coverage: $(TEST_REQUIREMENTS)
	$(VENV_BIN)/pytest --nomigrations -vv --cov $(PACKAGE) --cov-report term-missing:skip-covered --cov-report=xml:.coverage.xml tests

.PHONY: check-types
check-types: $(CHECK_REQUIREMENTS)
	$(VENV_BIN)/mypy --explicit-package-bases --show-error-codes src/$(PACKAGE) tests

.PHONY: check-package-metadata
check-package-metadata: $(CHECK_REQUIREMENTS)
	$(VENV_BIN)/pyroma --directory ./

.PHONY: checks
checks: check-types check-package-metadata

.PHONY: doc-html
doc-html: $(DOC_REQUIREMENTS) docs/mkdocs.yml
	rm -rf doc/site
	$(VENV_BIN)/mkdocs build -f docs/mkdocs.yml -d site

.PHONY: doc-live-prereqs
doc-live-prereqs:
	@echo "Running documentation pre-generation scripts..."
	python ./docs/scripts/visualize-dockerfile.py -o docs/src/dockerfile_mermaid.md
	python ./docs/scripts/visualize-ga-workflow.py .github/workflows/test.yaml -o docs/src/cicd_mermaid.md

.PHONY: doc-serve
doc-serve: $(DOC_REQUIREMENTS) doc-live-prereqs docs/mkdocs.yml
	$(VENV_BIN)/mkdocs serve -f docs/mkdocs.yml

.PHONY: doc-gh-deploy
doc-gh-deploy: $(DOC_REQUIREMENTS) docs/mkdocs.yml
	$(VENV_BIN)/mkdocs gh-deploy -f docs/mkdocs.yml -d site --force

.PHONY: updates
updates: $(PIP_REQUIREMENTS)
	$(VENV_BIN)/pip list --outdated

.PHONY: serve-dev
serve-dev: $(DEV_REQUIREMENTS)
	$(VENV_BIN)/python src/georama/manage.py runserver localhost:4242

# This target is for serving DEV georama so that it can  be reached within its network, you never want to do
# that locally on your host machine unless in docker containers or you have a good reason.
.PHONY: serve-dev-outbound
serve-dev-outbound: $(DEV_REQUIREMENTS)
	$(VENV_BIN)/python src/georama/manage.py runserver 0.0.0.0:4242

MANAGE_ACTION="shell_plus"
.PHONY: manage
manage: $(PIP_REQUIREMENTS)
	$(VENV_BIN)/python src/georama/manage.py $(MANAGE_ACTION)

.PHONY: migrate
collectstatic: $(PIP_REQUIREMENTS)
	$(VENV_BIN)/python src/georama/manage.py collectstatic

.PHONY: migrate
migrate: $(PIP_REQUIREMENTS)
	$(VENV_BIN)/python src/georama/manage.py migrate

.PHONY: make-migrations
make-migrations: $(PIP_REQUIREMENTS)
	$(VENV_BIN)/python src/georama/manage.py makemigrations

.PHONY: check-migrations
check-migrations: $(PIP_REQUIREMENTS)
	$(VENV_BIN)/python src/georama/manage.py makemigrations --check --dry-run

.PHONY: create-superuser
create-superuser: $(PIP_REQUIREMENTS) migrate
	$(VENV_BIN)/python src/georama/manage.py createsuperuser --username admin --email admin@xy.ch

.PHONY: create-example-content
create-example-content: $(PIP_REQUIREMENTS) migrate
	$(VENV_BIN)/python src/georama/manage.py loaddata tests/resources/users.json

.PHONY: pin-deps
pin-deps: $(CHECK_REQUIREMENTS) $(TEST_REQUIREMENTS)
	$(VENV_BIN)/$(PIP_COMMAND) freeze --all > $(PINNED_DEPS)

# This target depends on the original $(PINNED_DEPS) being created first.
$(PINNED_DEPS_FOR_CI): $(PINNED_DEPS)
	@echo "Creating CI-specific requirements file: $(PINNED_DEPS_FOR_CI) from $(PINNED_DEPS)"
	@# Step 1: Read $(PINNED_DEPS), filter out any existing pygeoapi AND qgis-server-light git+ lines,
	@# and write the result to $(PINNED_DEPS_FOR_CI).
	sed -e '/^pygeoapi @ git+/d' -e '/^qgis-server-light @ git+/d' $(PINNED_DEPS) > $(PINNED_DEPS_FOR_CI)
	@# Step 2: Append the desired branch reference lines for both packages
	@echo "$(PYGEOAPI_BRANCH_SPEC)" >> $(PINNED_DEPS_FOR_CI)
	@echo "$(QGIS_SERVER_LIGHT_BRANCH_SPEC)" >> $(PINNED_DEPS_FOR_CI)
	@echo "$(PINNED_DEPS_FOR_CI) created successfully."

# Phony target to easily create the CI requirements file
.PHONY: prepare-ci-reqs
prepare-ci-reqs: $(PINNED_DEPS_FOR_CI)
	@echo "CI requirements file is ready at $(PINNED_DEPS_FOR_CI)."
