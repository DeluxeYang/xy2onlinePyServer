# Generated by Django 2.1.2 on 2019-02-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0029_ui'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cn', models.CharField(max_length=30)),
            ],
        ),
    ]
