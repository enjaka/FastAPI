from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return { "message": "Hello World"}

@app.get("/moje")
async def welcome() -> dict:
    return { "message": "To je pa moje"}

app.include_router(todo_router)
