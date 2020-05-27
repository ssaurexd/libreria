from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.models import Token
#
from .serializers import UserSerializer
from .models import User

class UserApiView(CreateAPIView):

	permission_classes = [IsAdminUser]
	serializer_class = UserSerializer
	
	def get_queryset(self):

		name = self.POST.get('name')
		username = self.POST.get('username')
		email = self.POST.get('email')
		password = self.POST.get('password')
		image = self.POST.get('image')
		gender = self.POST.get('gender')
		age = self.POST.get('age')

		queryset = User.objects.create_user(
			username=username,
			email=email,
			password=password,
			extra_fields= {
				image: image,
				gender:gender,
				age: age,
				name: name
			}
		) 
		return queryset

