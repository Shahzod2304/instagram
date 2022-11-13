from django.shortcuts import render
from .models import Data
from django.views.generic import TemplateView, CreateView
# Create your views here.
class HomePage(CreateView):
    model = Data
    template_name = "index.html"
    fields = "__all__"

class Add(TemplateView):
    template_name = "add.html"
