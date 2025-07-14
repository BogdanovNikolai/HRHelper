# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Создание пользователя
RUN useradd -m appuser
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY . .

# Переменные окружения (пример)
ENV PYTHONUNBUFFERED=1
ENV ENV_FILE=.env

# Миграции Alembic (опционально)
# RUN alembic upgrade head

# HEALTHCHECK (пример)
# HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

# Запуск приложения (пример)
CMD ["python", "main.py"] 