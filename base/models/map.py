from django.db import models


# Create your models here.
class Map(models.Model):
    version_choice = ((0, "scene"), (1, "newscene"))
    map_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    version = models.IntegerField(choices=version_choice)

    def get_data(self):
        return {
            'id': self.id,
            'map_id': self.map_id,
            'name': self.name,
            'version': self.version_choice[self.version][1]
        }
