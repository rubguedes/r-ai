from fastapi import FastAPI
from app.api.conversations import router as conversations_router

from app.exceptions.app_exceptions import AppException
from app.exceptions.handlers import app_exception_handler

app = FastAPI()
# uvicorn app.main:app --reload


@app.get("/")
def health_check():
    return {"status": "OK!"}


app.include_router(conversations_router)

app.add_exception_handler(AppException, app_exception_handler)
