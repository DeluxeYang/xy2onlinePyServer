from django.db import models
from resource.models.wdf import WAS
from resource.models.effect import Effect


class Monster(models.Model):
    name = models.CharField(max_length=30, unique=True)
    name_cn = models.CharField(max_length=30)
    type = models.IntegerField(default=0, choices=((0, "普通召唤兽"),(10, "畜牧召唤兽"),(20, "新召唤兽"),(30, "天书召唤兽"),
                                                   (40, "高级守护"),(50, "龙涎丸召唤兽"),(99, "神兽")))
    title_level = models.IntegerField(default=0)  # 称谓
    prototype = models.IntegerField(default=0)  # 原型
    skin_num = models.IntegerField(default=0)  # 皮肤数量

    init_max_hp = models.FloatField(default=0.0)
    init_max_mp = models.FloatField(default=0.0)
    init_max_ap = models.FloatField(default=0.0)
    init_max_sp = models.FloatField(default=0.0)
    init_max_speed = models.FloatField(default=0.0)
    init_max_growth = models.FloatField(default=0.0)
    init_max_high_growth = models.FloatField(default=0.0)

    gold = models.FloatField(default=0.0)
    wood = models.FloatField(default=0.0)
    soil = models.FloatField(default=0.0)
    water = models.FloatField(default=0.0)
    fire = models.FloatField(default=0.0)

    describe = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name_cn


class MonsterAction(models.Model):
    monster = models.ForeignKey(Monster, related_name='MonsterAction', on_delete=models.CASCADE)
    was = models.ForeignKey(WAS, related_name='MonsterAction', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.monster.name_cn + ": " + self.name + "（方向: " + str(self.was.direction_num) + "）"

    def save(self, *args, **kwargs):
        self.was.hooked = True
        self.was.describe = self.monster.name_cn + ": " + self.name
        self.was.save()
        super().save(*args, **kwargs)


class MonsterSkill(models.Model):
    effect = models.ForeignKey(Effect, related_name='MonsterSkill', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    name_cn = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=30)
    level = models.IntegerField(default=1)
    describe = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name_cn + "(" + str(self.level) + ")"


class MonsterAndSkill(models.Model):
    monster = models.ForeignKey(Monster, related_name='MonsterAndSkill', on_delete=models.CASCADE)
    monster_skill = models.ForeignKey(MonsterSkill, related_name='MonsterAndSkill', on_delete=models.CASCADE)

    def __str__(self):
        return self.monster.name_cn + ": " + self.monster_skill.name_cn


class MonsterSkin(models.Model):
    monster = models.ForeignKey(Monster, related_name='MonsterSkin', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    name_cn = models.CharField(max_length=30)
    describe = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.monster.name_cn + ": " + self.name_cn

class MonsterSkinAction(models.Model):
    monster_skin = models.ForeignKey(MonsterSkin, related_name='MonsterSkinAction', on_delete=models.CASCADE)
    was = models.ForeignKey(WAS, related_name='MonsterSkinAction', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.monster_skin) + ": " + self.name + "（方向: " + str(self.was.direction_num) + "）"

    def save(self, *args, **kwargs):
        self.was.hooked = True
        self.was.describe = str(self.monster_skin) + ": " + self.name
        self.was.save()
        super().save(*args, **kwargs)
