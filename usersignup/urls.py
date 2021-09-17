from django.urls import path
from .import views

urlpatterns = [
    path("register", views.registration, name='registration'),
    path("login",views.loginuser, name='login'),
    path("logout",views.logoutuser,name='logout')

]
