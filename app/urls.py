from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('',views.drink_list, name='drink_list'),
    path('drinks/<int:id>/', views.drink_detail, name='drink_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)