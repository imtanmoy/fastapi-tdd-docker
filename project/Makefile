.PHONY:help

DOCKER_COMMAND = docker-compose exec web
PIPENV_COMMAND = docker-compose exec web

help: ## Help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


test: ## all test commands
	@echo "Running pytest"
	@$(DOCKER_COMMAND) python -m pytest
	@echo "Running flake8"
	@$(PIPENV_COMMAND) python -m flake8 .
	@echo "Running black"
	@$(PIPENV_COMMAND) python -m black . --check
	@echo "Running isort"
	@$(PIPENV_COMMAND) python -m isort ./*/*.py --check-only


fix: ## fixing all black and isort error
	@echo "Running pytest"
	@$(DOCKER_COMMAND) python -m pytest
	@echo "Running flake8"
	@$(PIPENV_COMMAND) python -m flake8 .
	@echo "Running black"
	@$(PIPENV_COMMAND) python -m black .
	@echo "Running isort"
	@$(PIPENV_COMMAND) python -m isort ./*/*.py