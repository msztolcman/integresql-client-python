.PHONY: distro distro-test clean build upload upload-test test lint help

## building
distro: clean build upload ## build and upload distro to prod pypi

distro-test: clean build upload-test ## build and upload distro to test pypi

clean: ## cleanup all distro
	-rm -fr dist
	-rm -fr __pycache__
	-rm -fr integresql_client_python/__pycache__
	-rm -fr build

build: ## build distro
	python3 setup.py sdist bdist_wheel

upload: ## upload distro
	twine upload dist/integresql_client_python*

upload-test: ## upload distro to test Pypi
	twine upload --repository testpypi dist/integresql_client_python*

test: ## run test suite
	pytest --nf --ff -q

lint: ## run external tools like flake8, bandit, safety
	flake8 integresql_client_python
	bandit -rq integresql_client_python
	safety check --bare

.DEFAULT_GOAL := help
help:
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'
