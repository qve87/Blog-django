from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Page


class PageListView(ListView):
    model = Page
    template_name = "home.html"


class PageDetailView(DetailView):
    model = Page
    template_name = "pages_detail.html"
