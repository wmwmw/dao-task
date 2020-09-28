FROM ubuntu:focal

RUN apt-get update && \
    apt-get install python3 wget python3-pip -y && \
    apt-get clean

RUN pip3 install poetry

WORKDIR /tmp 
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install && rm -rfd .cache

WORKDIR /app
COPY ./dao .


