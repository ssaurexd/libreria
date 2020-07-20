#
from rest_framework import serializers
#
from .models import User

class UserSerializer(serializers.ModelSerializer):

	password = serializers.CharField(write_only=True)
	
	def create(self, validated_data):
		
		user = User.objects.create_user(
			username = validated_data['username'],
			email = validated_data['email'],
			name = validated_data['name'],
			last_name = validated_data['last_name'],
			age = validated_data['age'],
			gender = validated_data['gender']	
		)
		user.set_password(validated_data['password'])
		user.save()

		return user

	class Meta: 
		model = User
		fields = (
			'username',
			'email',
			'password',
			'name',
			'last_name',
			'age',
			'gender'
		)
