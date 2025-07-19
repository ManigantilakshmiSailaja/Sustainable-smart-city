from fastapi import APIRouter, Form
from datetime import datetime
import json
import os

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.post("/")
def submit_feedback(name: str = Form(...), issue: str = Form(...), category: str = Form(...)):
    feedback_data = {
        "name": name,
        "issue": issue,
        "category": category,
        "timestamp": datetime.now().isoformat()
    }
    feedback_file = "data/feedback.json"
    os.makedirs("data", exist_ok=True)
    if os.path.exists(feedback_file):
        with open(feedback_file, "r") as f:
            all_feedback = json.load(f)
    else:
        all_feedback = []
    all_feedback.append(feedback_data)
    with open(feedback_file, "w") as f:
        json.dump(all_feedback, f, indent=4)
    return {"message": "Feedback submitted successfully"}