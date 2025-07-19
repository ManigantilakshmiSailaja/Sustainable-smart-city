from fastapi import FastAPI
from routes import summarizer, feedback, eco_tips, forecast, chat, anomaly

app = FastAPI(title="Sustainable Smart City Assistant")
from transformers import BartTokenizer, BartForConditionalGeneration
import os

model_path = os.path.join(os.path.dirname(__file__), "..", "bart-large-cnn")

tokenizer = BartTokenizer.from_pretrained(model_path)
model = BartForConditionalGeneration.from_pretrained(model_path)


app.include_router(summarizer.router)
app.include_router(feedback.router)
app.include_router(eco_tips.router)
app.include_router(forecast.router)
app.include_router(chat.router)
app.include_router(anomaly.router)