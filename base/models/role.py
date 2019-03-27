from django.db import models
from base.models.account import Account
from base.models.map import Map

from resource.models.character import Character
from resource.models.race import Race


# Create your models here.
class Role(models.Model):
    reborn_choices = ((0, "未转"), (1, "一转"), (2, "二转"), (3, "三转"))

    account = models.ForeignKey(Account, related_name='Role', on_delete=models.CASCADE)
    character = models.ForeignKey(Character, related_name='Role', on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    reborn = models.IntegerField(default=0, choices=reborn_choices)

    map = models.ForeignKey(Map, related_name='Role', on_delete=models.CASCADE, default=0)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    def __str__(self):
        return self.account.account + self.name

    def save(self, *args, **kwargs):
        self.account.role_num += 1
        self.account.save()
        super().save(*args, **kwargs)

    def get_data(self):
        return {
            'id': self.id,
            'account': self.account,
            'res': self.character.get_data(),
            'name': self.name,
            'level': self.level,
            'reborn': self.reborn,
            'map': self.map.get_data(),
            'x': self.x,
            'y': self.y
        }
