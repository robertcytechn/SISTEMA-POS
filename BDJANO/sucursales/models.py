from django.db import models
from django.utils.translation import gettext_lazy as _

class Sucursal(models.Model):
    """
    Modelo para representar una sucursal o tienda física del negocio.
    Este modelo es autocontenido y no tiene relaciones con otros modelos.
    """

    # --- Información Básica de la Sucursal ---
    nombre = models.CharField(
        max_length=100,
        unique=True,
        help_text=_("Nombre único para identificar la sucursal.")
    )
    activa = models.BooleanField(
        default=True,
        help_text=_("Indica si la sucursal está operativa. Desmarcar en lugar de borrar para mantener la integridad de los datos históricos.")
    )

    # --- Información de Contacto y Ubicación ---
    calle = models.CharField(_("Calle"), max_length=255)
    numero_exterior = models.CharField(_("Número Exterior"), max_length=20)
    numero_interior = models.CharField(_("Número Interior/Local"), max_length=20, blank=True, null=True)
    colonia = models.CharField(_("Colonia/Barrio"), max_length=100)
    ciudad = models.CharField(_("Ciudad"), max_length=100)
    estado = models.CharField(_("Estado/Provincia"), max_length=100)
    codigo_postal = models.CharField(_("Código Postal"), max_length=10)
    pais = models.CharField(_("País"), max_length=50, default="México")
    
    telefono = models.CharField(
        max_length=20,
        blank=True,
        help_text=_("Número de teléfono de contacto de la sucursal.")
    )
    email = models.EmailField(
        _("Correo Electrónico"),
        max_length=254,
        blank=True,
        help_text=_("Correo electrónico de contacto de la sucursal.")
    )

    # --- Información Administrativa y Fiscal ---
    gerente = models.CharField(
        _("Nombre del Gerente"),
        max_length=150,
        blank=True, # El campo es opcional
        help_text=_("Nombre del gerente o responsable de la sucursal.")
    )
    fecha_apertura = models.DateField(
        _("Fecha de Apertura"),
        blank=True,
        null=True,
        help_text=_("Fecha en que la sucursal inició operaciones.")
    )
    rfc = models.CharField(
        _("Registro Federal de Contribuyentes (RFC)"),
        max_length=13,
        unique=True,
        blank=True,
        null=True,
        help_text=_("RFC de la sucursal para facturación. Debe ser único si se especifica.")
    )

    # --- Campos de Auditoría ---
    creado_en = models.DateTimeField(
        _("Fecha de Creación"),
        auto_now_add=True,
        help_text=_("Fecha y hora en que se creó el registro.")
    )
    actualizado_en = models.DateTimeField(
        _("Última Actualización"),
        auto_now=True,
        help_text=_("Fecha y hora de la última modificación del registro.")
    )

    class Meta:
        verbose_name = _("Sucursal")
        verbose_name_plural = _("Sucursales")
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def direccion_completa(self):
        """
        Devuelve la dirección completa como una sola cadena.
        """
        partes_direccion = [
            self.calle, self.numero_exterior, self.numero_interior,
            self.colonia, self.ciudad, self.estado, self.codigo_postal
        ]
        return ", ".join(filter(None, partes_direccion))
