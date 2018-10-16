from django.contrib import admin
from resource.models.symbolic_animals import SymbolicAnimal, SymbolicAnimalAction
from django.utils.safestring import mark_safe
from xy2onlineServer.settings import STATIC_URL


class SymbolicAnimalActionAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'image_data')
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'


class SymbolicAnimalActionInline(admin.TabularInline):
    model = SymbolicAnimalAction
    extra = 1
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'


class SymbolicAnimalAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'shape_actions')
    inlines = [SymbolicAnimalActionInline]

    readonly_fields = ('shape_actions',)

    def shape_actions(self, obj):
        actions = SymbolicAnimalAction.objects.filter(shape=obj)
        action_names = ""
        for action in actions:
            action_names += action.name + "; "
        return action_names

    shape_actions.short_description = u'文本'


admin.site.register(SymbolicAnimal, SymbolicAnimalAdmin)
admin.site.register(SymbolicAnimalAction, SymbolicAnimalActionAdmin)
