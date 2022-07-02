from django.urls import path
from . import views

urlpatterns = [
    path("spotify/", views.SpotifyView.as_view(),name="spotify"),
    path("paypal/", views.PaypalView.as_view(),name="paypal"),
    path("wordpress/", views.WordPressView.as_view(),name="wordpress"),
    path("tiktok/", views.TiktokView.as_view(),name="tiktok"),
]
