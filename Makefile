install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=term-missing --cov-fail-under=90

lint:
	uv run ruff check gendiff tests

build:
	uv build

.PHONY: install update run test test-coverage lint lint-fix check build