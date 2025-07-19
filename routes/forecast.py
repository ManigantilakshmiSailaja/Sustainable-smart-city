from fastapi import APIRouter, UploadFile
import pandas as pd
from utils.ml import forecast_kpi

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.post("/")
async def forecast_kpi_route(file: UploadFile):
    df = pd.read_csv(file.file)
    prediction = forecast_kpi(df)
    return {"next_year_prediction": prediction}