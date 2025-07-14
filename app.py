"""
Точка входа приложения (app.py)
FastAPI-приложение: инициализация, роуты, запуск сервера
"""
from fastapi import FastAPI
from api.hh.views import router as hh_router
from api.avito.views import router as avito_router

app = FastAPI(title="HR Helper Platform")

app.include_router(hh_router)
app.include_router(avito_router)

@app.get("/health")
def health_check():
    """
    Проверка работоспособности сервиса
    """
    return {"status": "ok"}

# TODO: Подключить другие роуты и middlewares 