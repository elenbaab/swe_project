from django.db import models

# Create your models here.

class Form(models.Model):
    major = models.TextField()
    grad = models.TextField()

    #def __str__(self):
     #   return self.major