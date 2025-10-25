# -*- coding: utf-8 -*-

# Se importa el módulo de serializers de Django REST Framework.
from rest_framework import serializers

# Se importa el modelo Sucursal desde el archivo models.py de la misma aplicación.
from .models import Sucursal


class SucursalSerializer(serializers.ModelSerializer):
    """
    Este serializer se encarga de convertir los objetos del modelo Sucursal a formatos
    como JSON (serialización) y de convertir datos JSON de vuelta a objetos Sucursal (deserialización).
    Está diseñado para ser explícito y autocontenido, sirviendo como el serializer principal
    para todas las operaciones CRUD (Crear, Leer, Actualizar, Borrar) de las sucursales.
    """
    class Meta:
        # La clase Meta configura el comportamiento del serializer.
        model = Sucursal  # Especifica que este serializer trabaja con el modelo 'Sucursal'.
        fields = '__all__'  # Indica que se deben incluir todos los campos declarados arriba.

    def get_direccion_completa(self, obj):
        """
        Este método genera el valor para el campo 'direccion_completa'.
        Concatena las partes de la dirección en una sola cadena de texto.
        `obj` es la instancia del modelo Sucursal que se está serializando.
        """
        # Se crea una lista con las partes de la dirección.
        partes_direccion = [
            obj.calle, obj.numero_exterior, obj.numero_interior,
            obj.colonia, obj.ciudad, obj.estado, obj.codigo_postal
        ]
        # Se usa filter(None, ...) para eliminar elementos vacíos y luego se unen con ", ".
        return ", ".join(filter(None, partes_direccion))

    # --- Métodos de Validación ---
    # Estos métodos son llamados automáticamente por el framework al deserializar los datos.

    def validate_nombre(self, value):
        """
        Validación para el campo 'nombre'.
        Asegura que el nombre de la sucursal sea único (ignorando mayúsculas/minúsculas).
        """
        # Se busca si ya existe una sucursal con ese nombre (insensible a mayúsculas).
        query = Sucursal.objects.filter(nombre__iexact=value)
        # Si se está actualizando un objeto (self.instance existe), se excluye a sí mismo de la búsqueda.
        if self.instance:
            query = query.exclude(pk=self.instance.pk)
        # Si la consulta encuentra algún resultado, significa que el nombre ya está en uso.
        if query.exists():
            # Se lanza un error de validación que será enviado en la respuesta de la API.
            raise serializers.ValidationError("Ya existe una sucursal con este nombre.")
        # Si la validación es exitosa, se devuelve el valor original.
        return value

    def validate_rfc(self, value):
        """
        Validación para el campo 'rfc'.
        Asegura que el RFC, si se proporciona, sea único.
        """
        # Si el valor es nulo o vacío, no se realiza la validación.
        if not value:
            return value
        # Se busca si ya existe una sucursal con ese RFC.
        query = Sucursal.objects.filter(rfc__iexact=value)
        # Si se está actualizando, se excluye el objeto actual de la búsqueda.
        if self.instance:
            query = query.exclude(pk=self.instance.pk)
        # Si ya existe, se lanza un error.
        if query.exists():
            raise serializers.ValidationError("Ya existe una sucursal registrada con este RFC.")
        # Se devuelve el valor si es válido.
        return value
