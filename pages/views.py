from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
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

    def get_context_data(self, **kwargs):
        certain_page = get_object_or_404(Page, id=self.kwargs["pk"])
        total_likes = certain_page.total_likes()

        liked = False
        if certain_page.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = super(PageDetailView, self).get_context_data(**kwargs)
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = "create_post.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Page
    template_name = "update_post.html"
    fields = ("title", "body")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
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


def like_view(request, pk):
    post = get_object_or_404(Page, id=request.POST.get("page_id"))
    # liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        # liked = False
    else:
        post.likes.add(request.user)
        # liked = True
    return HttpResponseRedirect(reverse("pages_detail", args=[str(pk)]))
