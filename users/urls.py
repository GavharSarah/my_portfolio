from django.urls import path, include
from .views import my_profile,teacher_view

urlpatterns = [
    path('',my_profile ,name='my_profile'),
    path('about',teacher_view,name='teacher'),
]