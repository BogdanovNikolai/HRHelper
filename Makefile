# Makefile для HR Helper

.PHONY: test lint build up down

test:
	pytest tests/

lint:
	flake8 .

build:
	docker build -t hr-helper -f docker/Dockerfile .

up:
	docker-compose -f docker/docker-compose.yml up -d

down:
	docker-compose -f docker/docker-compose.yml down 