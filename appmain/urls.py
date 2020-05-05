from django.urls import path
from . import views


urlpatterns = [
    path('', views.PizzaView.as_view(), name='index'),
    path('pizza_api/', views.PizzaApi.as_view()),
    path('pizza_api/<int:pk>', views.PizzaApi.as_view()),
]
