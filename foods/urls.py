from django.urls import path
from .views import *
urlpatterns = [
    path('', home_view, name='home'),
    path('menu/', menu_view, name='menu'),
    path('about/', about_view, name='about'),
    path('menu/<int:pk>/', food_detail_view, name='food_detail'),
]