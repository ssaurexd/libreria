from django.db import models

# Create your models here.
class Category(models.Model):

	name = models.CharField(max_length=30, unique=True)
	created = models.DateField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name