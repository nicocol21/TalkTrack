from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('bienvenido/', views.bienvenido_view, name='bienvenido'),
]
