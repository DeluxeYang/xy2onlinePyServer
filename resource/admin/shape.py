from django.contrib import admin
from resource.models.shape import Shape, ShapeAction
from django.utils.safestring import mark_safe
from xy2onlineServer.settings import STATIC_URL


class ShapeActionAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'image_data')
    readonly_fields = ('image_data',)

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


class ShapeAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'shape_actions')
    inlines = [ShapeActionInline]

    readonly_fields = ('shape_actions',)

    def shape_actions(self, obj):
        actions = ShapeAction.objects.filter(shape=obj)
        action_names = ""
        for action in actions:
            action_names += action.name + "; "
        return action_names

    shape_actions.short_description = u'文本'


admin.site.register(Shape, ShapeAdmin)
admin.site.register(ShapeAction, ShapeActionAdmin)