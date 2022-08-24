from django.urls import path

from .views import PageListView

urlpatterns = [
    path("", PageListView.as_view(), name="home"),
]
