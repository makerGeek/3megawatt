from django.shortcuts import render, redirect
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


class SummaryAverage(View):
    def get(self, request, *args, **kwargs):
        sites = Site.objects.all()
        averages = []
        for site in sites:
            a_sum = 0
            b_sum = 0
            operations = site.operation_set.all()
            for operation in operations:
                a_sum+=operation.a_value
                b_sum+=operation.b_value
            try:
                a_avg = a_sum/len(operations)
                b_avg = b_sum/len(operations)
                averages.append({'a_avg':a_avg, 'b_avg':b_avg, 'name':site.name})
            except Exception as e:
                print(e)
                pass
        return render(request, 'sites/summary-average.html', {'averages': averages})