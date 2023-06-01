from django.urls import path

from core.views import CreateUserAPIView, LoginAPIView, ProfileAPIView, UpdatePasswordAPIView

urlpatterns = [
    path('signup/', CreateUserAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', ProfileAPIView.as_view(), ),
    path('update_password/', UpdatePasswordAPIView.as_view()),
]
