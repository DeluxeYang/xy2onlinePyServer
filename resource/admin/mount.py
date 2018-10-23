from django.contrib import admin
from resource.models.mount import Mount, MountAction
from django.utils.safestring import mark_safe
from xy2onlineServer.settings import STATIC_URL


class MountActionAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'image_data')
    readonly_fields = ('image_data',)
    raw_id_fields = ("was",)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'


class MountActionInline(admin.TabularInline):
    model = MountAction
    extra = 1
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'


class MountAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__")
    inlines = [MountActionInline]


admin.site.register(Mount, MountAdmin)
admin.site.register(MountAction, MountActionAdmin)
