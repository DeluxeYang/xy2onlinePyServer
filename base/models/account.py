from django.db import models


# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=200)
    character_num = models.IntegerField(default=0)

    def __str__(self):
        return self.name