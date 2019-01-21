from django.contrib import admin
from resource.models.ui import UI
from django.utils.safestring import mark_safe
from xy2onlineServer.settings import STATIC_URL


class UIAdmin(admin.ModelAdmin):
    list_display = ("__str__","was_hash", "image_data")
    readonly_fields = ("image_data", "was_hash")
    raw_id_fields = ("was", )

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    def was_hash(self, obj):
        return obj.was.hash

    image_data.short_description = u'图片'


admin.site.register(UI, UIAdmin)
