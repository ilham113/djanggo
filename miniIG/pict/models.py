from django.contrib.auth.models import User
from django.db import models

class Pict(models.Model):
	name = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
	picture = models.ImageField()
	describe = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.describe