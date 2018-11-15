from django.db import models
from base.models.map import Map
from resource.models.map_ani import MapAni

# Create your models here.
class Portal(models.Model):
    map = models.ForeignKey(Map, related_name='Portal', on_delete=models.CASCADE)
    res = models.ForeignKey(MapAni, related_name='Portal', on_delete=models.CASCADE)

    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    target_map_id = models.CharField(max_length=200)
    target_x = models.IntegerField(default=0)
    target_y = models.IntegerField(default=0)