from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.

class DevlogList(ListView):
    queryset = models.Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'main.html'
    paginate_by = 2

class DevlogDetail(DetailView):
    model = models.Post 
    template_name = 'devlog_detail.html'
