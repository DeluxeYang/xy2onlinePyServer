from django.db import models
from base.models.map import Map
from resource.models.shape import Shape


# Create your models here.
class NPC(models.Model):
    type_choices = ((0, "其他"), (1, "传送"))

    map = models.ForeignKey(Map, related_name='NPC', on_delete=models.CASCADE)
    res = models.ForeignKey(Shape, related_name='NPC', on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    direction = models.IntegerField(default=0)

    npc_type = models.IntegerField(default=0, choices=type_choices)

    def __str__(self):
        return self.name + "(" + str(self.map) + ", " + str(self.x) + ", " + str(self.y) + ")"
