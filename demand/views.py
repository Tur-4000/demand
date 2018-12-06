from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CommentForm
from .models import Demand, Comments


def demand_list(request):
    demands = Demand.objects.all()
    return render(request,
                  'demand/demand_list.html',
                  {'demands': demands, 'title': 'Список требований'})


class DemandDetailView(LoginRequiredMixin, DetailView):
    model = Demand
    form_class = CommentForm
    template_name = 'demand/demand_detail.html'
    success_url = reverse_lazy('demand_detail')


def demand_detail(request, pk):
    demand = get_object_or_404(Demand, id=pk)
    comments = Comments.objects.filter(demand=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user:
                comment.user = request.user
                comment.demand = demand
                comment.save()
        return redirect(demand_detail, pk)
    else:
        form = CommentForm()

    return render(request,
                  'demand/demand_detail.html',
                  {'demand': demand, 'form': form, 'comments': comments})


class DemandCreateView(LoginRequiredMixin, CreateView):
    model = Demand
    template_name = 'demand/demand_add.html'
    fields = '__all__'
    success_url = reverse_lazy('demand_list')


class DemandDeleteView(LoginRequiredMixin, DeleteView):
    model = Demand
    template_name = 'demand/demand_del.html'
    success_url = reverse_lazy('demand_list')


class DemandUpdateView(LoginRequiredMixin, UpdateView):
    model = Demand
    template_name = 'demand/demand_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('demand_list')
