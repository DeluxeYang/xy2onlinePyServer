from django.db import models
from resource.models.wdf import WAS

class Effect(models.Model):
    was = models.ForeignKey(WAS, related_name='Effect', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30)

    def __str__(self):
        return self.name
