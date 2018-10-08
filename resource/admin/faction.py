from django.contrib import admin

from resource.models.character import Faction


class FactionInline(admin.TabularInline):
    model = Faction
    extra = 1


admin.site.register(Faction)