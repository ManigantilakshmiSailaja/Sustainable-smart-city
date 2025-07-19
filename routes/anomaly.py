from fastapi import APIRouter, UploadFile
import pandas as pd
from scipy.stats import zscore

router = APIRouter(prefix="/anomaly", tags=["Anomaly Detection"])

@router.post("/")
async def detect_anomalies(file: UploadFile):
    df = pd.read_csv(file.file)
    z_scores = zscore(df.iloc[:, 1])
    anomalies = df[z_scores > 2]
    return {"anomalies": anomalies.to_dict(orient="records")}