from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import DefaultUserCreationForm

from .models import Page


class PageListView(ListView):
    model = Page
    template_name = "home.html"


class PageDetailView(DetailView):
    model = Page
    template_name = "pages_detail.html"


class PostCreateView(CreateView):
    model = Page
    template_name = "create_post.html"
    fields = ("title", "author", "body")


class PostUpdateView(UpdateView):
    model = Page
    template_name = "update_post.html"
    fields = ("title", "body")


class PostDeleteView(DeleteView):
    model = Page
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


class SignUpView(CreateView):
    form_class = DefaultUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def search_title(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        titles = Page.objects.filter(title__contains=searched)
        return render(
            request,
            "search_title.html",
            {
                "searched": searched,
                "titles": titles,
            },
        )
    else:
        return render(request, "search_title.html", {})
