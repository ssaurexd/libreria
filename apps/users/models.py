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
	nombre = models.CharField(max_length=30, blank=True)
	apellidos = models.CharField(max_length=30, blank=True)
	genero = models.CharField(max_length=1, blank=True, choices=SEXO_CHOICES)
	codregistro = models.CharField(blank=True, max_length=6)
	image = models.ImageField(upload_to='users')
	edad = models.IntegerField(max_length=3)

	created = models.DateField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now=True)

	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email',]

	objects = UserManager()

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return self.nombre + ' ' + self.apellidos