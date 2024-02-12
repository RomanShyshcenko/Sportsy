from django.shortcuts import get_object_or_404

from core.settings.celery import app
from celery.utils.log import get_task_logger
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from user.services.email_service import EmailService

User = get_user_model()
logger = get_task_logger(__name__)


@app.task(name='send_verify_email')
def send_verify_email(user: User):
    logger.info(f'Sending verification email to {user}')
    EmailService.send_activation_email(user)


@app.task(name='send_reset_password_email')
def send_reset_password_email(email: str):
    logger.info(f'Sending reset password email to {email}')
    user = get_object_or_404(User, email=email)

    return EmailService.send_password_reset_email(user)
