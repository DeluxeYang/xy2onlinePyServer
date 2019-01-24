from django.db import models
import datetime


# Create your models here.
class Account(models.Model):
    account = models.CharField(max_length=200)
    character_num = models.IntegerField(default=0)
    create_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.account

    def save(self, *args, **kwargs):
        if not self.create_time:
            self.create_time = datetime.datetime.now()
        super().save(*args, **kwargs)

