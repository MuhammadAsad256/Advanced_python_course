from django.urls import path
from . import views


urlpatterns = [
    path('calculate_total', views.calculate_total, name='name'),
    path('calculate_average', views.calculate_average, name='name'),
    path('calculate_product', views.calculate_product, name='name'),
]