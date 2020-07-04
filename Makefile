.PHONY: build

SHELL := /bin/bash

build: ## Build the backend Docker image
	docker build -t portfolio_backend_image .

up: build ## Bring the backend Docker container up
	docker-compose -p portfolio up -d backend || echo 'Already up!'

down: ## Stop the backend Docker container
	docker-compose stop

enter: ## Enter the running backend Docker container
	docker exec -it portfolio_backend /bin/bash

clean: ## Stop and remove all Docker containers
	docker-compose down

up_db: up
	docker-compose -p portfolio up -d db || echo 'DB Up'

down_db: ## Stop the backend Docker container
	docker-compose -p portfolio stop db

enter_db: ## Enter the running backend Docker container
	docker exec -it portfolio_db /bin/bash
