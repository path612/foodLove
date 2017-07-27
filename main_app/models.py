from django.db import models

# Create your models here.
class Lunch(models.Model):
	submitter = models.CharField(max_length = 100)
	food = models.CharField(max_length =256)

