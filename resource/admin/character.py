from django.contrib import admin

from resource.models.character import Character
from resource.admin.character_action import CharacterActionInline
from resource.admin.character_photo import CharacterPhotoInline


class CharacterAdmin(admin.ModelAdmin):
    inlines = [CharacterActionInline, CharacterPhotoInline]

admin.site.register(Character, CharacterAdmin)