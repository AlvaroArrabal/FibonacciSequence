EXEC = python3 -m app.main
EXEC_TEST = pytest -v -s

.DEFAULT_GOAL := help

## —— 📦 Makefile 📦 —————————————————————————————————————————

help: ## Outputs this help screen
	@grep -E '(^[a-zA-Z0-9_-]+:.*?##.*$$)|(^##)' Makefile | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

## —— 🐋 Docker 🐋 ———————————————————————————————————————————

build: ## builds the container
	docker-compose build
up: ## up
	docker-compose -f docker-compose.yml up -d
down: ## down
	docker-compose -f docker-compose.yml down
enter: ## enter to docker container with compiler
	docker exec -it my-python-app /bin/bash
run: ## run the app
	$(EXEC)
runTest: ## run the test
	$(EXEC_TEST)
@:
	help