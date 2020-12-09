from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    path_photo = models.TextField()


class Memory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=225)
    location_latitude = models.DecimalField()
    location_longitude = models.DecimalField()
    comment = models.TextField()
