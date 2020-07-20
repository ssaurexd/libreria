from rest_framework.authtoken.models import Token

def create_token (sender, instance, **kargs):
	
	Token.objects.get_or_create(user = instance)
