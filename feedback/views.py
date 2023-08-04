from datetime import datetime

from django.conf import settings
from django.utils.timezone import get_current_timezone
from feedback.serializers import EmailFormSerializer
from rest_framework import status, views
from rest_framework.decorators import action
from rest_framework.response import Response

from .utils import send_feedback_by_email, send_feedback_by_telegram


class EmailFormView(views.APIView):
    serializer_class = EmailFormSerializer

    @staticmethod
    def _send_to_email(
        to: str, email: str, name: str, message: str, created: str
    ) -> None:
        send_feedback_by_email.delay(
            to=to, email=email, name=name, message=message, created=created
        )

    @staticmethod
    def _send_to_telegram(
        chat_id: id, email: str, name: str, message: str, created: str
    ) -> None:
        send_feedback_by_telegram.delay(
            chat_id=chat_id, email=email, name=name, message=message, created=created
        )

    @action(methods=["post"], detail=True)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        created = (
            datetime.now()
            .replace(tzinfo=get_current_timezone())
            .strftime("%Y-%m-%d %H:%M:%S")
        )
        self._send_to_email(
            to=settings.EMAIL_CUSTOMER_EMAIL,
            created=created,
            **serializer.validated_data
        )
        self._send_to_telegram(
            chat_id=settings.TELEGRAM_CHAT_ID,
            created=created,
            **serializer.validated_data
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
