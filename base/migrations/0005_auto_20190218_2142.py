# Generated by Django 2.1.2 on 2019-02-18 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0029_ui'),
        ('base', '0004_auto_20190124_1258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Character',
            new_name='Role',
        ),
    ]
