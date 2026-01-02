from fastapi import APIRouter
from typing import Optional


router = APIRouter()

users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 28},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 34},
    {"id": 3, "name": "Bob Wilson", "email": "bob@example.com", "age": 45},
    {"id": 4, "name": "Alice Brown", "email": "alice@example.com", "age": 29}
]

@router.get("/ui/users")
def showAllUsers():
    return {"users": users}