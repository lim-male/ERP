from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sales_index'),
]
