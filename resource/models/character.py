from django.db import models
from resource.models.race import Race
from resource.models.wdf import WAS


class Character(models.Model):
    race = models.ForeignKey(Race, related_name='Character', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    name_cn = models.CharField(max_length=30)
    reborn = models.IntegerField(default=0, choices=((0, "未转形象"), (1, "一转形象"), (3, "三转形象")))
    gender = models.IntegerField(choices=((-1, "female"), (1, "male")))
    describe = models.CharField(max_length=300)

    def __str__(self):
        return self.race.name_cn + ": " + self.name_cn


class CharacterAction(models.Model):
    character = models.ForeignKey(Character, related_name='CharacterAction', on_delete=models.CASCADE)
    was = models.ForeignKey(WAS, related_name='CharacterAction', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30, null=True, blank=True)
    weapon = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.character.name_cn + ": " + self.name + "（方向: " + str(self.was.direction_num) + "）"


class CharacterPhoto(models.Model):
    character = models.ForeignKey(Character, related_name='CharacterPhoto', on_delete=models.CASCADE)
    was = models.ForeignKey(WAS, related_name='CharacterPhoto', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30, null=True, blank=True)
    level = models.IntegerField(default=0)
    w = models.IntegerField(default=0)
    h = models.IntegerField(default=0)

    def __str__(self):
        return self.character.name_cn + ": " + self.name
