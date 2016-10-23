from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Client(models.Model):
	nombres = models.CharField(max_length = 50 )
	apellidos = models.CharField(max_length = 50 )
	direccion = models.CharField(max_length = 140)
	telefono = models.DecimalField(max_digits = 6, decimal_places = 2)
	email = models.EmailField(max_length = 254)
	phone = models.IntegerField(unique = True)
	address = models.CharField(max_length = 100)


	def __str__(self):
		return self.nombres

