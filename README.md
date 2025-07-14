# HR Helper Platform

Модульная Python-платформа для работы с HR-данными, интеграциями (hh, avito), асинхронными задачами, PostgreSQL, Redis, RabbitMQ.

## Архитектура
- PostgreSQL (SQLAlchemy, Alembic)
- Redis (кэш, очереди)
- RabbitMQ (очереди задач)
- Docker, docker-compose
- Jenkins (CI/CD)

## Быстрый старт

```bash
# Клонируйте репозиторий
# cp .env.example .env
cd docker
# Соберите и запустите все сервисы
sudo docker-compose up --build
```

Приложение будет доступно на http://localhost:8000

## Документация
- docs/architecture.md — архитектура
- docs/api.md — OpenAPI спецификация
- docs/testing.md — тестирование
- docs/cicd.md — CI/CD

## Тесты
- pytest, testcontainers, coverage

## CI/CD
- Jenkins, Jenkinsfile (ci/)

## Переменные окружения
- .env.example — пример

## Лицензия
MIT 