from django.urls import path
from .views import UserRegistrationView, MyObtainTokenPairView, TaskListView, TaskPrivatListView, TaskCreateView, TaskDetailView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('task/all/', TaskListView.as_view()),
    path('task/my/', TaskPrivatListView.as_view()),
    path('task/create/', TaskCreateView.as_view()),
    path('task/detail/<int:pk>/', TaskDetailView.as_view()),
    path('registr/', UserRegistrationView.as_view()),
    path('login/', MyObtainTokenPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]