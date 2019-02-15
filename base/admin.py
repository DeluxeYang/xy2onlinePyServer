from django.contrib import admin
from base.models.account import Account
from base.models.role import Role
from base.models.map import Map
from base.models.npc import NPC
from base.models.portal import Portal
from base.models.announcement import Announcement

# Register your models here.
admin.site.register(Account)
admin.site.register(Role)
admin.site.register(Map)
admin.site.register(NPC)
admin.site.register(Portal)
admin.site.register(Announcement)