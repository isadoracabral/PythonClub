from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create models meeting, meeting minutes, resource and event

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    location=models.CharField(max_length=255)
    agenda=models.CharField(max_length=255)
    
    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'
        
class MeetingMinutes(models.Model):
    #(a foreign key)
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    #(a many to many field with User)
    attendance=models.ManyToManyField(User)
    minutestext=models.CharField(max_length=255)

    def __str__(self):
        return str(self.meetingid)
    
    class Meta:
        db_table='meetingminutes'
        verbose_name_plural='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    url=models.URLField(max_length=255)
    dateentered=models.DateField()
    #(foreign key with User)
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING) 
    description=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    Location=models.CharField(max_length=255)
    Date=models.DateField()
    Time=models.TimeField()
    Description=models.TextField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'



