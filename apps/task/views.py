import logging
from django.http import Http404
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from django.core.exceptions import ObjectDoesNotExist
from apps.baselayer.baseapiviews import BaseAPIView, get_first_error_message_from_serializer_errors
from django.conf import settings
from apps.task.serializer import TaskSerializer
from apps.task.models import Task

logger = logging.getLogger(settings.LOGGER_NAME_PREFIX + __name__)


class TaskAPIView(BaseAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ["name"]
    ordering = ["-name"]  # default ordering field

    def post(self, request, *args, **kwargs):
        try:
            serializer_data = self.serializer_class(data=request.data)
            if not serializer_data.is_valid():
                return self.send_bad_request_response(
                    msg_code=1,
                    message=get_first_error_message_from_serializer_errors(
                        serializer_data.errors
                    ),
                    errors_details=serializer_data.errors,
                )
            serializer_data.save()
            return self.send_created_response(
                msg_code=0,
                message="Task created.",
                data=serializer_data.data,
            )

        except Exception as err:
            logger.error(err)
            return self.send_internal_server_error_response(
                msg_code=1, message="Something went wrong!"
            )

    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            if pk:
                try:
                    self.get_queryset().get(pk=pk)
                except ObjectDoesNotExist:
                    return self.send_not_found_response(msg_code=1)
                data = self.retrieve(request, *args, **kwargs).data
            else:
                # Retrieve a list of objects if pk is not provided
                data = self.list(request, *args, **kwargs).data
            return self.send_success_response(
                data=data, message="Success", msg_code=0
            )
        except Exception as err:
            logger.exception(err)
            return self.send_bad_request_response(
                msg_code=1, message="Something went wrong!"
            )

    def patch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer_data = self.serializer_class(data=request.data, instance=instance, partial=True)
            if not serializer_data.is_valid():
                return self.send_bad_request_response(
                    msg_code=1,
                    message=get_first_error_message_from_serializer_errors(
                        serializer_data.errors
                    ),
                    errors_details=serializer_data.errors,
                )
            serializer_data.save()
            return self.send_created_response(
                msg_code=0,
                message="Task updated.",
                data=serializer_data.data,
            )

        except Exception as err:
            logger.error(err)
            return self.send_internal_server_error_response(
                msg_code=1, message="Something went wrong!"
            )

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return self.send_created_response(
                msg_code=0,
                message="Task deleted.",
                data={},
            )
        except Http404 as err:
            return self.send_not_found_response(msg_code=1, message="Invalid record.")

        except Exception as err:
            print(type(err))
            logger.error(err)
            return self.send_internal_server_error_response(
                msg_code=1, message="Something went wrong!"
            )
