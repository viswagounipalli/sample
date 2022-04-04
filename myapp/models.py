from django.db import models

# Create your models here.
class register(models.Model):
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	email=models.EmailField(max_length=254)
	address=models.TextField(blank=True)
	password=models.CharField(max_length=18)
	def __str__(self):
		return self.firstname+"-"+self.lastname