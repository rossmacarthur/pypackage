.PHONY: help clean venv build build-all lint sort-imports test

PYTHON := python3
VIRTUAL_ENV := $(or $(VIRTUAL_ENV), $(VIRTUAL_ENV), "venv")

help: ## Show this message and exit.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-13s\033[0m %s\n", $$1, $$2}'

clean: ## Remove all build artifacts.
	rm -rf build dist wheels venv *.egg-info
	find . \( -name *.pyc -o -name *.pyo -o -name __pycache__ \) -exec rm -rf {} +

venv: ## Create virtualenv
	virtualenv --python=$(PYTHON) venv

build: ## Install package.
	$(VIRTUAL_ENV)/bin/pip install -e .

build-all: ## Install package and development dependencies.
	$(VIRTUAL_ENV)/bin/pip install -e ".[linting,testing]"

lint: ## Run all lints.
	$(VIRTUAL_ENV)/bin/flake8 --max-complexity 10 .

sort-imports: ## Sort import statements according to isort configuration.
	$(VIRTUAL_ENV)/bin/isort --recursive .

test: ## Run all tests.
	$(VIRTUAL_ENV)/bin/pytest -vv --cov={{ cookiecutter.slug }} --cov-report term-missing tests
