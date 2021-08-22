from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookMiniSerializer, BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class ClassView(View):
	def get(self,request):
		books=Book.objects.all()
		output=''

		for book in books:
			output+=f'{book.title} with ID : {book.id}<br>'
		return HttpResponse(output)

def testFunction(request):
	return HttpResponse('Hello World!')

def first(request):
	books=Book.objects.all()
	book_names=[]
	for book in books:
		book_names.append(book.title)
	return render(request,'index.html',{'data':'Books Available',
		'book_names': book_names
		})

class BookViewSet(viewsets.ModelViewSet):
	serializer_class=BookMiniSerializer
	queryset=Book.objects.all()
	authentication_classes=(TokenAuthentication,)
	permission_classes=(IsAuthenticated,)

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = BookSerializer(instance)
		return Response(serializer.data)
