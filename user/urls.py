from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path("login/", CustomAuthToken.as_view()),
    path("logout/", logout_view),
    path("register/", RegisterView.as_view()),
]
