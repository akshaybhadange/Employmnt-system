from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
class SnippetHighlight(generics.GenericAPIView):

	def get(self,*args, **kwargs):
		return Response()
