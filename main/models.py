from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')

    def __str__(self):
        return self.name


class Good(models.Model):
    category = (
        ('Oil', 'Моторное масло'),
        ('transmission', 'Трансмиссия'),
        ('Mototechnic', 'Мототехника'),
        ('Technical', 'Технические жидкости'),
        ('Lubricants', 'Смазки'),
    )
    tec_category = (
        ('Cleaners', 'Очистители'),
        ('Antifreeze', 'Антифриз'),
        ('Antikor', 'Антикор'),
        ('Brake_fluids', 'Тормозные жидкости'),
    )
    name = models.CharField(max_length=200, verbose_name='Наименование')
    cat = models.CharField(max_length=40, choices=category,
                           blank=True, verbose_name='Категория')
    tec_category = models.CharField(max_length=40, choices=tec_category, blank=True, verbose_name='Категория для технических жидкостей',
                                    help_text="Если выбрана категория 'Технические жидкости', то необходимо указать это поле")
    volume = models.CharField(max_length=10, verbose_name='Объем',
                              default='1', blank=True, help_text="Пример: 4л, 150мл, 1.5л")
    viscosity = models.CharField(
        max_length=40, verbose_name='Вязкость', blank=True, help_text="Пример: 10W-40, 20W-30")
    type = models.CharField(
        max_length=50, verbose_name='Тип', blank=True, help_text="Тип масла")
    viscosity_index = models.CharField(
        max_length=50, verbose_name='Индекс вязкости', blank=True, help_text="Для масел при необходимости")
    viscosity_100c = models.CharField(
        max_length=50, verbose_name='Вязкость при 100 °C, мм²/с', blank=True, help_text="Для масел при необходимости")
    temp_lose = models.CharField(
        max_length=50, verbose_name='Температура потери текучести, °C', blank=True, help_text="Для масел при необходимости")
    temp_fire = models.CharField(
        max_length=50, verbose_name='Температура вспышки, °C', blank=True, help_text="Для масел при необходимости")
    description = HTMLField()
    cost = models.IntegerField(
        verbose_name='Цена', default='0')
    img = models.ImageField(
        upload_to='images', verbose_name='Фото', blank=True)

    def __str__(self):
        return self.name


class Orders(models.Model):
    payment = (
        ('On', 'Безналичными'),
        ('Off', 'Наличными'),
    )
    firstname = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=16, verbose_name='Телефонный номер')
    mail = models.CharField(max_length=60, verbose_name='Email')
    adress = models.CharField(max_length=400, verbose_name='Адрес')
    description = models.CharField(
        max_length=1000, verbose_name='Комментарий к заказу')
    payment = models.CharField(max_length=40, choices=payment, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.mail
