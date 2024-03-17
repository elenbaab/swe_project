from django.db import models

# Create your models here.

class Form(models.Model):
    firstname = models.TextField(default='0000000', editable=False)
    lastname = models.TextField(default='0000000', editable=False)
    startyear = models.TextField(default='0000000', editable=False)
    gradyear = models.TextField(default='0000000', editable=False)
    major1 = models.TextField(default='0000000', editable=False)
    major2 = models.TextField(default='0000000', editable=False)
    minor1 = models.TextField(default='0000000', editable=False)
    minor2 = models.TextField(default='0000000', editable=False)