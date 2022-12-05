from django.db import models


class DBUsers(models.Model):
    token = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    login = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
