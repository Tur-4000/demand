from django.urls import path
from . import views

urlpatterns = [
    path('', views.demand_list, name='demand_list'),
    path('new/', views.demand_new, name='demand_add'),
    path('delete/<int:demand_id>/', views.demand_delete_mark, name='demand_del'),
    path('edit/<int:pk>', views.demand_edit, name='demand_edit'),
    path('demand_detail/<int:pk>', views.demand_detail, name="demand_detail"),
    path('demand/filter/<str:slug>', views.app_filter, name='app_filter'),
    path('demand_deleted/', views.demand_list_deleted, name='demand_list_deleted'),
    path('app_list', views.app_list, name='app_list'),
    path('app_add', views.app_new, name='app_add'),
    path('app_edit/<int:pk>/', views.app_edit, name='app_edit'),
]
