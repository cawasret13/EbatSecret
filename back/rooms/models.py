from django.db import models


class photos(models.Model):
    id_photo = models.IntegerField()
    photo = models.FileField(upload_to='icon/rooms')


class rooms(models.Model):
    id_room = models.CharField(max_length=16)
    id_created = models.CharField(max_length=32)
    id_icon = models.IntegerField()
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    numHum = models.IntegerField()
    max_price = models.IntegerField()
    date = models.DateField(null=True)
    autoRes = models.BooleanField()
    private = models.BooleanField()
    users = models.TextField()
    OK_list = models.TextField()
    play = models.BooleanField(null=True)
    listSant = models.TextField(null=True)
    endPlay = models.BooleanField(null=True)

