# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:0.7.4-alpine

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates \
    gcc \
    postgresql-dev \
    linux-headers \
    musl-dev \
    libffi-dev \
    jpeg-dev \
    zlib-dev \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

# Install the project into `/app`
WORKDIR /app

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

COPY build/docker/docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching

COPY pyproject.toml /app/pyproject.toml
COPY uv.lock /app/uv.lock
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

WORKDIR /app/src
COPY src .

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
# ENTRYPOINT []

# Set the default command to run when the container starts
CMD ["../docker-entrypoint.sh"]
