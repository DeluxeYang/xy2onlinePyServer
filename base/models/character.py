from django.db import models
from base.models.account import Account
from resource.models.character import Character as CharacterShape


# Create your models here.
class Character(models.Model):
    account = models.ForeignKey(Account, related_name='Character', on_delete=models.CASCADE)
    res = models.ForeignKey(CharacterShape, related_name='Character', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    map_id = models.CharField(max_length=200)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    def __str__(self):
        return self.account.name + self.name

    def save(self, *args, **kwargs):
        self.account.character_num += 1
        self.account.save()
        super().save(*args, **kwargs)