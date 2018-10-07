from django.contrib import admin
from resource.models.WDF import *
from resource.models.character import *


class WASAdmin(admin.ModelAdmin):
    list_display = ("__str__", "preview")

    def preview(self, obj):

        return u'<img src="%s" height="64" width="64" />' % obj.image

    preview.allow_tags = True

    preview.short_description = "图片"


admin.site.register(WDF)
admin.site.register(WAS, WASAdmin)
admin.site.register(Race)
admin.site.register(Faction)
admin.site.register(Character)
admin.site.register(CharacterAction)

