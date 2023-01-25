from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('games/', views.Game_List.as_view(), name='games_list'),
    path('about/', views.About.as_view(), name='about')
]
