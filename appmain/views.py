from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.views import generic

from .models import Pizza
from .serializers import PizzaSerializer

# Показывает страницу 'appmain/index.html' и  queryset сохраняется все объекты Pizza
class PizzaView(generic.ListView):
    template_name = 'appmain/index.html'
    queryset = Pizza.objects.all().order_by('name')

# класс api
class PizzaApi(APIView):
    # Функция get, возвращает все объекты Pizza и сериализирует, потом возвращает как json
    def get(self, request):
        pizza = Pizza.objects.all()
        serializer = PizzaSerializer(pizza, many=True)
        return Response({"pizza": serializer.data})
    # Функция post. Через api можно создать новый объект Pizza
    def post(self, request):
        # Берет dict 'pizza' и сериализирует. Создается новый объект Pizza
        pizza = request.data.get("pizza")
        serializer = PizzaSerializer(data=pizza)
        # Если сериализация верна то сохраняет в новую переменную и возвращает success
        if serializer.is_valid(raise_exception=True):
            pizza_saved = serializer.save()
        return Response({"success": "Pizza '{}' created successfully".format(pizza['name'])})

    # Функция put. Через id объекта мы изменяем данные объекта, цену или названию
    def put(self, request, pk):
        saved_pizza = get_object_or_404(Pizza.objects.all(), pk=pk)
        data = request.data.get('pizza')
        serializer = PizzaSerializer(instance=saved_pizza, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            pizza_saved = serializer.save()

        return Response({
            "success": "Pizza '{}' updated successfully".format(pizza_saved['name'])
        })
    # Функция delete, удаляет объект по id
    def delete(self, request, pk):
        # Get object with this pk
        pizza = get_object_or_404(Pizza.objects.all(), pk=pk)

        pizza.delete()
        return Response({
            "message": "Pizza with id `{}` has been deleted.".format(pk)
        }, status=204)
