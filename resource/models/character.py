from django.db import models

from resource.models.WDF import WAS


class Race(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Faction(models.Model):
    race = models.ForeignKey(Race, related_name='Faction', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    gender = models.IntegerField(choices=((0, "female"), (1, "male"), (2, "either")))

    def __str__(self):
        if self.gender == 0:
            gender = " (女)"
        elif self.gender == 1:
            gender = " (男)"
        else:
            gender = ""
        return self.race.name + ": " + self.name + gender


class Character(models.Model):
    race = models.ForeignKey(Race, related_name='Character', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    gender = models.IntegerField(choices=((0, "female"), (1, "male")))
    describe = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class CharacterAction(models.Model):
    character = models.ForeignKey(Character, related_name='CharacterAction', on_delete=models.CASCADE)
    was = models.ForeignKey(WAS, related_name='CharacterAction', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    weapon = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name
