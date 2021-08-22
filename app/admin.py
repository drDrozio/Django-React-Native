from django.contrib import admin
from .models import Author, Book, BookDetails, Character
# Register your models here.
admin.site.register(Book)

admin.site.register(BookDetails)

admin.site.register(Character)

admin.site.register(Author)
