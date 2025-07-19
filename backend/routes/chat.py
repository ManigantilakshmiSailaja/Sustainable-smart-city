from fastapi import APIRouter
from utils.granite_api import granite_chat

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.get("/")
def chat_response(question: str):
    return {"answer": granite_chat(question)}