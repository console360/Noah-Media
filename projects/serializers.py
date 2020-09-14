from collections import OrderedDict

from rest_framework import serializers

from projects.models import ProjectPartBlock, ProjectPart, Project


class CreateProjectSerializer(serializers.Serializer):
    template = serializers.UUIDField(allow_null=False, required=True)

    class Meta:
        swagger_schema_fields = {
            'example': OrderedDict([('template', 'a0d67b99-854a-4aa3-b730-3d6ba58fee27')])}

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GetProjectPartBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPartBlock
        fields = '__all__'


class GetProjectPartAndBlockSerializer(serializers.ModelSerializer):
    project_part_blocks = GetProjectPartBlockSerializer(many=True)

    class Meta:
        model = ProjectPart
        fields = '__all__'


class GetProjectSerializer(serializers.ModelSerializer):
    project_parts = GetProjectPartAndBlockSerializer(many=True)
    status_type = serializers.CharField(source='get_status_display')

    class Meta:
        model = Project
        fields = '__all__'


class UpdateProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        swagger_schema_fields = {
            'example': OrderedDict([('title', 'Change title'), ('is_deleted', False)])}


class UpdateProjectPartBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectPartBlock
        fields = '__all__'
        swagger_schema_fields = {
            'example': OrderedDict([('description', 'Add detail description'), ('is_deleted', False)])}
