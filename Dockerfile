FROM python:3.10.20-slim-trixie

RUN apt-get update && apt-get upgrade
RUN apt-get install curl -y

ENV PATH="/root/.local/bin:$PATH"
RUN curl -LsSf https://astral.sh/uv/install.sh | sh 

RUN uv --version && \
    which uv && \
    uv init /app &&\
    uv venv /app/.venv

WORKDIR /app
COPY . .

RUN uv sync 
ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "main.py"]