FROM python:3.10.7

WORKDIR /usr/src/backend

ENV PIP_ROOT_USER_ACTION=ignore

COPY poetry.lock .
COPY pyproject.toml .
COPY entrypoint.sh .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN chmod +x entrypoint.sh

COPY . .
