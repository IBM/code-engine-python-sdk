# This makefile is used to make it easier to get the project set up
# to be ready for development work in the local sandbox.
# example: "make setup"

setup: deps dev_deps install_project

all: upgrade_pip setup test-unit lint

ci: setup test-unit lint

upgrade_pip:
	python3 -m pip install --upgrade pip

deps:
	python3 -m pip install -r requirements.txt

dev_deps:
	python3 -m pip install -r requirements-dev.txt

install_project:
	python3 -m pip install -e .

test: test-unit test-int

test-unit:
	python3 -m pytest --cov=ibm_code_engine_sdk test/unit

test-int:
	python3 -m pytest test/integration

test-examples:
	python3 -m pytest example

lint:
	./pylint.sh && black --check .

lint-fix:
	black .
