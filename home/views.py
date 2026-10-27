from django.shortcuts import render
from django.views import generic


class HomeTemplateView(generic.TemplateView):
    template_name = "home/home.html"
