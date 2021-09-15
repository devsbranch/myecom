from django.urls import path
from users.views import Home_page,register

urlpatterns=[
    path("",Home_page, name='Homepage'),
    path("register/",register, name='register'),


]