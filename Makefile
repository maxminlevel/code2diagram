PHONY: help

help: 		## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

docker-down: 	## docker-compose down
	@docker-compose -f docker/docker-compose.yml down

docker-up: 	## docker-compose up
	@docker-compose -f docker/docker-compose.yml up -d

docker-build:
	@sh scripts/docker-image.sh

build: 		## build anything
	@echo "To do"

setup: 		## setup project
	pip3 install -r requirements.txt

hide.env:
	@sh scripts/env-hide.sh

load.env:
	@echo "copy and pase command: source .env"

install: 	## install tool and list
	@echo "To do"

requirements:	## export requirements.txt
	@pip3 freeze > requirements.txt
