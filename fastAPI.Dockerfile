FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /py-rest

COPY poetry.lock pyproject.toml /py-rest/
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

ARG DEV=false
RUN poetry install

# COPY ./app/ ./
# COPY ./alembic.ini alembic.ini
# COPY ./alembic alembic

COPY ./app/ ./app

ENV PYTHONPATH "${PYTHONPATH}:/py-rest:/py-rest/services"

EXPOSE 8080
CMD uvicorn app.main:app --host 0.0.0.0 --port 8080