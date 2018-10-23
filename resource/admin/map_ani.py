from django.contrib import admin
from resource.models.map_ani import MapAni
from django.utils.safestring import mark_safe
from xy2onlineServer.settings import STATIC_URL


class MapAniAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'image_data')
    readonly_fields = ('image_data',)
    raw_id_fields = ("was", )

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'


admin.site.register(MapAni, MapAniAdmin)
