from rest_framework import serializers

from templates.models import Template, TemplatePart


class TemplatePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplatePart
        fields = '__all__'


class TemplateSerializer(serializers.ModelSerializer):
    parts = TemplatePartSerializer(many=True)

    class Meta:
        model = Template
        fields = '__all__'
