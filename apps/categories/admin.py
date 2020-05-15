from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	'''Admin View for '''

	list_display = (
		'id',
		'name',
		'created',
		'updated',	
	)

admin.site.register(Category, CategoryAdmin)