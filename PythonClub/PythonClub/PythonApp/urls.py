from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('resource/', views.getresource, name='resource'),
    path('meeting/', views.getmeeting, name='meeting'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('newMeeting/', views.newMeeting, name='newMeeting'),
    path('newEvent/', views.newEvent, name='newEvent'),
    path('loginmessage/', views.loginMessage, name='loginmessage'),
    path('logoutmessage/', views.logoutMessage, name='logoutmessage'),
]

