from rest_framework import status, generics, response, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import MyTokenObtainPairSerializer, UserRegistrSerializer, TaskDetailSerializer, TaskCreateSerializer, TaskListSerializer
from .permisisions import IsOwnerOrReadOnly
from .models import Tasks
from rest_framework_simplejwt.views import TokenObtainPairView


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response_my = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully'
        }

        return response.Response(response_my, status=status_code)


class MyObtainTokenPairView(TokenObtainPairView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class TaskCreateView(generics.CreateAPIView):

    serializer_class = TaskCreateSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class TaskListView(generics.ListAPIView):

    serializer_class = TaskListSerializer
    authentication_classes = (JWTAuthentication,)
    queryset = Tasks.objects.all()


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TaskDetailSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Tasks.objects.all()


class TaskPrivatListView(generics.ListAPIView):

    serializer_class = TaskListSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        queryset = Tasks.objects.filter(owner=self.request.user)
        return queryset

