from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class ClassView(View):
	def get(self,request):
		return HttpResponse('This is a class view')

def testFunction(request):
	return HttpResponse('Hello World!')
