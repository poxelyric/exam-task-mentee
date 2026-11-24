FROM python:3.12-slim

ARG APP_VERSION=0.0.1

ENV APP_VERSION=${APP_VERSION}

COPY requirements.txt ./

RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

COPY app/ ./app/

WORKDIR /app

ENV PORT=8080

ENTRYPOINT ["python3", "app.py"]