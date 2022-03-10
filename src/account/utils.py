import re

from django.conf import settings
from django.template.loader import render_to_string

from rest_framework.exceptions import ValidationError
from sendgrid import Mail, SendGridAPIClient

from config.celery import app


@app.task
def send_email(email, code, message, full_name):
    subject = "Verification code"
    message = render_to_string(
        "account/email.html",
        {"code": code, "message": message, "full_name": full_name},
    )
    print(settings.SENDGRID_API_KEY)
    message = Mail(
        from_email=settings.SENDER_EMAIL,
        to_emails=[email],
        subject=subject,
        html_content=message,
    )

    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
    sg.send(message)
    print("-" * 100)


def validate_password(password):
    if len(password) < settings.PASSWORD_LENGTH:
        raise ValidationError("Minimum 10 characters.")
    elif not re.search("[a-z]", password):
        raise ValidationError("The alphabets must be between [a-z].")
    elif not re.search("[A-Z]", password):
        raise ValidationError(
            "At least one alphabet should be of Upper Case [A-Z]."
        )
    elif not re.search("[0-9]", password):
        raise ValidationError("At least 1 number or digit between [0-9].")
    elif not re.search("[_@$()#&]", password):
        raise ValidationError("At least 1 character from [_@$()#&]")
    elif re.search("\s", password):  # noqa
        raise ValidationError("No space between characters.")


def validate_phone(phone):
    if len(phone) < 13 or not phone[1:].isdecimal():
        raise ValidationError("Invalid phone number.")


def validate_zip(zip_code):
    if len(zip_code) < 6 or not zip_code.isdecimal():
        raise ValidationError("Invalid zip code.")
