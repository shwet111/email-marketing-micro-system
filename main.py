from fastapi import FastAPI, UploadFile, File, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
from email_sender import send_email
from db import update_status

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def upload_page(request: Request):
    return templates.TemplateResponse(request, "upload.html", {"request": request})

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    df = pd.read_csv(file.file)

    for _, row in df.iterrows():
        background_tasks.add_task(send_email, row.to_dict())

    return {"message": "Emails queued successfully"}

@app.post("/bounce")
async def handle_bounce(data: dict):
    email = data.get("email")
    update_status(email, "bounced")
    return {"message": f"Bounce recorded for {email}"}