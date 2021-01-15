FROM python:3.9-alpine

RUN apk add --update \
    bash \
    curl \
    git \
    && rm -rf /var/cache/apk/*

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
