import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template


class SendEmailService:
    @classmethod
    def _send_email(cls, to: str, from_email: str, subject: str, message: str) -> None:
        message = EmailMessage(
            to=(to,), from_email=from_email, subject=subject, body=message
        )
        message.content_subtype = "html"
        message.send()

    @classmethod
    def send_email_template(
        cls, to: str, subject: str, template: str, **kwargs
    ) -> None:
        message = get_template(template).render(kwargs)
        cls._send_email(
            to=to, from_email=settings.EMAIL_HOST_USER, subject=subject, message=message
        )


class TelegramService:
    @classmethod
    def _send_message(cls, chat_id: int, message: str) -> int:
        r = requests.post(
            f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        )
        return r.status_code

    @classmethod
    def send_telegram_message_template(cls, chat_id: int, template: str, **kwargs):
        message = template.format(kwargs)
        cls._send_message(chat_id=chat_id, message=message)


@shared_task
def send_feedback_by_email(to, **kwargs):
    SendEmailService.send_email_template(
        to=to, subject="Новая заявка", template="contact_us.html", **kwargs
    )


@shared_task
def send_feedback_by_telegram(chat_id: int, **kwargs):
    message = "Новое обращение\nemail - {email}\nname - {name}\nmessage - {message}\ncreated - {created}"
    TelegramService.send_telegram_message_template(
        chat_id=chat_id, template=message, **kwargs
    )
