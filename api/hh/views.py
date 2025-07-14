"""
API-эндпоинты для работы с hh.ru (FastAPI)
"""
from fastapi import APIRouter
from .schemas import Resume
from typing import List

router = APIRouter(prefix="/hh", tags=["hh"])

@router.get("/resumes", response_model=List[Resume])
def get_resumes():
    """Получить список резюме с hh.ru (пример)"""
    return [Resume(id="1", name="Иван Иванов", experience="3 года")] 