from django.contrib import admin

from .models import Pizza
# Register your models here.
# Зарегистрировал модель Pizza чтоб появилась в админке
admin.site.register(Pizza)