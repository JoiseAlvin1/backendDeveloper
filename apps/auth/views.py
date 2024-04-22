import logging
from rest_framework.generics import ListAPIView, UpdateAPIView
from apps.baselayer.baseapiviews import BaseAPIView
from django.conf import settings
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

logger = logging.getLogger(settings.LOGGER_NAME_PREFIX + __name__)


class AccessTokenAPIView(BaseAPIView, ListAPIView, UpdateAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.filter(username=request.data.get("username")).first()
            print(user)
            if not user:
                return self.send_not_found_response(
                    message="user not found",
                    msg_code=0
                )
            else:
                token, created = Token.objects.get_or_create(user=user)
                return self.send_success_response(
                    message="Token successfully retrieved.",
                    msg_code=1,
                    data = {"token": token.key}
                )
        except Exception as err:
            logger.error(err)
            return self.send_internal_server_error_response(
                msg_code=1, message="Something went wrong!"
            )
