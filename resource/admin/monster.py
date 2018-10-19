from django.contrib import admin
from resource.models.monster import Monster, MonsterAction, MonsterSkill, MonsterAndSkill, MonsterSkin, MonsterSkinAction
from django.utils.safestring import mark_safe
from xy2onlineServer.settings import STATIC_URL

class MonsterActionInline(admin.TabularInline):
    model = MonsterAction
    extra = 1
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'

class MonsterAndSkillInline(admin.TabularInline):
    model = MonsterAndSkill
    extra = 1

class MonsterAdmin(admin.ModelAdmin):
    list_display = ("__str__", "id", "type", "title_level", "init_max_hp", "init_max_mp", "init_max_ap",
                    "init_max_sp", "init_max_speed", "init_max_growth")
    inlines = [MonsterActionInline, MonsterAndSkillInline]

class MonsterSkinActionInline(admin.TabularInline):
    model = MonsterSkinAction
    extra = 1
    readonly_fields = ('image_data',)

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'

class MonsterSkinAdmin(admin.ModelAdmin):
    list_display = ("__str__", "id")
    inlines = [MonsterSkinActionInline]

class MonsterSkinActionAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'image_data')
    readonly_fields = ('image_data',)
    raw_id_fields = ("was", "monster_skin")

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'

class MonsterActionAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'image_data')
    readonly_fields = ('image_data',)
    raw_id_fields = ("was", "monster")

    def image_data(self, obj):
        return mark_safe(u'<img src="%s%s"/>' % (STATIC_URL, obj.was.image.url))

    image_data.short_description = u'图片'

admin.site.register(Monster, MonsterAdmin)
admin.site.register(MonsterAction, MonsterActionAdmin)
admin.site.register(MonsterSkill)
admin.site.register(MonsterAndSkill)
admin.site.register(MonsterSkin, MonsterSkinAdmin)
admin.site.register(MonsterSkinAction, MonsterSkinActionAdmin)
