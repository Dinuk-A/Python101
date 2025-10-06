from fastapi import FastAPI
from typing import Optional

app = FastAPI()

#define root directory ✅ 
@app.get("/")
def root():
    return  {"message": "Hello, FastAPI!"}

#a custom route
@app.get("/user")
def get_user():
    return {"user": "Welcome user!"}

#we cannot redefine the same route, it will always take the first one defined ✅

# path parameter example ✅
items = []
@app.get("/items/{item_name}")
def read_item(item_name):
    items.append(item_name)
    return {"all items": items}
#in browser > http://127.0.0.1:8000/items/any_name_here

# path parameter with type validation ✅
item_ids = []
@app.get("/itemids/{item_id}")
def read_item(item_id:int):
    item_ids.append(item_id)
    return {"all item_ids": item_ids}

# show diff redults in browser when accessing the same route with different path parameters ✅
@app.get("/user/greet/{username}")
def greet_user(username: str):
    return {"message": f"Hello, {username}!"}
#by default this will accept ints too, to prevent that, use an IF before return > username.isDigit() ... 

# real world simple example ✅
users = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    if 0 <= user_id < len(users):
        return users[user_id]
    return {"error": "User not found"}

# multiple path params example ✅
users2 = [
    {"id": 0, "name": "Alice", "orders": ["Book", "Pen"]},
    {"id": 1, "name": "Bob", "orders": ["Laptop"]},
    {"id": 2, "name": "Charlie", "orders": ["Notebook", "Pencil", "Eraser"]}
]

@app.get("/userorder/{uid}/order/{ord_id}")
def get_user_and_order(uid: int, ord_id:int):
    
    #first validate user ids
    if 0 <= uid < len(users2):        
        user = users2[uid]        
        #then validate orders
        if 0<= ord_id < len(user["orders"] ):
            return {"username" : user["name"], "order": user["orders"][ord_id] }        
        else: 
            return {"error":"order not found"}               
    else:
        return {"error":"user not found"}
# test in browser >> http://127.0.0.1:8000/userorder/1/order/0

# query param basic
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


@app.get("/books/")
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





