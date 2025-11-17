from fastapi import APIRouter

router = APIRouter()

#define root directory ✅ 
@router.get("/")
def root():
    return  {"message": "Hello, FastAPI!"}

#a custom route
@router.get("/user")
def get_user():
    return {"user": "Welcome user!"}

#we cannot redefine the same route, it will always take the first one defined ✅