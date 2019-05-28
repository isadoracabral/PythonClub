from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, EventForm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'PythonApp/meetingdetails.html')

@login_required
def newMeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'PythonApp/newMeeting.html', {'form': form})

@login_required
def newEvent(request):
     form=EventForm
     if request.method=='POST':
          form=EventForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=EventForm()
     else:
          form=EventForm()
     return render(request, 'PythonApp/newEvent.html', {'form': form})

def loginMessage(request):
    return render(request, 'PythonApp/loginmessage.html')

def logoutMessage(request):
    return render(request, 'PythonApp/logoutmessage.html')