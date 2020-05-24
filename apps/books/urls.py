from django.urls import path
from .views import BookListApiView, BookDetailApiView, BookByCategoryListApiView

app_name = 'books_app'
urlpatterns = [
	path(
		'api/list/',
		BookListApiView.as_view(),
		name='api-list'
	),
	path(
		'api/detail/<pk>/',
		BookDetailApiView.as_view(),
		name='api-detail'
	),
	path(
		'api/list-by-category/',
		BookByCategoryListApiView.as_view(),
		name='api-list-by-category'
	),
]