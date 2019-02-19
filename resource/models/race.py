from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30)

    def __str__(self):
        return self.name_cn

    def get_data(self, gender):
        from .faction import Faction
        factions = Faction.objects.filter(race=self, gender__in=[0, gender])
        return_dict = {
            'id': self.id,
            'name_cn': self.name_cn,
            'factions': {}
        }
        for f in factions:
            return_dict['factions'][f.name] = f.get_data()
        return return_dict
