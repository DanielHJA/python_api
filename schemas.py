from typing import Sequence

from pydantic import BaseModel


class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: str

    class Config:
        orm_mode = True


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]