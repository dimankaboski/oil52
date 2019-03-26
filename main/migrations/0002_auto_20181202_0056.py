# Generated by Django 2.0.1 on 2018-12-01 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Категория')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='cost',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='post',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category', verbose_name='Категория'),
        ),
    ]