from pydantic import BaseModel

class Book(BaseModel):
    id: str
    name: str
    author: str
    publication_year: int
    genre: str
