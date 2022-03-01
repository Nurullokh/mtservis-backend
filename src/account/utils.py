from django.conf import settings
from django.template.loader import render_to_string

from sendgrid import Mail, SendGridAPIClient

from config.celery import app


@app.task
def send_email(email, code, message):
    subject = "Verification code"
    message = render_to_string(
        "account/email.html", {"code": code, "message": message}
    )
    message = Mail(
        from_email=settings.SENDER_EMAIL,
        to_emails=[email],
        subject=subject,
        html_content=message,
    )
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    sg.send(message)
