from django.contrib import admin
from resource.models.shape import Shape, ShapeAction, ShapePhoto
from django.utils.safestring import mark_safe
from xy2onlineServer.settings import STATIC_URL


class ShapeActionAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'image_data')
    readonly_fields = ('image_data',)
    raw_id_fields = ("was", "shape")

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'


class ShapeActionInline(admin.TabularInline):
    model = ShapeAction
    extra = 1
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'


class ShapePhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'image_data')
    readonly_fields = ('image_data',)
    raw_id_fields = ("was", "shape")

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'


class ShapePhotoInline(admin.TabularInline):
    model = ShapePhoto
    extra = 1
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'


class ShapeAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", 'shape_actions')
    inlines = [ShapeActionInline, ShapePhotoInline]

    readonly_fields = ('shape_actions',)

    def shape_actions(self, obj):
        actions = ShapeAction.objects.filter(shape=obj)
        html = ""
        for action in actions:
            temp = u'<p>%s</p><img src="%s%s"/>' % (action.name, STATIC_URL, action.was.image.url)
            html += temp
        return mark_safe(html)

    shape_actions.short_description = u'文本'


admin.site.register(Shape, ShapeAdmin)
admin.site.register(ShapeAction, ShapeActionAdmin)
admin.site.register(ShapePhoto, ShapePhotoAdmin)