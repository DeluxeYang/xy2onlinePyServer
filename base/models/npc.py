from django.db import models
from base.models.map import Map
from resource.models.shape import Shape

# Create your models here.
class NPC(models.Model):
    map = models.ForeignKey(Map, related_name='NPC', on_delete=models.CASCADE)
    figure = models.ForeignKey(Shape, related_name='NPC', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
