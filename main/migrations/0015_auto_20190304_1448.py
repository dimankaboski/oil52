# Generated by Django 2.0.1 on 2019-03-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20190228_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='volume',
            field=models.CharField(blank=True, default='1', max_length=10, verbose_name='Объем'),
        ),
    ]