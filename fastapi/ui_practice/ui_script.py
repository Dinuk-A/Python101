from fastapi import APIRouter
from typing import Optional

router = APIRouter()

users = [
    {
        "emp_id": 1, 
        "name": "John Doe", 
        "roles": ["admin", "developer"],
        "active": True
    },
    {
        "emp_id": 2, 
        "name": "Jane Smith", 
        "roles": ["manager", "hr"],
        "active": True
    },
    {
        "emp_id": 3, 
        "name": "Bob Wilson", 
        "roles": ["developer"],
        "active": False
    },
    {
        "emp_id": 4, 
        "name": "Alice Brown", 
        "roles": ["admin", "manager"],
        "active": True
    }
]

# for basic GET
@router.get("/ui/users")
def showAllUsers():
    
    return {"users": users}

# GET + path param
@router.get("/ui/user/{emp_id}")
def getUserByEmpId(emp_id:int):

    if emp_id < 1  or emp_id > len(users)  :
        return {"error": "user not available"}
    else:
        return{"users": users[emp_id-1]}

# GET + multi path param
@router.get("/ui/user/{emp_id}/roles")
def getUserRoles(emp_id:int):
    
    # Find user by actual emp_id field, not list position
    user = next((u for u in users if u["emp_id"] == emp_id), None)

    if not user  :
        return {"error": "user not available"}
    else:
        return{"roles": users[emp_id-1]["roles"]}
