from django.db import  models;
from wagtail.core.fields import RichTextField
from datetime import datetime;


class Project(models.Model):
    #date ,rating,assigned instructor,

    intro = models.CharField(blank=True,max_length=100 )
    Summary = RichTextField()
    Project_Lead = models.CharField(max_length=100,null=False,editable=True,default="Nagindra" )
    Project_status = models.BooleanField(default=False)
    rating_proj = models.FloatField(default=5.0)


    def __str__(self):
        return self.intro

class Tasks(models.Model):
    title = models.CharField(blank=True,max_length=100 )
    Summary = RichTextField()
    due_date = models.DateField(default=datetime.now, blank=True)
    #many to one
    select_project = models.ForeignKey(Project ,on_delete=models.CASCADE,help_text="Select Your Project")




    def __str__(self):
        return self.title