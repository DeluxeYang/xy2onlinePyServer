# Generated by Django 2.1.5 on 2019-05-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20190311_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='version',
            field=models.IntegerField(choices=[(0, 'scene'), (1, 'newscene')]),
        ),
    ]