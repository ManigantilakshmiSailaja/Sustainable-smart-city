from fastapi import FastAPI, UploadFile, File
from utils import summarize_text, forecast_kpi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

@app.post("/summarize/")
async def summarize(file: UploadFile = File(...)):
    content = await file.read()
    summary = summarize_text(content.decode("utf-8"))
    return {"summary": summary}

@app.post("/forecast/")
async def forecast_kpi_route(file: UploadFile = File(...)):
    content = await file.read()
    result = forecast_kpi(content.decode("utf-8"))
    return {"forecast": result}
