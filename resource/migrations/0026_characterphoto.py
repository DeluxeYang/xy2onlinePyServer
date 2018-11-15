# Generated by Django 2.1.2 on 2018-10-26 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0025_auto_20181023_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('name_cn', models.CharField(blank=True, max_length=30, null=True)),
                ('level', models.IntegerField(default=0)),
                ('w', models.IntegerField(default=0)),
                ('h', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CharacterPhoto', to='resource.Character')),
                ('was', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CharacterPhoto', to='resource.WAS')),
            ],
        ),
    ]