from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
from noah import responses, constants
from noah.custom_status_codes import TEMPLATES_LIST_SENT, TEMPLATE_WITH_SPECIFY_ID_NOT_FOUND, \
    TEMPLATE_WITH_SPECIFY_ID_SENT
from noah.permissions import IsAuthenticated
from templates.models import Template
from noah.utils import get_paginated_response
from templates.serializers import TemplateSerializer


class TemplatesListAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Template'])
    def get(self, request):
        page = self.request.query_params.get('page')

        templates = Template.objects.filter(is_deleted=False)
        payload = get_paginated_response(templates, page, constants.RECORD_PER_PAGE)
        serializer = TemplateSerializer(payload['results'], many=True)
        payload['results'] = serializer.data

        return Response(responses.generate_success_response(TEMPLATES_LIST_SENT, payload=payload), status=status.HTTP_200_OK)


class GetTemplateAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Template'])
    def get(self, request, template_id):

        try:
            tutorial = Template.objects.exclude(is_deleted=True).get(id=template_id)

            serializer = TemplateSerializer(tutorial)

            return Response(responses.generate_success_response(TEMPLATE_WITH_SPECIFY_ID_SENT, payload=serializer.data),
                            status=status.HTTP_200_OK)

        except Template.DoesNotExist:
            return Response(responses.generate_failure_response(TEMPLATE_WITH_SPECIFY_ID_NOT_FOUND, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)
