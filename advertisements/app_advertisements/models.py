from django.db import models


class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=3)
    auction = models.BooleanField('Торг', help_text='Укажите, возможен ли торг')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)




"""
Название
Описание
Цена
Дата создания
Дата обновления
Торг
"""
