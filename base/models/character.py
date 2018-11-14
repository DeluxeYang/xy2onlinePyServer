from django.db import models
from base.models.account import Account
from resource.models.character import Character as CharacterShape


# Create your models here.
class Character(models.Model):
    account = models.ForeignKey(Account, related_name='Character', on_delete=models.CASCADE)
    figure = models.ForeignKey(CharacterShape, related_name='Character', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)