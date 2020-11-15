from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("history/", views.history, name="history"),
]
