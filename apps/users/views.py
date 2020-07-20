from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
#
from .serializers import UserSerializer
from .models import User

class UserApiView(CreateAPIView):

	permission_classes = [ IsAdminUser ]
	serializer_class = UserSerializer
	
	