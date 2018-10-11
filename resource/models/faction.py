from django.db import models
from resource.models.race import Race


class Faction(models.Model):
    race = models.ForeignKey(Race, related_name='Faction', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    gender = models.IntegerField(choices=((-1, "female"), (1, "male"), (0, "either")))
    name_cn = models.CharField(max_length=30)
    master = models.CharField(max_length=30, null=True, blank=True)
    nick_name = models.CharField(max_length=30, null=True, blank=True)
    describe = models.CharField(max_length=200, null=True, blank=True)
    feature = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.gender == -1:
            gender = " (女)"
        elif self.gender == 1:
            gender = " (男)"
        else:
            gender = ""
        return self.race.name_cn + ": " + self.name_cn + gender


class Skill(models.Model):
    faction = models.ForeignKey(Faction, related_name='Skill', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    name_cn = models.CharField(max_length=30)
    level = models.IntegerField(default=1)
    nick_name = models.CharField(max_length=30)
    describe = models.CharField(max_length=200)

    def __str__(self):
        return self.name_cn
