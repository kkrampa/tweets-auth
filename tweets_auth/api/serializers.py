from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from tweets.models import Tweet


class UserSerializer(serializers.Serializer):

    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField()

    password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)

    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def create(self, validated_data):
        validated_data.pop('repeat_password')
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        if attrs['password'] != attrs['repeat_password']:
            raise ValidationError("Passwords don't match!")
        return attrs


class TweetSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
