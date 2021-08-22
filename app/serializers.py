from rest_framework import serializers
from .models import Author, Book, BookDetails , Character


class BookDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model=BookDetails
		fields=['id','author','publisher']


class CharacterSerializer(serializers.ModelSerializer):
	class Meta:
		model=Character
		fields=['id','name']


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model=Author
		fields=['id','first_name','last_name']


class BookSerializer(serializers.ModelSerializer):
	bookdetails = BookDetailsSerializer(many=False)
	characters = CharacterSerializer(many=True)
	authors = AuthorSerializer(many=True)
	class Meta:
		model=Book
		fields=['id','title','description','price','published','is_published','bookdetails','characters','authors']

class BookMiniSerializer(serializers.ModelSerializer):
	class Meta:
		model=Book
		fields=['id','title']	