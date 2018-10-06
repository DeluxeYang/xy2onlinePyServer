from django.contrib import admin
from resource.models.WDF import *
from resource.models.character import *


admin.site.register(WDF)
admin.site.register(WAS)
admin.site.register(Race)
admin.site.register(Faction)
admin.site.register(Character)
admin.site.register(CharacterAction)

