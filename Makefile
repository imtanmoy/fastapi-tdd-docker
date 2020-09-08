.PHONY:help

DOCKER_COMMAND = docker-compose
DOCKER_COMMAND_EXEC = docker-compose exec web

help: ## Help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

db-init:
	@$(DOCKER_COMMAND_EXEC) python app/db.py

up: ## Start development containers
	@echo "Starting development containers"
	@$(DOCKER_COMMAND) up -d --build

down: ## Remove development containers
	@echo "Removing development containers"
	@$(DOCKER_COMMAND) down

clean: ## Remove development containers and volumes
	@echo "Removing development containers and volumes"
	@$(DOCKER_COMMAND) down -v