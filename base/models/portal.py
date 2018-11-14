from django.db import models
from base.models.map import Map

# Create your models here.
class Portal(models.Model):
    map = models.ForeignKey(Map, related_name='NPC', on_delete=models.CASCADE)
    # TODO res资源如何组织
    name = models.CharField(max_length=200)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
