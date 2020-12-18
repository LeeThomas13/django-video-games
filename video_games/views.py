from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import VideoGame

class GameListView(ListView):
    template_name = 'video_games/games-list.html'
    model = VideoGame

class GameCreateView(CreateView):
    template_name = 'video_games/games-create.html'
    model = VideoGame

class GameDetailView(DetailView):
    template_name = 'video_games/games-detail.html'
    model = VideoGame

class GameUpdateView(UpdateView):
    template_name = 'video_games/games-update.html'
    model = VideoGame
    fields = ['name', 'description']

class GameDeleteView(DeleteView):
    template_name = 'video_games/games-delete.html'
    model = VideoGame

