from spammail.celery import app

from .service import send_email


@app.task
def send_some_email(mail):
    """
    Sending test email using celery

    """
    send_email(mail)
