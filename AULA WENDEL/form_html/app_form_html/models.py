from django.db import models

class User(models.Model):
    id_Usr = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
