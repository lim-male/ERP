from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='purchases_index'),
]
