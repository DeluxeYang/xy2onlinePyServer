from django.db import models


class Weapon(models.Model):
    name_cn = models.CharField(max_length=30)

    def __str__(self):
        return self.name_cn
