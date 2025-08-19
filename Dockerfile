FROM python:3.11

WORKDIR /test
COPY pyproject.toml uv.lock /test

COPY --link --from=ghcr.io/astral-sh/uv:0.4 /uv /usr/local/bin/uv
RUN uv pip install --system .

COPY . /test