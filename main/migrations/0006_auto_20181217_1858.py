# Generated by Django 2.0.1 on 2018-12-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181213_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='viscosity',
            field=models.CharField(default='10W-40', max_length=40, verbose_name='Вязкость'),
        ),
        migrations.AlterField(
            model_name='good',
            name='type',
            field=models.CharField(default='Синтетическое', max_length=50, verbose_name='Тип'),
        ),
    ]
