from django.db import models

# Create your models here.
from mongoengine import *

class Notes(Document):
    note_heading = StringField(max_length=50)
    note = StringField(max_length=500)
    note_time = DateTimeField()
    meta = {'collection': 'notes'}