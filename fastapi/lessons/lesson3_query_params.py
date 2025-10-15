
from fastapi import APIRouter
from typing import Optional

router = APIRouter()

# query param basic ✅
books_db = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"id": 3, "title": "The Silmarillion", "author": "J.R.R. Tolkien"},
    {"id": 4, "title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling"},
    {"id": 5, "title": "Harry Potter and the Chamber of Secrets", "author": "J.K. Rowling"},
    {"id": 6, "title": "Harry Potter and the Prisoner of Azkaban", "author": "J.K. Rowling"},
    {"id": 7, "title": "Harry Potter and the Goblet of Fire", "author": "J.K. Rowling"},
    {"id": 8, "title": "Harry Potter and the Order of the Phoenix", "author": "J.K. Rowling"},
    {"id": 9, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 10, "title": "The Clean Coder", "author": "Robert C. Martin"},
    {"id": 11, "title": "Clean Architecture", "author": "Robert C. Martin"},
    {"id": 12, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    {"id": 13, "title": "Pragmatic Thinking and Learning", "author": "Andrew Hunt"},
    {"id": 14, "title": "Programming Ruby", "author": "Andrew Hunt"},
]


@router.get("/books/")
def searchBooks(author: Optional[str]=None,title: Optional[str]=None, limit: int = 3):
    
    filteredBooks = books_db
    
    if author:
        filteredBooks = [b for b in filteredBooks if author.lower() in b["author"].lower() ]
    
    if title:
        filteredBooks = [b for b in filteredBooks if title.lower() in b["title"].lower()]
    
    return{"results": filteredBooks[:limit]}

# to test without limit
    #return{"results": filteredBooks}
   
#http://127.0.0.1:8000/books/?author=tolkien
#http://127.0.0.1:8000/books/?title=code
#http://127.0.0.1:8000/books/?author=martin&title=clean

#a custom limit
#http://127.0.0.1:8000/books/?title=Harry%20Potter&limit=4
