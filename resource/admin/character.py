from django.contrib import admin

from resource.models.character import Character
from resource.admin.character_action import CharacterActionInline
from django.utils.safestring import mark_safe
from xy2onlineServer.settings import STATIC_URL


class CharacterAdmin(admin.ModelAdmin):
    inlines = [CharacterActionInline]


admin.site.register(Character, CharacterAdmin)