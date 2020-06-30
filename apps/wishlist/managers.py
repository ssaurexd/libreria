from django.db import models

class WishListManager(models.Manager):
	
	def by_user(self, user):	

		return self.filter(user__username=user)