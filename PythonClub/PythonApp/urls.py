from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('resource/', views.getresource, name='resource'),
    path('meeting/', views.getmeeting, name='meeting'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
]

