from django.urls import path

from .views import (
    PageListView,
    PageDetailView,
    search_title,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    SignUpView,
    like_view,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("page/<int:pk>", PageDetailView.as_view(), name="pages_detail"),
    path("page/new", PostCreateView.as_view(), name="create_post"),
    path("page/<int:pk>/update", PostUpdateView.as_view(), name="update_post"),
    path("page/<int:pk>/delete", PostDeleteView.as_view(), name="delete_post"),
    path("like/<int:pk>", like_view, name="like_post"),
    path("", PageListView.as_view(), name="home"),
    path("search_title", search_title, name="search_title"),
]
