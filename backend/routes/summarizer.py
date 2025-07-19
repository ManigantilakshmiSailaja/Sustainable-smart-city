from fastapi import APIRouter, UploadFile
from utils.granite_api import summarize_text

router = APIRouter(prefix="/summarize", tags=["Summarizer"])




@router.post("/")
async def summarize_file(file: UploadFile):
    content = await file.read()
    summary = summarize_text(content.decode())
    return {"summary": summary}