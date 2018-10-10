from django.contrib import admin

from resource.models.character import Skill


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


admin.site.register(Skill)