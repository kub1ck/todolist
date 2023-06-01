from django.urls import path

from core.views import CreateUserAPIView, LoginAPIView, ProfileAPIView, UpdatePasswordAPIView

urlpatterns = [
    path('signup/', CreateUserAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),
    path('update_password/', UpdatePasswordAPIView.as_view()),
]
