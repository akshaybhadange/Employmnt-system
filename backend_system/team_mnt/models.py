from django.db import models;
from setuptools._vendor.pyparsing import SkipTo
from wagtail.core.fields import RichTextField
from datetime import datetime;

# this will change during login system

class Team(models.Model):
# date ,rating,assigned instructor,
    team_name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.team_name


class Student(models.Model):
    name = models.CharField(blank=True, max_length=100)
    college = models.CharField(blank=True, max_length=100)
    #many to one
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

