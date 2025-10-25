# -*- coding: utf-8 -*-

# Se importan los módulos necesarios de Django y Django REST Framework.
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Se importa el ViewSet definido en el archivo views.py de esta misma aplicación.
from .views import SucursalViewSet

# Se crea una instancia de DefaultRouter.
# El router se encarga de generar automáticamente las rutas URL para el ViewSet.
router = DefaultRouter()

# Se registra el SucursalViewSet con el router.
# - El primer argumento, r'sucursales', define el prefijo de la URL para este recurso.
#   Las URLs generadas serán del tipo /sucursales/ y /sucursales/{pk}/.
# - El segundo argumento es el ViewSet que manejará las peticiones.
# - `basename` es el nombre base para las URLs generadas, útil para revertirlas.
router.register(r'sucursales', SucursalViewSet, basename='sucursal')

# `urlpatterns` es la lista de patrones de URL que Django buscará.
# Aquí, simplemente incluimos todas las URLs generadas por el router.
urlpatterns = router.urls
