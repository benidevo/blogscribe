build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up

up-d:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down
down-v:
	docker compose -f local.yml down -v

show-logs-db:
	docker compose -f local.yml logs postgres

show-logs-api:
	docker compose -f local.yml logs api

show-logs-flower:
	docker compose -f local.yml logs flower

makemigrations:
	docker compose -f local.yml run --rm api python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm api python manage.py migrate

collectstatic:
	docker compose -f local.yml run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm api python manage.py createsuperuser

volume:
	docker volume inspect src_local_postgres_data

blogscribe-db:
	docker compose -f local.yml exec postgres psql --username=benidevo --dbname=blogscribe

search-index:
	docker compose -f local.yml exec api python manage.py search_index --rebuild

flake8:
	docker compose -f local.yml exec api flake8 .

black-check:
	docker compose -f local.yml  exec api black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml  exec api black --diff --exclude=migrations .

black:
	docker compose -f local.yml  exec api black --exclude=migrations .

isort-check:
	docker compose -f local.yml  exec api isort . --chsck-only --skip migrations --skip venv

isort-diff:
	docker compose -f local.yml  exec api isort . --diff --skip migrations --skip venv

isort:
	docker compose -f local.yml  exec api isort . --skip migrations --skip venv
