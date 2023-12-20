.PHONY: help
.SILENT:

help:
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install:  # Install base requirements to run project
	pip install -r requirements/base.txt

dev-install: install  # Install developer requirements + base requirements
	pip install -r requirements/test.txt

test:  # Test
	python -m tests

build:  # Build package
	python -m build

publish: build  # Publish on Pypi (https://packaging.python.org/en/latest/tutorials/packaging-projects/)
	python -m twine upload --repository pypi dist/*
