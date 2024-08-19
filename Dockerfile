FROM jenkins/agent:alpine-jdk11

USER root

# Install Python 3 and virtualenv
RUN apk add --no-cache python3 py3-pip python3-dev \
    && python3 -m venv /venv \
    && . /venv/bin/activate \
    && pip install --upgrade pip \
    && pip install Flask

# Set environment variables to use the virtual environment
ENV PATH="/venv/bin:$PATH"

USER jenkins


