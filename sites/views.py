from django.shortcuts import render
from.models import Site
# Create your views here.
from django.views.generic import ListView


class SitesList(ListView):
    template_name = 'sites/sites_list.html'
    model = Site