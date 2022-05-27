from sqlalchemy import Column, Integer, String
from database import Base


class Recipe(Base):
    __tablename__ = "Recipe"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(100))
    source = Column(String(100))
    url = Column(String(100))
