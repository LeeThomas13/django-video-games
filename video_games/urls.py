from django.urls import path
from .views import GameListview, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView

urlpatterns = [
    path('', GameListView.as_view(), name='game_list')
    path('detail/', GameDetailView.as_view(), name='game_detail')
]