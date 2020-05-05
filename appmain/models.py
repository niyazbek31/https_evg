from django.db import models

# Create your models here.

# Создал модель пиццы. Названия пиццы и цена
class Pizza(models.Model):
    name = models.CharField('Название', max_length=250)
    price = models.FloatField('Цена')

    # В админке названия объекта это названия пиццы
    def __str__(self):
        return self.name
    #  В админке названия таблицы
    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пицца'