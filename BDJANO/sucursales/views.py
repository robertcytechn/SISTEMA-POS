# -*- coding: utf-8 -*-

# Se importan los módulos necesarios de Django REST Framework.
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

# Se importa el modelo Sucursal y su serializer correspondiente.
from .models import Sucursal
from .serializers import SucursalSerializer


class SucursalViewSet(viewsets.ModelViewSet):
    """
    Este ViewSet proporciona automáticamente las acciones `list`, `create`, `retrieve`,
    `update` y `destroy` para el modelo Sucursal.

    - `list`: Devuelve un listado de todas las sucursales.
    - `create`: Crea una nueva sucursal.
    - `retrieve`: Devuelve los detalles de una sucursal específica.
    - `update`: Actualiza completamente una sucursal.
    - `partial_update`: Actualiza parcialmente una sucursal.
    - `destroy`: Elimina una sucursal.
    """
    # `queryset` define el conjunto de objetos que estarán disponibles para ser vistos.
    # En este caso, son todos los registros del modelo Sucursal.
    queryset = Sucursal.objects.all()

    # `serializer_class` especifica el serializer que se usará para convertir
    # los objetos del modelo a JSON y viceversa.
    serializer_class = SucursalSerializer

    # Se añade el backend de filtro para habilitar la búsqueda.
    filter_backends = [SearchFilter]
    # Se especifica el campo por el cual se podrá buscar.
    search_fields = ['nombre']

    # `permission_classes` controla quién puede acceder a esta vista.
    # `AllowAny` permite el acceso a cualquier usuario, autenticado o no,
    # cumpliendo con el requisito de no necesitar inicio de sesión.
    permission_classes = [AllowAny]