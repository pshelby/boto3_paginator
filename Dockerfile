FROM python:3.11-alpine

ENV GROUP=appuser
ENV USER=appuser

RUN addgroup -S ${GROUP} && \
  adduser -S ${USER} -G ${GROUP}

RUN python3 -m pip install --no-cache-dir poetry==2.1.4

WORKDIR /app

COPY --chown=${USER}:${GROUP} pyproject.toml poetry.lock ./

RUN chown -R ${USER}:${GROUP} ./

USER ${USER}

RUN poetry config virtualenvs.create true && \
  poetry config virtualenvs.in-project true && \
  poetry install --no-interaction --no-ansi --no-root

COPY --chown=${USER}:${GROUP} . ./

RUN poetry install --no-interaction --no-ansi

ENTRYPOINT ["poetry", "run"]
