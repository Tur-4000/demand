from django.urls import path
from . import views

urlpatterns = [
    path('', views.demand_list, name='demand_list'),
    path('new/', views.DemandCreateView.as_view(), name='demand_add'),
    path('delete/<int:pk>/', views.DemandDeleteView.as_view(), name='demand_del'),
    path('edit/<int:pk>', views.DemandUpdateView.as_view(), name='demand_edit'),
    path('demand_detail/<int:pk>', views.DemandDetailView.as_view(), name="demand_detail"),
]
