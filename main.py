app = FastAPI()

from fastapi import FastAPI
from pydantic import BaseModel
import dateparser
from datetime import datetime

class Message(BaseModel):
    text: str
    phone: str


def extract_event(text):
    text_lower = text.lower()

    # detect event type
    if "exam" in text_lower:
        title = "Exam"
    elif "assignment" in text_lower:
        title = "Assignment"
    elif "meeting" in text_lower:
        title = "Meeting"
    else:
        title = "Event"

    # detect date/time
    parsed_date = dateparser.parse(text)

    if parsed_date is None:
        parsed_date = datetime.now()

    return title, parsed_date


@app.get("/")
def home():
    return {"message": "CampusFlow AI API running"}


@app.post("/process")
def process_message(msg: Message):

    title, event_time = extract_event(msg.text)

    insight = "Start preparing early to avoid last minute stress."

    return {
        "title": title,
        "datetime": event_time.isoformat(),
        "phone": msg.phone,
        "insight": insight
    }
