from django.urls import path
from .views import UserApiView

app_name = 'users_app'
urlpatterns = [
	path(
		'api/create-user/',
		UserApiView.as_view(),
		name = 'create-user'
	)
]
