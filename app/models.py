from django.db import models
from django.db.models.base import Model

# Create your models here.
class BookDetails(models.Model):
	author = models.CharField(max_length=50, blank=True)
	publisher = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return '%s' % (self.author)


class Book(models.Model):
	title=models.CharField(max_length=36, blank=False, unique=True)
	description=models.TextField(max_length=256, blank=True)
	price=models.DecimalField(default=0, max_digits=3, decimal_places=2)
	published=models.DateField(blank=True, null=True, default=None)
	is_published=models.BooleanField(default=False)
	cover=models.ImageField(upload_to='uploads/', blank=True)
	bookdetails = models.OneToOneField(BookDetails, on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % (self.title)


class Character(models.Model):
	name = models.CharField(max_length=50)
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

	def __str__(self):
		return '%s' % (self.name)

class Author(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	books = models.ManyToManyField(Book, related_name='authors')

	def __str__(self):
		return '%s' % (self.last_name+" "+self.first_name)