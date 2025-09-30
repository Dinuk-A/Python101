from fastapi import FastAPI

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


