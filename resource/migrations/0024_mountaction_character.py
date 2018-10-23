# Generated by Django 2.1.1 on 2018-10-23 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0023_mount_mountaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountaction',
            name='character',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='MountAction', to='resource.Character'),
            preserve_default=False,
        ),
    ]
