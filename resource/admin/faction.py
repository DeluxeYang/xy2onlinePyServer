from django.contrib import admin

from resource.models.faction import Faction
from resource.admin.skill import SkillInline


class FactionInline(admin.TabularInline):
    model = Faction
    extra = 1

class FactionAdmin(admin.ModelAdmin):
    inlines = [SkillInline]


admin.site.register(Faction, FactionAdmin)