from django.db import models
from resource.utils.ResManager import save_gif
from xy2onlineServer.settings import STATIC_PATH


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
    describe = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        if self.describe:
            return self.hash + ": " + self.describe
        return self.hash

    def save_with_file(self, *args, **kwargs):
        try:
            sub_path = 'was/'
            file_name, direction_num, frame_num = save_gif(self.wdf.name, self.hash, path=STATIC_PATH + '/' + sub_path)
            self.image = sub_path + file_name
            self.direction_num = direction_num
            self.frame_num = frame_num
            super().save(*args, **kwargs)
            return True
        except Exception as e:
            print(e)
            return False
