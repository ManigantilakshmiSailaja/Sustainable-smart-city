from pydantic import BaseModel

class TextSummaryRequest(BaseModel):
    text: str

class TextSummaryResponse(BaseModel):
    summary: str

class ForecastResponse(BaseModel):
    forecast: float
