from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'PythonApp/index.html')

def getresource(request):
    resource_list=Resource.objects.all()
    return render(request, 'PythonApp/resource.html' ,{'resource_list' : resource_list})