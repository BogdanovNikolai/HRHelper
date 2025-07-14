from pydantic import BaseModel
from typing import Optional


class Resume(BaseModel):
    id: str
    name: str
    experience: Optional[str] = None 