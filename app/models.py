from django.db import models


class Users(models.Model):
    id = models.AutoField('user_id', primary_key=True)
    email = models.EmailField('email', max_length=100, null=False, unique=True)
    username = models.CharField(max_length=32, null=False)
    password = models.CharField(max_length=32, null=False)
    age = models.IntegerField(null=False)

