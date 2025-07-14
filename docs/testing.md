# Тестирование

## Подход

- TDD/BDD: сначала тесты, потом код
- Покрытие: unit, integration, e2e
- Использование pytest, coverage, mock

## Структура тестов

- tests/unit/ — модульные тесты (отдельные функции, классы)
- tests/integration/ — интеграционные тесты (работа с БД, Redis, RabbitMQ)
- tests/e2e/ — сквозные тесты (API, воркеры, очереди)

## Пример unit-теста (pytest)

```python
import pytest
from core.services import parse_resume

def test_parse_resume_valid():
    data = {"name": "Иван", "experience": "3 года"}
    result = parse_resume(data)
    assert result["name"] == "Иван"
```

## Пример интеграционного теста (pytest + testcontainers)

```python
import pytest
from testcontainers.postgres import PostgresContainer
from sqlalchemy import create_engine

def test_db_connection():
    with PostgresContainer("postgres:15") as pg:
        engine = create_engine(pg.get_connection_url())
        conn = engine.connect()
        assert conn.closed is False
        conn.close()
```

## Тестирование Redis и RabbitMQ

- Использовать testcontainers (testcontainers.redis, testcontainers.rabbitmq)
- Мокировать соединения при необходимости
- Для e2e — запускать через docker-compose тестовые сервисы

## Покрытие кода

- coverage run -m pytest
- coverage report -m

## Рекомендации

- Изолировать тестовые данные
- Использовать фикстуры pytest
- Для асинхронных задач — pytest-asyncio 