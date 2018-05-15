from django.shortcuts import render
from django.views import View
from django.db.models import Sum

from.models import Site, Operation
# Create your views here.
from django.views.generic import ListView


class SitesList(ListView):
    template_name = 'sites/sites_list.html'
    model = Site

class OperationsList(ListView):
    template_name = 'sites/operations_list.html'
    model = Operation

    def get_queryset(self):
        site_id = self.kwargs['site_id']
        return Operation.objects.filter(site_id=site_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_id = self.kwargs['site_id']
        context['site_name'] = Site.objects.filter(id=site_id).first().name
        return context

class Summary(ListView):
    template_name = 'sites/summary.html'

    def get_queryset(self):
        return Site.objects.values('id','name').annotate(a_sum=Sum('operation__a_value'),b_sum=Sum('operation__b_value'))

