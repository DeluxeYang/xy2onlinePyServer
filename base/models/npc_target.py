from django.db import models
from base.models.map import Map
from base.models.npc import NPC


class NPCTarget(models.Model):
    npc = models.ForeignKey(NPC, related_name='NPCTarget', on_delete=models.CASCADE)
    target_map = models.ForeignKey(Map, related_name='NPCTarget', on_delete=models.CASCADE)
    target_x = models.IntegerField(default=0)
    target_y = models.IntegerField(default=0)

    def __str__(self):
        return str(self.target_map)
