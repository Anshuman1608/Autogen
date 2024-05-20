from fastapi import APIRouter
from pydantic import BaseModel
import requests
from services.userservice import Service

router = APIRouter()

class Register(BaseModel):
    name: str
    email: str
    password: str

# Define your API routes here
@router.get("/")
async def example():
    return {"message": "Hello World from controllers.py"}

@router.post("/register")
async def register_user(register:Register):
    name = register.name
    email = register.email
    password = register.password
    service_instance = Service(name, email, password) 
    return service_instance.register_user(name, email, password)
