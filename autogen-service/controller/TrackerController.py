from fastapi import APIRouter

# Create an instance of APIRouter
router = APIRouter()

# Define your API routes here
@router.get("/")
async def example():
    return {"message": "Hello World from controllers.py"}
