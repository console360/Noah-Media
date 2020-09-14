from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
from noah import responses, constants
from noah.custom_status_codes import TUTORIALS_LIST_SENT, TUTORIAL_WITH_SPECIFY_ID_NOT_FOUND
from noah.permissions import IsAuthenticated
from noah.utils import get_paginated_response
from tutorials.models import Tutorial

# Create your views here.
from tutorials.serializers import TutorialSerializer


class TutorialsListAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Tutorial'])
    def get(self, request):
        page = self.request.query_params.get('page')

        tutorials = Tutorial.objects.all().exclude(is_deleted=True)
        payload = get_paginated_response(tutorials, page, constants.RECORD_PER_PAGE)
        serializer = TutorialSerializer(payload['results'], many=True)
        payload['results'] = serializer.data

        return Response(responses.generate_success_response(TUTORIALS_LIST_SENT, payload=payload), status=status.HTTP_200_OK)


class GetTutorialAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Tutorial'])
    def get(self, request, tutorial_id):

        try:
            tutorial = Tutorial.objects.exclude(is_deleted=True).get(id=tutorial_id)

            serializer = TutorialSerializer(tutorial)

            return Response(responses.generate_success_response(TUTORIALS_LIST_SENT, payload=serializer.data),
                            status=status.HTTP_200_OK)

        except Tutorial.DoesNotExist:
            return Response(responses.generate_failure_response(TUTORIAL_WITH_SPECIFY_ID_NOT_FOUND, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)
