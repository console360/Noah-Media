# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from noah import custom_status_codes
from noah import responses
from .models import Miscellaneous
from .serializers import MiscellaneousSerializer


class MiscellaneousFeatures(APIView):

    @swagger_auto_schema(tags=['Miscellaneous'])
    def get(self, requests, slug=None):
        if slug is None:
            data = Miscellaneous.objects.all()
            serialized_data = MiscellaneousSerializer(data, many=True)
            return Response(responses.generate_success_response(custom_status_codes.SENT_ALL_MISCELLANEOUS_PAGE,
                                                                payload=serialized_data.data),
                            status=status.HTTP_200_OK)

        try:
            data_obj = Miscellaneous.objects.get(slug=slug)
        except Miscellaneous.DoesNotExist:
            return Response(responses.generate_failure_response(custom_status_codes.MISCELLANEOUS_ERR_SLUG, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)

        serialized_data = MiscellaneousSerializer(data_obj)
        return Response(responses.generate_success_response(custom_status_codes.MISCELLANEOUS_SUCCESS,
                                                            payload=serialized_data.data),
                        status=status.HTTP_200_OK)
