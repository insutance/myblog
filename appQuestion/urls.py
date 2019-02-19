from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.question, name= 'question'),
    path('<int:question_id>', views.read_question, name= 'read_question'),
    path('write_question', views.write_question, name='write_question'),
    path('create', views.create, name = 'create'),
]