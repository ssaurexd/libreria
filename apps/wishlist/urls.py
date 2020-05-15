from django.urls import path
from .views import WishListListApiView

app_name = 'wishlist_app'
urlpatterns = [
	path(
		'api/list/',
		WishListListApiView.as_view(),
		name='api-list'
	)
]	