# Generated by Django 2.0.1 on 2019-03-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190304_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='temp_fire',
            field=models.CharField(blank=True, help_text='Для масел при необходимости', max_length=50, verbose_name='Температура вспышки, °C'),
        ),
        migrations.AddField(
            model_name='good',
            name='temp_lose',
            field=models.CharField(blank=True, help_text='Для масел при необходимости', max_length=50, verbose_name='Температура потери текучести, °C'),
        ),
        migrations.AddField(
            model_name='good',
            name='viscosity_100c',
            field=models.CharField(blank=True, help_text='Для масел при необходимости', max_length=50, verbose_name='Вязкость при 100 °C, мм²/с'),
        ),
        migrations.AddField(
            model_name='good',
            name='viscosity_index',
            field=models.CharField(blank=True, help_text='Для масел при необходимости', max_length=50, verbose_name='Индекс вязкости'),
        ),
        migrations.AlterField(
            model_name='good',
            name='tec_category',
            field=models.CharField(blank=True, choices=[('Cleaners', 'Очистители'), ('Antifreeze', 'Антифриз'), ('Antikor', 'Антикор'), ('Brake_fluids', 'Тормозные жидкости')], help_text="Если выбрана категория 'Технические жидкости', то необходимо указать это поле", max_length=40, verbose_name='Категория для технических жидкостей'),
        ),
        migrations.AlterField(
            model_name='good',
            name='type',
            field=models.CharField(blank=True, help_text='Тип масла', max_length=50, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='good',
            name='viscosity',
            field=models.CharField(blank=True, help_text='Пример: 10W-40, 20W-30', max_length=40, verbose_name='Вязкость'),
        ),
        migrations.AlterField(
            model_name='good',
            name='volume',
            field=models.CharField(blank=True, default='1', help_text='Пример: 4л, 150мл, 1.5л', max_length=10, verbose_name='Объем'),
        ),
    ]
