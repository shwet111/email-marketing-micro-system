from celery import Celery
from email_sender import send_email

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def send_email_task(user_data):
    send_email(user_data)