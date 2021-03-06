from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.

class MeetingTest(TestCase):
    def test_string(self):
        type=Meeting(meetingtitle='fun meeting')
        self.assertEqual(str(type),type.meetingtitle)
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table),'meeting')

class ResourceTest(TestCase):
    def test_string(self):
        type=Resource(resourcename='FirstResource')
        self.assertEqual(str(type),type.resourcename)
    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table),'resource')

class EventTest(TestCase):
    def test_string(self):
        type=Event(eventtitle='FirstEvent')
        self.assertEqual(str(type),type.eventtitle)
    def test_table(self):
        self.assertEqual(str(Event._meta.db_table),'event')
