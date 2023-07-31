include .env

DCE = docker compose exec
DEI = docker exec -it

# *****************************
# *      For First Build      *
# *****************************

# .envがなければ生成する
.PHONY: env
env:
	@if [ -e .env ] ; then \
		echo ".env already exists"; \
	else \
		cp .env.example .env; \
	fi

.PHONY: init
init:
	@make build_c
	@make up

# *****************************
# *     Container Controll    *
# *****************************
.PHONY: build_c
build_c:
	docker compose build --no-cache --force-rm

.PHONY: build
build:
	docker compose build

.PHONY: up
up:
	docker compose up -d

.PHONY: stop
stop:
	docker compose stop

.PHONY: down
down:
	docker compose down --remove-orphans

.PHONY: restart
restart:
	@make down
	@make up


# *****************************
# *     Backend Controll    *
# *****************************
.PHONY: app
app:
	$(DCE) $(BACKEND_SERVICE_NAME) bash

.PHONY: log
log:
	docker compose logs -f $(BACKEND_SERVICE_NAME)

.PHONY: format
format:
	$(DCE) $(BACKEND_SERVICE_NAME) bash -c "yapf -i -r ."

.PHONY: run
run:
	$(DCE) $(BACKEND_SERVICE_NAME) bash -c "python main.py"