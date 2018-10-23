from django.db import models
from resource.models.wdf import WAS


class MapAni(models.Model):
    was = models.ForeignKey(WAS, related_name='MapAni', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.was.hooked = True
        self.was.describe = self.name + ": " + self.name_cn
        self.was.save()
        super().save(*args, **kwargs)
