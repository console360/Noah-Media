from rest_framework import serializers

from tutorials.models import Tutorial
from videos.serializers import VideoSerializer


class TutorialSerializer(serializers.ModelSerializer):
    video = VideoSerializer()

    class Meta:
        model = Tutorial
        fields = '__all__'
