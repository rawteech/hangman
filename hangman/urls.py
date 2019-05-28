from django.urls import path
from . import views

urlpatterns = [
    path('game/<int:game_id>', views.GameView.as_view(), name="game_detail"),
    path('game', views.GameView.as_view(), name="game"),
    path('', views.HomeView.as_view(), name="home")
]
