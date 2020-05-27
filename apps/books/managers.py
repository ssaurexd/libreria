from django.db import models

class BookManager(models.Manager):

	def by_category(self, category):
		return self.filter(categories__name__icontains=category)
	
	def by_title(self, title):
		return self.filter(title__icontains=title)