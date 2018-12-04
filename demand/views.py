from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Demand


def demand_list(request):
    demands = Demand.objects.all()
    return render(request,
                  'demand/demand_list.html',
                  {'demands': demands, 'title': 'Список требований'})


class DemandDetailView(DetailView):
    model = Demand
    template_name = 'demand/demand_detail.html'


class DemandCreateView(CreateView):
    model = Demand
    template_name = 'demand/demand_add.html'
    fields = '__all__'
    success_url = reverse_lazy('demand_list')


class DemandDeleteView(DeleteView):
    model = Demand
    template_name = 'demand/demand_del.html'
    success_url = reverse_lazy('demand_list')


class DemandUpdateView(UpdateView):
    model = Demand
    template_name = 'demand/demand_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('demand_list')
