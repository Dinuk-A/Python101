from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# mock data for GET lessons
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

# for basic GET ✅
@router.get("/ui/users")
def showAllUsers():
    
    return {"users": users}

# GET + path param ✅
@router.get("/ui/user/{emp_id}")
def getUserByEmpId(emp_id:int):

    if emp_id < 1  or emp_id > len(users)  :
        return {"error": "user not available"}
    else:
        return{"user": users[emp_id-1]}

# GET + multi path param ✅
@router.get("/ui/user/{emp_id}/roles")
def getUserRoles(emp_id:int):
    
    # Find user by actual emp_id field, not list position
    user = next((u for u in users if u["emp_id"] == emp_id), None)

    if not user  :
        return {"error": "user not available"}
    else:
        return{"roles": users[emp_id-1]["roles"]}
    
# GET + query param ✅
@router.get("/ui/users/role/")
def getUsersByRole(roleName: str):

    filteredUsers = [u for u in users if roleName.lower() in [r.lower() for r in u["roles"]]]

    return {"users by role" :filteredUsers }
    
# GET + multi query param ✅
# http://127.0.0.1:8000/ui/users/byrolenstatus/?roleName=developer&activeStatus=false
@router.get("/ui/users/byrolenstatus/")
def getUsersByRoleAndStatus(roleName: str, activeStatus: bool):

    filteredUsers = [
        user for user in users
        if roleName.lower() in [r.lower() for r in user["roles"]]
        and user["active"] == activeStatus
    ]

    return {"results": filteredUsers}

# GET + path + query (combined) ✅
@router.get("/ui/user/mult/{emp_id}/")
# http://127.0.0.1:8000/ui/user/mult/3/?roleName=developer
def getUserCombined(emp_id: int, roleName: str):

    if 0 < emp_id and emp_id < len(users):

        userByEmpId = [user for user in users if user["emp_id"]==emp_id]

        if userByEmpId != []:
            userByRole = [u for u in userByEmpId if roleName.lower() in u["roles"]]
            return {"results": userByRole}

        else:
            return{"results": "user not found for this role for this emp id"}
        
    else:
        return{"results": "user not found for this emp id"}

# ================POST =====================

# mock data for POST lessons ✅
randomThings = ["cat",150.00,True,"abCD"]

namesArray = ["tom","batman"]

# data models for POST lessons ✅

# for random things array - this will accept any type
class RandomItem(BaseModel):
    value:str | int | bool | float
 
# for names array
class Name(BaseModel):
    nameVal:str

# basic POST (accept any type) ✅
@router.post("/ui/post/random")
def add_randomThing(thing: RandomItem):
    randomThings.append(thing.value)
    print(f'added: {thing}')
    return {"message":"random bs added successfully","added":thing}

# POST only strings are accepted
@router.post("/ui/post/names")
def addNames(name: Name):
    namesArray.append(name.nameVal)
    return {"message":"name added successfully","added":name}

# simple GET for show random things array (just to show results of above POST)
@router.get("/ui/postexm/get/rndmthngs")
def getRandomThings():
    return {"random things":randomThings}

# simple GET for show names array (just to show results of above POST)
@router.get("/ui/postexm/get/names")
def getNames():
    return {"names":namesArray}


