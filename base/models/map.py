from django.db import models

version_choice = ((0, "scene"), (1, "newscene"))


# Create your models here.
class Map(models.Model):
    version_choice = version_choice
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

    def __str__(self):
        return self.name + "" + self.version_choice[self.version][1] + "/" + self.map_id


def get_version(v):
    for _tuple in version_choice:
        if _tuple[1] == v:
            return _tuple[0]
    return 0
