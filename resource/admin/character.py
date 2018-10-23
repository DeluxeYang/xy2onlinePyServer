from django.contrib import admin

from resource.models.character import Character
from resource.admin.character_action import CharacterActionInline


class CharacterAdmin(admin.ModelAdmin):
    inlines = [CharacterActionInline]

admin.site.register(Character, CharacterAdmin)