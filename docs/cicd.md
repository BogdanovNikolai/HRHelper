# CI/CD (Jenkins)

## Общий процесс

1. Проверка кода (линтеры, тесты)
2. Сборка Docker-образа
3. Прогон миграций Alembic
4. Публикация образа (DockerHub/Registry)
5. Деплой на тест/прод

## Пример пайплайна Jenkins

```groovy
pipeline {
  agent any
  environment {
    DOCKER_IMAGE = "myorg/hr-helper:${env.BUILD_NUMBER}"
    POSTGRES_USER = credentials('pg_user')
    POSTGRES_PASSWORD = credentials('pg_pass')
    REDIS_URL = 'redis://redis:6379/0'
    RABBITMQ_URL = 'amqp://guest:guest@rabbitmq:5672/'
  }
  stages {
    stage('Lint & Test') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pytest --maxfail=1 --disable-warnings'
        sh 'flake8 .'
      }
    }
    stage('Build Docker') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE .'
      }
    }
    stage('Migrate DB') {
      steps {
        sh 'docker-compose -f docker/docker-compose.yml run --rm app alembic upgrade head'
      }
    }
    stage('Push Image') {
      steps {
        sh 'docker push $DOCKER_IMAGE'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker-compose -f docker/docker-compose.yml up -d'
      }
    }
  }
}
```

## Работа с переменными окружения

- Все секреты — через Jenkins credentials или .env
- Не хранить пароли в репозитории

## Запуск сервисов для тестов

- docker-compose: поднимает PostgreSQL, Redis, RabbitMQ
- healthchecks для сервисов

## Линтеры и тесты

- flake8, black, isort
- pytest, coverage

## Миграции Alembic

- alembic upgrade head — после сборки 