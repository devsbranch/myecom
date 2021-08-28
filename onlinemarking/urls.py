from django.urls import path
from . import views



urlpatterns=[

    path('',views.iteamlist,name='items'),
    path('detail/<str:pk>/', views.iteamDetails, name='details'),
    path('create/', views.iteamCreate, name='Create'),
    path('update/<str:pk>', views.iteamUpdate, name='Update'),
    path('delete/<str:pk>', views.iteamdelate, name='Delate'),
    path('catcreate/', views.addcategory, name='add'),
    path('deletecat/<str:pk', views.removecategory, name='deletecat')

]