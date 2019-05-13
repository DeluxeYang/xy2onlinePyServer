from django.db import models
from base.models.map import Map
from resource.models.map_ani import MapAni


# Create your models here.
class Portal(models.Model):
    res = models.ForeignKey(MapAni, related_name='Portal', on_delete=models.CASCADE)

    map = models.ForeignKey(Map, related_name='Portal', on_delete=models.CASCADE)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    target_map = models.ForeignKey(Map, related_name='PrePortal', on_delete=models.CASCADE)
    target_x = models.IntegerField(default=0)
    target_y = models.IntegerField(default=0)

    def __str__(self):
        return str(self.map) + " --> " + str(self.target_map)
