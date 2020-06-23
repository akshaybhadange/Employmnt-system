from django.db import  models;
from wagtail.core.fields import RichTextField
from datetime import datetime;


class Instructor(models.Model):
    #date ,rating,assigned instructor,

    name = models.CharField(blank=True,max_length=100 )
    college = models.CharField(blank=True,max_length=100 )
    subject = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name