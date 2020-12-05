from django.db import models
from django.forms.widgets import PasswordInput



# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=34)
