SHELL := /bin/bash

# Variables definitions
# -----------------------------------------------------------------------------

ifeq ($(TIMEOUT),)
TIMEOUT := 60
endif

ifeq ($(MODEL_PATH),)
MODEL_PATH := ./ml/model/
endif

ifeq ($(MODEL_NAME),)
MODEL_NAME := model.pkl
endif

# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: all clean test install run deploy down

all: clean test install run deploy down

test:
	poetry run pytest tests -vv --show-capture=all --cov=app --cov-report=term-missing -p no:warnings

install: generate_dot_env
	pip install --upgrade pip
	pip install poetry
	poetry install --with dev

run:
	PYTHONPATH=app/ poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8080

run-celery:
	PYTHONPATH=app/ poetry run celery \
  --app=celery_app.celery worker --pool=prefork --loglevel=INFO --beat -E \
  --concurrency=1 --autoscale=1


deploy: generate_dot_env
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

generate_dot_env:
	@if [[ ! -e .env ]]; then \
		cp .env.example .env; \
	fi

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build