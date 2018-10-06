from django.db import models
from resource.utils.ResManager import res_manager, WAS as was


class WDF(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class WAS(models.Model):
    wdf = models.ForeignKey(WDF, related_name='WAS', on_delete=models.CASCADE)
    hash = models.CharField(max_length=30)
    direction_num = models.IntegerField(default=1)
    frame_num = models.IntegerField(default=1)
    hooked = models.BooleanField(default=False)
    describe = models.CharField(max_length=100)

    def __str__(self):
        if self.describe != "":
            return self.hash + ": " + self.describe
        return self.hash

    def show(self):
        res = res_manager.get_res(self.wdf.name, self.hash)
