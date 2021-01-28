from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here

'''
AbstractUser est le model cree automatiquement par Django et qui est utilisé pour authentifier les utilisateurs, par defaut utilisé pour authentifier
les utilisateurs dans la page admin.
Ici on cree le model Person qui herite de ce model, et ainsi ajouter nos propres champs et fonctionalités "eg. phone_number et ville"
Pour que notre projet django utilise la classe Person par defaut il faut ajouter un champ a settings.py qui specifie le model Person comme model 
d'authentification.
'''

class Person(AbstractUser):
    phone_number = models.CharField(max_length=50, null=True)
    ville = models.CharField(max_length=100, null=True)

