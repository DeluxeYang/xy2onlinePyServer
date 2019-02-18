from django.db import models
from base.models.account import Account
from resource.models.character import Character


# Create your models here.
class Role(models.Model):
    account = models.ForeignKey(Account, related_name='Character', on_delete=models.CASCADE)
    res = models.ForeignKey(Character, related_name='Character', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    map_id = models.CharField(max_length=200)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    def __str__(self):
        return self.account.account + self.name

    def save(self, *args, **kwargs):
        self.account.character_num += 1
        self.account.save()
        super().save(*args, **kwargs)

    def get_role_data(self):
        return {
            'account': self.account,
            'res': self.res.get_data()
        }
