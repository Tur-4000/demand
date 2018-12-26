from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.db.models import Q

from .forms import CommentForm, DemandForm, AppForm
from .models import Demand, Comments, App


def demand_list(request):
    demands = Demand.objects.filter(is_deleted=False)
    return render(request,
                  'demand/demand_list.html',
                  {'demands': demands, 'title': 'Список требований'})


def demand_status_filter(request):
    putaside = 0
    complete = 0
    a_wait = 0
    operating = 0
    if request.GET.get('putaside'):
        putaside = 1
    if request.GET.get('complete'):
        complete = 2
    if request.GET.get('a_wait'):
        a_wait = 3
    if request.GET.get('operating'):
        operating = 4
    demands = Demand.objects.filter(Q(is_deleted=False) &
                                    (Q(status=putaside) |
                                     Q(status=complete) |
                                     Q(status=a_wait) |
                                     Q(status=operating)))
    return render(request,
                  'demand/demand_list.html',
                  {'demands': demands,
                   'title': 'Список требований',
                   'putaside': putaside,
                   'complete': complete,
                   'a_wait': a_wait,
                   'operating': operating})


def demand_list_deleted(request):
    title = 'Список удалённых требований'
    demands = Demand.objects.filter(is_deleted=True)
    return render(request,
                  'demand/demand_list.html',
                  {'demands': demands, 'title': title})


def app_filter(request, slug):
    title = 'Список требований'
    demands = Demand.objects.filter(for_apps__slug=slug, is_deleted=False).all()
    return render(request, 'demand/demand_list.html',
                  {'demands': demands, 'title': title})


class DemandDetailView(LoginRequiredMixin, DetailView):
    model = Demand
    form_class = CommentForm
    template_name = 'demand/demand_detail.html'
    success_url = reverse_lazy('demand_detail')


@login_required
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
        return redirect('demand_detail', pk)
    else:
        form = CommentForm()

    return render(request,
                  'demand/demand_detail.html',
                  {'demand': demand, 'form': form, 'comments': comments})


@login_required
def demand_new(request):
    if request.method == 'POST':
        form = DemandForm(request.POST)
        if form.is_valid():
            demand = form.save(commit=False)
            if request.user:
                demand.user = request.user
                demand.save()
                form.save_m2m()
        else:
            return render(request, 'demand/demand_edit.html', {'form': form})
        return redirect('demand_list')
    else:
        form = DemandForm()
        return render(request, 'demand/demand_add.html', {'form': form})


@login_required
def demand_edit(request, pk):
    if request.method == 'POST':
        demand = get_object_or_404(Demand, id=pk)
        form = DemandForm(request.POST, instance=demand)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
        else:
            return render(request, 'demand/demand_edit.html',
                          {'form': form, 'demand': demand})
        return redirect('demand_detail', pk)
    else:
        demand = get_object_or_404(Demand, id=pk)
        form = DemandForm(instance=demand)
        return render(request, 'demand/demand_edit.html',
                      {'form': form, 'demand': demand})


@login_required
def demand_delete_mark(request, demand_id):
    if request.method == 'POST':
        demand = Demand.objects.get(id=demand_id)
        demand.is_deleted = True
        demand.save()
        return redirect('demand_detail', demand_id)
    demand = get_object_or_404(Demand, id=demand_id)
    return render(request, 'demand/demand_del.html', {'demand': demand})


@login_required
def app_list(request):
    apps = App.objects.all()
    return render(request, 'demand/app_list.html', {'apps': apps})


@login_required
def app_new(request):
    title = 'Добавить приложение'
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'demand/app.html', {'form': form, 'title': title})
        return redirect('app_list')
    else:
        form = AppForm()
        return render(request, 'demand/app.html', {'form': form, 'title': title})


@login_required
def app_edit(request, pk):
    title = 'Редактировать приложение'
    if request.method == 'POST':
        app = get_object_or_404(App, id=pk)
        form = AppForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'demand/app.html', {'form': form, 'title': title})
        return redirect('app_list')
    else:
        app = get_object_or_404(App, id=pk)
        form = AppForm(instance=app)
        return render(request, 'demand/app.html', {'form': form, 'title': title})


# class DemandDeleteView(LoginRequiredMixin, DeleteView):
#     model = Demand
#     template_name = 'demand/demand_del.html'
#     success_url = reverse_lazy('demand_list')
#

# class DemandCreateView(LoginRequiredMixin, CreateView):
#     model = Demand
#     template_name = 'demand/demand_add.html'
#     fields = '__all__'
#     success_url = reverse_lazy('demand_list')
#
#
# class DemandUpdateView(LoginRequiredMixin, UpdateView):
#     model = Demand
#     template_name = 'demand/demand_edit.html'
#     fields = '__all__'
#     success_url = reverse_lazy('demand_list')
