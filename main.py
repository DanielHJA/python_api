import logging
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
import models
import schemas
from database import SessionLocal, engine

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")
api_router = APIRouter()
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return "root"


@app.get("/recipe/{recipe_id}", status_code=200, response_model=schemas.Recipe)
def fetch_recipe(*, keyword: str = Query(None, min_length=1, example=1),
                 recipe_id: int, db: Session = Depends(get_db)) -> dict:
    """
    Fetch a single recipe by ID
    """
    result = db.query(models.Recipe).get(recipe_id)

    if not result:
        if not result:
            raise HTTPException(
                status_code=404, detail=f"Recipe with ID {recipe_id} not found"
            )

    return result


@app.get("/search/", status_code=200, response_model=schemas.RecipeSearchResults)  # 3
def search_recipes(
        keyword: Optional[str] = Query(None, min_length=3, example="chicken"),
        max_results: Optional[int] = 10, db: Session = Depends(get_db)
) -> dict:

    result = db.query(models.Recipe).filter(models.Recipe.label.contains(keyword)).all()
    if not result:
        if not result:
            raise HTTPException(
                status_code=404, detail=f"No recipes found"
            )

    return {"results": result}  # 6


@app.get("/search/all", status_code=200, response_model=schemas.RecipeSearchResults)  # 3
def search_recipes(db: Session = Depends(get_db)) -> dict:

    result = db.query(models.Recipe).all()

    if not result:
        if not result:
            raise HTTPException(
                status_code=404, detail=f"No recipes found"
            )

    return {"results": result}  # 6


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")