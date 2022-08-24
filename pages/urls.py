from django.urls import path

from .views import PageListView, PageDetailView

urlpatterns = [
    path("page/<int:pk>", PageDetailView.as_view(), name="pages_detail"),
    path("", PageListView.as_view(), name="home"),
]
