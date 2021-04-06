from django.contrib import admin
from django.urls import path,include
from demo_celery_app import views
urlpatterns = [
    path('',views.index,name='index')
]