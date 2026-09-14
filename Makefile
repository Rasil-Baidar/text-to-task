.PHONY: install dev run

install:
	uv sync

dev:
	uv run fastapi dev src/text_to_task/app.py

run:
	uv run fastapi run src/text_to_task/app.py