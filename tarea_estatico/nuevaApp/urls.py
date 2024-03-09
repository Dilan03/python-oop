from django.urls import path
from nuevaApp import views 

urlpatterns = [
    path('',views.index, name='index'),
]