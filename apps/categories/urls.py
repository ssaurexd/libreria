from django.urls import path
from .views import *

app_name = 'categories_app'
urlpatterns = [
	path(
		'api/list/',
		CategoryListApiView.as_view(),
		name='api-list'
	)
]