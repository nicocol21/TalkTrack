from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UsuarioViewSet

# API
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    # --- API ---
    path('api/', include(router.urls)),

    # --- Páginas web ---
    path('', views.login_view, name='login'),
    path('index/', views.login_view, name='index'),
    path('crear/', views.crear_view, name='crear'),
    path('olvide/', views.olvide_view, name='olvide'),
    path('bienvenido/', views.bienvenido_view, name='bienvenido'),
]
