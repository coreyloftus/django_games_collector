from django.contrib import admin

# Register your models here.
# from .models import Game
from .models import *

admin.site.register(Game)
admin.site.register(Character)
