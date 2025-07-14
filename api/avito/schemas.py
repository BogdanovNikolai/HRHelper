from pydantic import BaseModel
from typing import Optional


class Vacancy(BaseModel):
    id: str
    title: str
    company: Optional[str] = None 