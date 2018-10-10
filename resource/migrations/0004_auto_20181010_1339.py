# Generated by Django 2.1.1 on 2018-10-10 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0003_auto_20181009_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('name_cn', models.CharField(max_length=30)),
                ('nick_name', models.CharField(max_length=30)),
                ('describe', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='faction',
            name='describe',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='faction',
            name='master',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='faction',
            name='nick_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='faction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Skill', to='resource.Faction'),
        ),
    ]
