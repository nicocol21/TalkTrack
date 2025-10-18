from django.urls import path
from . import views

urlpatterns = [
    # Index / Login
    path('', views.login_view, name='login'),
    path('index/', views.login_view, name='index'),
    # Registro y recuperación
    path('crear/', views.crear_view, name='crear'),
    path('olvide/', views.olvide_view, name='olvide'),
    # Página de bienvenida después del login
    path('bienvenido/', views.bienvenido_view, name='bienvenido'),
]
