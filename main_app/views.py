from django.shortcuts import render
from django.http import HttpResponse

from .models import Game

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

# class Game:
#     def __init__(self, title, genre, publisher, release_date, platform, imageURL):
#         self.title = title
#         self.genre = genre
#         self.publisher = publisher
#         self.release_date = release_date
#         self.platform = platform
#         self.imageURL = imageURL


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class GameList(TemplateView):
    template_name = 'game_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context['games'] = Game.objects.filter(title__icontains=title)
            context['header'] = f'Searching for {title}'
        else:
            context['games'] = Game.objects.all()
            context['header'] = "Game Collection Index"
        return context


class GameCreate(CreateView):
    model = Game
    fields = ['title', 'genre', 'publisher',
              'release_date', 'platform', 'imageURL', 'favorite']
    template_name = 'game_create.html'
    success_url = '/games/'


class GameDetail(TemplateView):
    model = Game
    template_name = 'game_detail.html'


class GameUpdate(UpdateView):
    model = Game
    fields = ['title', 'genre', 'publisher',
              'release_date', 'platform', 'imageURL', 'favorite']
    template_name = 'game_update.html'
    success_url = '/games/'


class GameDelete(DeleteView):
    model = Game
    template_name = "game_delete_confirmation.html"
    success_url = "/games/"
