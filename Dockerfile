FROM python:3.13-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

ENV MY_ENV_VAR=${MY_ENV_VAR}
ENV ANOTHER_VAR=${ANOTHER_VAR}

CMD ["poetry", "run", "python", "main.py"]
