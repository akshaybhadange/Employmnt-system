from django.db import  models;
from django.db.models.signals import post_save, pre_save
from django.dispatch.dispatcher import receiver
from django.http import JsonResponse
import django.core.serializers
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.core.signals import page_published


class covid19Country(models.Model):
    intro = models.CharField(blank=True,max_length=100 )
    country = models.CharField(max_length=100,null=False,help_text="Country Name",blank=False ,default="")
    codeName = models.CharField(max_length=100,null=False,editable=False,default="covid19" )
    totalCases = models.IntegerField(blank=True,null=False)
    totalDeath = models.IntegerField(blank=True, null=False)
    totalRecovered = models.IntegerField(blank=True, null=False)

    def __str__(self):
        return self.country

class covid19States(models.Model):
    intro = models.CharField(blank=True,max_length=100 )
    states = models.CharField(max_length=100,null=False,help_text="State Name",blank=False ,default="")
    codeName = models.CharField(max_length=100,null=False,editable=False,default="covid19" )
    totalCases = models.IntegerField(blank=True,null=False)
    totalDeath = models.IntegerField(blank=True, null=False)
    totalRecovered = models.IntegerField(blank=True, null=False)

    def __str__(self):
        return self.states


class covid19Locals(models.Model):
    intro = models.CharField(blank=True,max_length=100 )
    locals = models.CharField(max_length=100,null=False,help_text="Local Name",blank=False ,default="")
    codeName = models.CharField(max_length=100,null=False,editable=False,default="covid19" )
    totalCases = models.IntegerField(blank=True,null=False)
    totalDeath = models.IntegerField(blank=True, null=False)
    totalRecovered = models.IntegerField(blank=True, null=False)

    def __str__(self):
        return self.locals


class covid19MAHA(models.Model):
    intro = models.CharField(blank=True,max_length=100 )
    mahaArea = models.CharField(max_length=100, null=False, help_text="Maha area Name", blank=False, default="")
    codeName = models.CharField(max_length=100,null=False,editable=False,default="covid19" )
    totalCases = models.IntegerField(blank=True,null=False)
    totalDeath = models.IntegerField(blank=True, null=False)
    totalRecovered = models.IntegerField(blank=True, null=False)

    def __str__(self):
        return self.mahaArea




class covid19CountriesApi(Page):

    def serve(self,request):

        data = covid19Country.objects.order_by('-totalCases')

        s = django.core.serializers.serialize('json', data)

        return django.http.HttpResponse(s)


class covid19StatesApi(Page):

    def serve(self, request):
        data = covid19States.objects.order_by('-totalCases')

        s = django.core.serializers.serialize('json', data)

        return django.http.HttpResponse(s)


class covid19LocalsApi(Page):

    def serve(self, request):
        data = covid19Locals.objects.order_by('-totalCases')

        s = django.core.serializers.serialize('json', data)

        return django.http.HttpResponse(s)


class covid19MahaApi(Page):

    def serve(self, request):
        data = covid19MAHA.objects.order_by('-totalCases')

        s = django.core.serializers.serialize('json', data)

        return django.http.HttpResponse(s)



