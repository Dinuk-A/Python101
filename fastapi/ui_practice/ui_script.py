from fastapi import APIRouter
from typing import Optional

router = APIRouter()

# for basic GET
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 28},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 34},
    {"id": 3, "name": "Bob Wilson", "email": "bob@example.com", "age": 45},
    {"id": 4, "name": "Alice Brown", "email": "alice@example.com", "age": 29}
]

# for basic GET
@router.get("/ui/users")
def showAllUsers():
    return {"users": users}

# GET + path param
@router.get("/ui/users/{u_id}")
def getUserById(u_id:int):
    if u_id < 1  or u_id > len(users)  :
        return {"error": "user not available"}
    else:
        return{"users": users[u_id]}