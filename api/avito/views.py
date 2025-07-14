"""
API-эндпоинты для работы с avito.ru (FastAPI)
"""
from fastapi import APIRouter
from .schemas import Vacancy
from typing import List

router = APIRouter(prefix="/avito", tags=["avito"])

@router.get("/vacancies", response_model=List[Vacancy])
def get_vacancies():
    """
    Получить список вакансий с avito.ru (пример)
    """
    return [Vacancy(id="1", title="Python Developer", company="Avito")] 