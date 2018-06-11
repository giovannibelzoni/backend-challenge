FROM python:alpine3.7

RUN apk add --no-cache  \
    build-base \
    linux-headers \
    libc6-compat \
    mariadb-dev \
    curl \
    git

RUN addgroup -S qubit && \
    adduser -S -G qubit -u 1000 -D -h /qubit qubit && \
    install -d -o qubit -g qubit -m 02775 /qubit/app

ENV VIRTUAL_ENV=/qubit/.venv \
    APP_DIR=/qubit/app

ENV PATH=${VIRTUAL_ENV}/bin:${PATH}

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python && \
    pip install --no-cache-dir virtualenv && \
    virtualenv ${VIRTUAL_ENV}

WORKDIR /qubit

COPY *pyproject.lock pyproject.toml /qubit/

RUN poetry install

COPY . ${APP_DIR}

WORKDIR ${APP_DIR}

USER qubit
EXPOSE 8000
ENTRYPOINT ["/qubit/app/entrypoint.sh"]