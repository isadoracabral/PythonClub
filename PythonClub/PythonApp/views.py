from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'PythonApp/index.html')

def getresource(request):
    resource_list=Resource.objects.all()
    return render(request, 'PythonApp/resource.html' ,{'resource_list' : resource_list})

def getmeeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'PythonApp/meeting.html', {'meeting_list': meeting_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    return render(request, 'PythonApp/meetingdetails.html') #, {'meet':meet} 