# Changelog

## 0.0.1 (2024-05-23)

This is the first ever release of the **georama** Python Package.
The package is open source and is part of the **GeoRama** Project.
The project is hosted in a public repository on [GitHub](https://github.com/opengisch/georama) at 
The project was scaffolded using the 
[Cookiecutter Python Package](https://python-package-generator.readthedocs.io/en/master/) with a
[Template](https://github.com/boromir674/cookiecutter-python-package/tree/master/src/cookiecutter_python)

Scaffolding included:

- **CI Pipeline** running on [Github Actions](https://github.com/opengisch/georama/actions) 
  - `Test Workflow` running a multi-factor **Build Matrix** spanning different `platform`'s and `python version`'s
    1. Platforms: `ubuntu-latest`, `macos-latest`
    1. Python Interpreters: `3.10`

- Automated **Test Suite** with parallel Test execution across multiple cpus.
  - Code Coverage
- **Automation** in a 'make' like fashion, using **tox**
  - Seamless `Lint`, `Type Check`, `Build` and `Deploy` *operations*
