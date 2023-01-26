from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('games/', views.GameList.as_view(), name='game_list'),
    path('about/', views.About.as_view(), name='about'),
    path('games/new', views.GameCreate.as_view(), name="game_create"),
    path('games/<int:pk>/', views.GameDetail.as_view(), name="game_detail")
]
