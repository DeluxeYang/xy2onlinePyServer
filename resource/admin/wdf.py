from django.contrib import admin
from django.utils.safestring import mark_safe

from resource.models.wdf import *
from xy2onlineServer.settings import STATIC_URL


class WASAdmin(admin.ModelAdmin):
    list_display = ("__str__", "id", "direction_num", "hooked", 'image_data', "describe")
    list_filter = ('hooked', "wdf")
    search_fields = ('hash', 'describe', 'id')
    readonly_fields = ('image_data',)
    list_editable = ("describe",)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.image.url))

    image_data.short_description = u'图片'


admin.site.register(WDF)
admin.site.register(WAS, WASAdmin)
