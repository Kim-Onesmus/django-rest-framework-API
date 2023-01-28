from django.urls import path
from . import views

urlpatterns = [
    path('',views.drink_list, name='drink_list'),
    path('drinks/<int:id>/', views.drink_detail, name='drink_detail'),
]