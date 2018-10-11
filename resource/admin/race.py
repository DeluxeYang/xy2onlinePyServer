from django.contrib import admin
from resource.models.race import Race
from resource.admin.faction import FactionInline


class RaceAdmin(admin.ModelAdmin):
    inlines = [FactionInline]


admin.site.register(Race, RaceAdmin)
