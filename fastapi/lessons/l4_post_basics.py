from fastapi import APIRouter

# pydantic is a data validation library used by FastAPI, not part of FastAPI itself,
# which allows defining data models with type annotations.
# helps define, validate, and parse data easily
from pydantic import BaseModel

router = APIRouter()

# LESSON 1 ✅

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

#if the payload data doesnt match the pydantic model, fastapi will return a 422 Unprocessable Entity error
# (ex: change a letter in "year" to make it "yearr" and try to send the book again)

#just to test if the book is sent correctly ✅
@router.get("/newbooks/all")
def showNewBooks():
    return new_books_db

# LESSON 2 ✅
# post manually, without swagger,use >>> python l4_post_manual_client.py
# modal & functions are defined here, but a separate client file is used to send the post request

# install the library>>.  pip install requests 

people_db = []

class Person(BaseModel):
    name: str
    age: int

# to add a person 
@router.post("/person/add")
def addNewPerson(person: Person):
    people_db.append(person)
    return {"message": "Person added successfully!", "person": person}

# to get all users
@router.get("/person/all")
def getAllPeople():
    return people_db

# LESSON 3 ✅
# POST with path params
# execution added to the lessons\l5_post_params.py

user_orders = {
    1: {"name": "Alice", "orders": []},
    2: {"name": "Bob", "orders": []}
}

class Order(BaseModel):
    id: int
    item: str    

@router.post("/users/{user_id}/orders")
def add_order(user_id: int, order: Order):
    
    if user_id not in user_orders:
        return {"error": "User not found"}

    #only send the name (store it)
    #user_orders[user_id]["orders"].append(order.item)
    
    # store full order object
    user_orders[user_id]["orders"].append(order.model_dump())
    
    return {"message": "Order added", "orders": user_orders[user_id]["orders"]}

# to get all new users
@router.get("/userorders/all")
def getAllUserOrders():
    return user_orders