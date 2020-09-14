from rest_framework import serializers
from .models import User
from collections import OrderedDict


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserSignUpSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.EmailField(allow_blank=False, allow_null=False)
    name = serializers.CharField(allow_blank=False)
    password = serializers.CharField(max_length=128, allow_blank=False, allow_null=False)

    class Meta:
        swagger_schema_fields = {
            'example': OrderedDict([('email', 'albert@gmail.com'), ('name', 'Albert'), ('password', 'Qwerty@1')])}


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login request data
    """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.EmailField(allow_blank=False, allow_null=False)
    password = serializers.CharField(max_length=128, allow_blank=False, allow_null=False)
    
    class Meta:
        swagger_schema_fields = {
            'example': OrderedDict([('email', 'albert@gmailcom'),('password', 'Qwerty@1')])}


class UserProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    is_deleted = serializers.BooleanField()
    password = serializers.CharField(max_length=128)
    current_password = serializers.CharField(max_length=128, allow_blank=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.is_system_generated_password = validated_data.get('is_system_generated_password', instance.is_system_generated_password)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance

    def create(self, validated_data):
        pass

    class Meta:
        swagger_schema_fields = {
            'example': OrderedDict([('name', 'Mike'), ('password', 'Qwerty@2')])}


class UserForgetPassword(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.EmailField(allow_blank=False, allow_null=False)

    class Meta:
        swagger_schema_fields = {
            'example': OrderedDict([('email', 'albert@gmail')])}
