from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
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


class PageListView(LoginRequiredMixin, ListView):
    model = Page
    template_name = "home.html"


class PageDetailView(LoginRequiredMixin, DetailView):
    model = Page
    template_name = "pages_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = "create_post.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = "update_post.html"
    fields = ("title", "body")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


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
