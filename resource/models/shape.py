from django.db import models
from resource.models.wdf import WAS


class Shape(models.Model):
    name = models.CharField(max_length=30, unique=True)
    name_cn = models.CharField(max_length=30)
    describe = models.CharField(max_length=300)

    def __str__(self):
        return self.name_cn


class ShapeAction(models.Model):
    shape = models.ForeignKey(Shape, related_name='ShapeAction', on_delete=models.CASCADE)
    was = models.ForeignKey(WAS, related_name='ShapeAction', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    name_cn = models.CharField(max_length=30)

    def __str__(self):
        return self.shape.name_cn + self.name