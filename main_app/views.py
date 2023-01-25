from django.shortcuts import render

from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.

from django.http import HttpResponse


class Game:
    def __init__(self, title, genre, publisher, release_date, platform, imageURL):
        self.title = title
        self.genre = genre
        self.publisher = publisher
        self.release_date = release_date
        self.platform = platform
        self.imageURL = imageURL


games = [
    Game(
        "The Legend of Zelda",
        "Action",
        "Nintendo",
        "February 21, 1986",
        "NES",
        "https://www.mobygames.com/images/covers/l/14445-the-legend-of-zelda-nes-front-cover.jpg"
    ),
    Game(
        "Zelda 2: The Adventure of Link",
        "Action",
        "Nintendo",
        "January 17, 1987",
        "NES",
        "https://www.mobygames.com/images/covers/l/14437-zelda-ii-the-adventure-of-link-nes-front-cover.jpg"),
]

class Home(TemplateView):
    template_name= 'home.html'

class About(TemplateView):
    template_name = 'about.html'

class Game_List(TemplateView):
    template_name= 'game_list.html'