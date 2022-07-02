from django.contrib import admin
from .models import *

sits = [SpotifyModel, PaypalModel, WordPressModel,
        TiktokModel, 
        ]

for i in sits:
    admin.site.register(i)
