from fastapi import APIRouter

# pydantic is a data validation library used by FastAPI, not part of FastAPI itself,
# which allows defining data models with type annotations.
# helps define, validate, and parse data easily
from pydantic import BaseModel

router = APIRouter()

class Book(BaseModel):
    title:str
    author: str
    year: int
    
#for save data in memory
new_books_db = []

#to add a book ✅
@router.post("/newbooks")
def addNewBook(book: Book):
    new_books_db.append(book)
    return {"message": "Book added successfully!", "book": book}

#try in swagger UI
#http://127.0.0.1:8000/docs and send a book 

#just to test if the book is sent correctly ✅
@router.get("/newbooks/all")
def showNewBooks():
    return new_books_db


