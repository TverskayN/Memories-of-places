import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    """
    Имя и фотография пользователя подтягиваются из facebook.
    """
    name = models.CharField(max_length=255)
    path_photo = models.TextField()

    def __str__(self):
        return self.name


class Memory(models.Model):
    """
    Воспомининие пользователя включает название, координаты места
    (location_latitude - широта, location_longitude - долгота),
    коментарий и дату публикации.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=225)
    location_latitude = models.DecimalField(decimal_places=3, max_digits=8)
    location_longitude = models.DecimalField(decimal_places=3, max_digits=8)
    comment = models.TextField()
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.location_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
