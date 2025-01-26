.DEFAULT_GOAL := help

## —— 📦 Makefile 📦 —————————————————————————————————————————

help: ## Outputs this help screen
	@grep -E '(^[a-zA-Z0-9_-]+:.*?##.*$$)|(^##)' Makefile | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

## —— 🐋 Docker 🐋 —————————————————————————————————————————

up: ## up
	docker-compose -f docker-compose.yml up -d
down: ## down
	docker-compose -f docker-compose.yml down
run: ## run the app
	docker-compose run --rm python-app
build:
	docker-compose build
@:
	help