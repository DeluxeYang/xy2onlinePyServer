from django.db import models
from resource.models.race import Race
from resource.models.wdf import WAS
from resource.models.character import Character


class Mount(models.Model):
    race = models.ForeignKey(Race, related_name='Mount', on_delete=models.CASCADE)
    level = models.IntegerField(choices=((1, "一坐"), (2, "二坐"), (3, "三坐"),
                                         (4, "四坐"), (5, "五坐"), (6, "六坐"), (7, "七坐")))
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30, null=True, blank=True)
    describe = models.CharField(max_length=300, null=True, blank=True)

    init_max_mp = models.IntegerField(default=0)
    init_max_ap = models.IntegerField(default=0)
    init_max_hp = models.IntegerField(default=0)

    init_max_mp_reinforce = models.IntegerField(default=0)
    init_max_ap_reinforce = models.IntegerField(default=0)
    init_max_hp_reinforce = models.IntegerField(default=0)

    def __str__(self):
        return self.race.name_cn + ": " + str(self.level) + " " + self.name_cn

class MountAction(models.Model):
    mount = models.ForeignKey(Mount, related_name='MountAction', on_delete=models.CASCADE)
    character = models.ForeignKey(Character, related_name='MountAction', on_delete=models.CASCADE)
    was = models.ForeignKey(WAS, related_name='MountAction', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.mount) + ": " + self.character.name_cn + self.name + "（方向: " + str(self.was.direction_num) + "）"

    def save(self, *args, **kwargs):
        self.was.hooked = True
        self.was.describe = str(self.mount) + ": " + self.name
        self.was.save()
        super().save(*args, **kwargs)
