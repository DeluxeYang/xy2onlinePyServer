# Generated by Django 2.1.1 on 2018-10-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0021_mapani'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactermount',
            name='level',
            field=models.IntegerField(choices=[(1, '一坐'), (2, '二坐'), (3, '三坐'), (4, '四坐'), (5, '五坐'), (6, '六坐')], default=0),
            preserve_default=False,
        ),
    ]
