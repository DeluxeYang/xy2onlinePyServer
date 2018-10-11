from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30)

    def __str__(self):
        return self.name_cn