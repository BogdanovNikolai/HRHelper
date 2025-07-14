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

## Тесты
- pytest, testcontainers, coverage
- Запуск: `pytest tests/`

## CI/CD и автоматизация
- Jenkins запускается в Docker с пробросом docker.sock:
  ```bash
  docker run --name jenkins -p 8080:8080 -p 50000:50000 \
    -v jenkins_home:/var/jenkins_home \
    -v /var/run/docker.sock:/var/run/docker.sock \
    myjenkins:latest
  ```
- Jenkinsfile лежит в `ci/Jenkinsfile` (тесты и линтеры внутри Docker)
- Для работы docker-команд Jenkins-пользователь должен быть в группе docker (см. Dockerfile ниже)
- Все тесты и линтеры запускаются автоматически при каждом коммите

## Makefile (локальная автоматизация)
- `make test` — запустить тесты
- `make lint` — запустить flake8
- `make build` — собрать Docker-образ
- `make up` — поднять сервисы через docker-compose
- `make down` — остановить сервисы

## Pre-commit hooks
- Установите pre-commit: `pip install pre-commit`
- Активируйте: `pre-commit install`
- Линтеры и форматтеры будут запускаться автоматически при коммите

## Alembic
- Alembic должен быть в requirements.txt
- Миграции: `alembic upgrade head`

## Документация по Jenkins
- Jenkinsfile: `ci/Jenkinsfile`
- Для production рекомендуется использовать свой Dockerfile для Jenkins (см. ниже)

---

## Jenkins Dockerfile (для production)

Создайте файл `jenkins.Dockerfile`:
```dockerfile
FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y docker.io
RUN usermod -aG docker jenkins
USER jenkins
```

Запуск:
```bash
docker build -t myjenkins:latest -f jenkins.Dockerfile .
docker run --name jenkins -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  myjenkins:latest
```

---

## Лицензия
MIT 