FROM python:3.11-slim

RUN pip install poetry --no-cache-dir

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Setting this so that import in the script are using DuckDB functions.
ENV USE_DUCKDB=TRUE
