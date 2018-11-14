from django.db import models


# Create your models here.
class Map(models.Model):
    map_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    version = models.IntegerField(default=0)
