from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

	SEXO_CHOICES = (
		('M', 'Masculino'),
		('F', 'Femenino')
	)
	
	username = models.CharField(max_length=20, unique=True)
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=30, blank=False)
	last_name = models.CharField(max_length=30, blank=False)
	gender = models.CharField(max_length=1, blank=False, choices=SEXO_CHOICES)
	code = models.CharField(blank=True, max_length=6)
	image = models.ImageField(upload_to='users')
	age = models.IntegerField(blank=True, null=True)

	created = models.DateField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True)

	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email',]

	objects = UserManager()

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return self.nombre + ' ' + self.apellidos