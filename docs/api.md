# API HR-платформы

## Описание

REST API для интеграций с внешними сервисами (hh, avito), работы с резюме, вакансиями, очередями задач.

## OpenAPI (пример)

```yaml
openapi: 3.0.0
info:
  title: HR Platform API
  version: 1.0.0
paths:
  /api/hh/resumes:
    get:
      summary: Получить список резюме с hh.ru
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Resume'
  /api/avito/vacancies:
    get:
      summary: Получить список вакансий с avito.ru
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Vacancy'
  /api/task:
    post:
      summary: Поставить задачу в очередь (RabbitMQ)
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                type:
                  type: string
                payload:
                  type: object
      responses:
        '202':
          description: Задача принята
components:
  schemas:
    Resume:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
        experience:
          type: string
    Vacancy:
      type: object
      properties:
        id:
          type: string
        title:
          type: string
        company:
          type: string
```

## Примеры запросов/ответов

- **GET /api/hh/resumes** — список резюме
- **GET /api/avito/vacancies** — список вакансий
- **POST /api/task** — постановка задачи в очередь (RabbitMQ)

## Аутентификация

- JWT, OAuth2 (пример — TODO)

## Документация генерируется через OpenAPI/Swagger (FastAPI, drf-yasg и др.) 