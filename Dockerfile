FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

COPY pyproject.toml ./
COPY app/ ./app/

RUN addgroup --system --gid 10001 app \
    && adduser --system --uid 10001 --ingroup app app

USER 10001:10001

ENV PORT=8080

CMD gunicorn --workers 2 --bind 0.0.0.0:${PORT} --access-logfile - --error-logfile - app.app:application
