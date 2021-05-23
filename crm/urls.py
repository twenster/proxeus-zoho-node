from django.urls import path
from . import views

# Proxeus mandatory URLs
urlpatterns = [
    path("health", views.health, name="health"),
    path("next", views.next, name="next"),
    path("config", views.config, name="config"),
    path("remove", views.remove, name="remove"),
    path("close", views.close, name="close"),
]