from rest_framework import serializers
from .models import User, Tasks
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegistrSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['email'] = user.email

        return token


class TaskCreateSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tasks
        fields = ['id_workers', 'title', 'description', 'completion_date', 'owner']


class TaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ['id', 'id_workers', 'title', 'description', 'completion_date']


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ['id', 'id_workers', 'title', 'description', 'completion_date', 'owner']
