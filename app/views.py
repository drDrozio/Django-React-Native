from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer

# Create your views here.
class ClassView(View):
	books=Book.objects.all()
	output=''

	for book in books:
		output+=f'{book.title} with ID : {book.id}<br>'

	def get(self,request):
		return HttpResponse(self.output)

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
	serializer_class=BookSerializer
	queryset=Book.objects.all()
