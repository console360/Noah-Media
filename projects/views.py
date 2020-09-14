from drf_yasg import openapi
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from noah import responses
from noah.custom_status_codes import PROJECTS_LIST_SENT, TEMPLATE_ID_NOT_PROVIDED, TEMPLATE_WITH_SPECIFY_ID_NOT_FOUND, \
    TEMPLATE_DOES_NOT_HAVE_PARTS, PROJECT_CREATED_SUCCESSFULLY, PROJECT_DOES_NOT_EXISTS, INVALID_PROJECT_DETAIL, \
    PROJECT_UPDATED_SUCCESSFULLY, PROJECT_PART_DOES_NOT_EXISTS, EMPTY_BLOCK_ERROR, PROJECT_PART_BLOCK_CREATED, \
    PROJECT_PART_BLOCK_UPDATED, INVALID_PROJECT_PART_BLOCK_DETAIL, PROJECT_PART_BLOCK_DOES_NOT_EXISTS, \
    ONE_PROJECT_PART_BLOCK_NEED
from noah.permissions import IsAuthenticated
from projects.models import Project, ProjectPart, ProjectPartBlock
from projects.serializers import CreateProjectSerializer, GetProjectSerializer, UpdateProjectSerializer, \
    GetProjectPartBlockSerializer, UpdateProjectPartBlockSerializer
from templates.models import Template, TemplatePart

from drf_yasg.utils import swagger_auto_schema


class ProjectsCreateListAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Project'], operation_summary='Create project from templates',
                         request_body=CreateProjectSerializer)
    def post(self, request):
        serializer = CreateProjectSerializer(data=request.data)

        if not serializer.is_valid():
            # template id isn't provided
            return Response(responses.generate_failure_response(TEMPLATE_ID_NOT_PROVIDED, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            # Initiate project
            template = Template.objects.get(id=serializer.data['template'])

            template_parts = TemplatePart.objects.filter(template=template, is_deleted=False)

            if template_parts.count() <= 0:
                return Response(responses.generate_failure_response(TEMPLATE_DOES_NOT_HAVE_PARTS, payload={}),
                                status=status.HTTP_400_BAD_REQUEST)

            project = Project.objects.init_project(template, request.user)

            for template_part in template_parts:
                project_part = ProjectPart.objects.init_project_part(template_part, project)

                project_part_block = ProjectPartBlock.objects.init_project_part_block(project_part)

            # Get created project
            project_serializer = GetProjectSerializer(project)

            return Response(
                responses.generate_success_response(PROJECT_CREATED_SUCCESSFULLY, payload=project_serializer.data),
                status=status.HTTP_201_CREATED)

        except Template.DoesNotExist:
            return Response(responses.generate_failure_response(TEMPLATE_WITH_SPECIFY_ID_NOT_FOUND, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=['Project'], operation_summary='Get project list based on status', manual_parameters=[
        openapi.Parameter('status', openapi.IN_QUERY, description="Project status. (Draft: 0, Completed: 1)",
                          type=openapi.TYPE_INTEGER)])
    def get(self, request):

        projects = Project.objects.exclude(is_deleted=True)

        project_status = self.request.query_params.get('status', None)
        if project_status is not None:
            projects = projects.filter(status=project_status)

        serializer = GetProjectSerializer(projects, many=True)

        return Response(
            responses.generate_success_response(PROJECTS_LIST_SENT, payload=serializer.data))


class ProjectGetUpdateAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Project'], operation_summary='Get particular project')
    def get(self, request, project_id=None):

        projects = Project.objects.exclude(is_deleted=True)

        if project_id is not None:
            projects = projects.filter(id=project_id)

        serializer = GetProjectSerializer(projects, many=True)

        return Response(
            responses.generate_success_response(PROJECTS_LIST_SENT, payload=serializer.data))

    @swagger_auto_schema(tags=['Project'], operation_summary="Update project details.",
                         operation_description='Update project details. e.g., Title. Delete project using is_deleted.',
                         request_body=UpdateProjectSerializer)
    def patch(self, request, project_id=None):
        try:
            project = Project.objects.get(id=project_id)

            serializer = UpdateProjectSerializer(project, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response(responses.generate_failure_response(INVALID_PROJECT_DETAIL, payload=serializer.errors),
                                status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response(
                responses.generate_success_response(PROJECT_UPDATED_SUCCESSFULLY, payload=serializer.data),
                status=status.HTTP_201_CREATED)

        except Project.DoesNotExist:
            return Response(responses.generate_failure_response(PROJECT_DOES_NOT_EXISTS, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)


class ProjectPartBlocksCreateAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Project Blocks'], operation_summary='Create/Add new block to part of project')
    def post(self, request, project_id, part_id):
        try:
            project = Project.objects.exclude(is_deleted=True).get(id=project_id)
            project_part = ProjectPart.objects.exclude(is_deleted=True).get(id=part_id, project=project)

            project_part_blocks = ProjectPartBlock.objects.filter(project_part=project_part, is_deleted=False).order_by(
                '-block_letter')

            # If there is only one  block and empty description then don't allow to create a block
            if project_part_blocks.count() > 0 and not project_part_blocks.first().description:
                serializer = GetProjectPartBlockSerializer(project_part_blocks.first())
                return Response(responses.generate_failure_response(EMPTY_BLOCK_ERROR, payload=serializer.data),
                                status=status.HTTP_400_BAD_REQUEST)

            # Get next block letter
            block_letter = 'A'
            if project_part_blocks.count() > 0:
                block_letter = project_part_blocks.first().block_letter

            next_block_letter = chr(ord(block_letter) + 1)

            # Create block with next block letter
            project_part_block = ProjectPartBlock.objects.create_project_part_block(project_part, next_block_letter)

            serializer = GetProjectPartBlockSerializer(project_part_block)

            return Response(
                responses.generate_success_response(PROJECT_PART_BLOCK_CREATED, payload=serializer.data),
                status=status.HTTP_201_CREATED)

        except Project.DoesNotExist:
            return Response(responses.generate_failure_response(PROJECT_DOES_NOT_EXISTS, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)
        except ProjectPart.DoesNotExist:
            return Response(responses.generate_failure_response(PROJECT_PART_DOES_NOT_EXISTS, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)


class ProjectPartBlockUpdateAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(tags=['Project Blocks'], operation_summary='Update/Delete block details',
                         request_body=UpdateProjectPartBlockSerializer)
    def patch(self, request, project_id, part_id, block_id):
        try:
            project = Project.objects.exclude(is_deleted=True).get(id=project_id)
            project_part = ProjectPart.objects.exclude(is_deleted=True).get(id=part_id, project=project)

            # Create block with next block letter
            project_part_block = ProjectPartBlock.objects.exclude(is_deleted=True).get(id=block_id,
                                                                                       project_part=project_part)

            serializer = UpdateProjectPartBlockSerializer(project_part_block, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response(
                    responses.generate_failure_response(INVALID_PROJECT_PART_BLOCK_DETAIL, payload=serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST)

            # Block delete procedure
            if 'is_deleted' in request.data and request.data['is_deleted']:
                total_project_part_blocks = ProjectPartBlock.objects.exclude(is_deleted=True).filter(
                    project_part=project_part)
                if total_project_part_blocks.count() <= 1:
                    return Response(
                        responses.generate_failure_response(ONE_PROJECT_PART_BLOCK_NEED,
                                                            payload=serializer.data),
                        status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response(
                responses.generate_success_response(PROJECT_PART_BLOCK_UPDATED, payload=serializer.data),
                status=status.HTTP_201_CREATED)

        except Project.DoesNotExist:
            return Response(responses.generate_failure_response(PROJECT_DOES_NOT_EXISTS, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)
        except ProjectPart.DoesNotExist:
            return Response(responses.generate_failure_response(PROJECT_PART_DOES_NOT_EXISTS, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)
        except ProjectPartBlock.DoesNotExist:
            return Response(responses.generate_failure_response(PROJECT_PART_BLOCK_DOES_NOT_EXISTS, payload={}),
                            status=status.HTTP_400_BAD_REQUEST)
