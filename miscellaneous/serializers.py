from rest_framework import serializers
from .models import Miscellaneous


class MiscellaneousSerializer(serializers.ModelSerializer):
    """
    Serializer for miscellaneous task like terms and condition, privacy policy
    """
    class Meta:
        model = Miscellaneous
        fields = ['title', 'content', 'slug']
