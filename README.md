# 🌟 Plan de Proyecto: Sistema de Punto de Venta (POS) 🌟

> ### Resumen General
> **Duración Total (Producto Mínimo Viable):** 18 Semanas (90 días hábiles)
> **Metodología:** Desarrollo Vertical (Ágil). Cada fase entrega un módulo funcional que incluye tanto el Backend (lógica del servidor) como el Frontend (interfaz de usuario).

---

## 🚀 Fase 1: Cimientos y Administración Básica (Semanas 1-4)

_**Objetivo:** Establecer la estructura fundamental del proyecto, la seguridad y la capacidad de gestionar sucursales y usuarios._

### Semana 1: ⚙️ Configuración y Autenticación (Backend)
- **Día 1: Configuración del Servidor (Django)**
  - Iniciar el proyecto y realizar la configuración inicial (`settings.py`), incluyendo la conexión a la base de datos (`MySQL`) y la configuración regional.
  - Crear la aplicación principal del proyecto.
- **Día 2: Modelos de Datos de Autenticación**
  - Definir el modelo de **Usuario** personalizado y el modelo de **Rol** (Administrador, Gerente, Cajero).
- **Día 3: Serializers y Estrategia de Autenticación**
  - Crear los serializers para los modelos de Usuario y Rol.
  - Configurar el framework para la API (`Django REST Framework`) y la estrategia de autenticación mediante tokens (`JWT`).
- **Día 4: API de Autenticación**
  - Desarrollar los endpoints de la API para **iniciar sesión** (`/login/`) y **cerrar sesión** (`/logout/`).
- **Día 5: API de Gestión de Usuarios**
  - Desarrollar la API para la gestión completa de Usuarios (Crear, Leer, Actualizar, Eliminar).
  - Establecer permisos para que solo los Administradores puedan gestionar otros usuarios.
  - Realizar pruebas de validación de todas las APIs.

### Semana 2: 💻 Interfaz de Autenticación (Frontend) y Modelo Sucursal (Backend)
- **Día 6: Configuración del Cliente (Vue.js)**
  - Iniciar el proyecto de frontend con `Vue 3`.
  - Instalar y configurar las librerías base: `PrimeVue` (componentes UI), `Vue Router` (rutas) y `Pinia` (estado).
- **Día 7: Diseño de la Interfaz Principal**
  - Crear el layout principal de la aplicación (`App.vue`) que incluya un Menú Lateral (Sidebar) y una Barra de Navegación.
- **Día 8: Diseño de la Vista de Login**
  - Construir la página de inicio de sesión con un formulario para usuario y contraseña, utilizando componentes de `PrimeVue`.
- **Día 9: Lógica de Conexión del Login**
  - Conectar el formulario de Login con la API del backend.
  - Al autenticarse, guardar el token de sesión y los datos del usuario en el gestor de estado (`Pinia`).
  - Implementar la protección de rutas privadas para que solo usuarios autenticados puedan acceder.
- **Día 10: Modelo de Datos de Sucursal (Backend)**
  - Crear el modelo de **Sucursal** en la base de datos, incluyendo validaciones de negocio (RFC, teléfono, email).
  - Crear los serializers correspondientes para listar y detallar sucursales.

### Semana 3: 🏢 Módulo de Sucursales (Full Stack)
- **Día 11: API de Sucursales (Backend)**
  - Desarrollar la API para la gestión completa de Sucursales, incluyendo filtros y acciones para activar/desactivar.
  - Realizar pruebas de validación de la API.
- **Día 12: Vista de Lista de Sucursales (Frontend)**
  - Crear la interfaz para mostrar la lista de sucursales utilizando una tabla de datos de `PrimeVue`.
- **Día 13: Conexión de la Vista de Sucursales (Frontend)**
  - Conectar la tabla de sucursales a la API del backend.
  - Implementar funcionalidades de paginación y filtros en la interfaz.
- **Día 14: Formulario de Creación y Edición de Sucursales (Frontend)**
  - Diseñar y construir el formulario para registrar y modificar los datos de una sucursal.
- **Día 15: Lógica del Formulario de Sucursales (Frontend)**
  - Conectar el formulario a las APIs de creación y edición.
  - Implementar la lógica para los botones de activar/desactivar.
  - Realizar pruebas completas del flujo de gestión de sucursales.

### Semana 4: 🧑‍💼 Módulo de Usuarios (Frontend) y Cierre de Fase
- **Día 16: Vista de Lista de Usuarios (Frontend)**
  - Crear la interfaz para mostrar la lista de usuarios del sistema.
- **Día 17: Formulario de Creación y Edición de Usuarios (Frontend)**
  - Construir el formulario para registrar y modificar usuarios, incluyendo la asignación de Rol y Sucursal.
- **Día 18: Conexión del Módulo de Usuarios (Frontend)**
  - Conectar la vista y el formulario a la API de gestión de usuarios.
- **Día 19: Pruebas de Integración (Fase 1)**
  - Validar el flujo completo: Un Administrador inicia sesión, crea una Sucursal y asigna un nuevo usuario de tipo Gerente a esa sucursal.
- **Día 20: 🏁 Revisión y Demostración al Cliente (Fase 1)**
  - Presentación de los módulos de Login, Usuarios y Sucursales 100% funcionales.

---

## 📦 Fase 2: Módulo de Inventario (Semanas 5-9)

_**Objetivo:** Dotar al sistema de la capacidad para catalogar productos y gestionar el stock de manera eficiente._

### Semana 5: 🗂️ Gestión de Categorías y Modelo de Producto
- **Día 21: API de Categorías (Backend)**
- **Día 22: Interfaz de Categorías (Frontend)**
- **Día 23: Conexión y Pruebas del Módulo de Categorías**
- **Día 24: Modelo de Datos de Producto (Backend)**
- **Día 25: Serializers de Producto (Backend)**

### Semana 6: 🏭 API de Productos (Backend)
- **Día 26: API de Gestión de Productos**
- **Día 27: Filtros de Búsqueda para Productos**
- **Día 28: Filtros de Consulta para Productos**
- **Día 29: Pruebas de la API de Productos**
- **Día 30: Funcionalidad de Carga Masiva (desde Excel)**

### Semana 7: 🖥️ Módulo de Productos (Frontend)
- **Día 31: Vista de Lista de Productos**
- **Día 32: Conexión de la Lista de Productos**
- **Día 33: Filtros en la Interfaz de Productos**
- **Día 34: Formulario de Producto**
- **Día 35: Conexión del Formulario de Producto**

### Semana 8: 📈 Ajustes de Inventario (Full Stack)
- **Día 36: Modelo de Movimientos de Inventario (Backend)**
- **Día 37: API de Movimientos de Inventario (Backend)**
- **Día 38: Vista de Ajustes de Inventario (Frontend)**
- **Día 39: Conexión de la Vista de Ajustes (Frontend)**
- **Día 40: Historial de Movimientos (Full Stack)**

### Semana 9: 🧪 Cierre de Fase 2
- **Días 41-43: Pruebas de Integración**
- **Día 44: Corrección de Errores (Fase 1 y 2)**
- **Día 45: 🏁 Revisión y Demostración al Cliente (Fase 2)**

---

## 💰 Fase 3: Módulo de Ventas (Semanas 10-15)

_**Objetivo:** Permitir al sistema gestionar sesiones de caja y procesar ventas, actualizando el inventario en tiempo real._

### Semana 10: 🏪 Cajas y Turnos (Backend)
- **Día 46: Gestión de Cajas (Full Stack)**
- **Día 47: Modelo de Turnos (Backend)**
- **Día 48: API para Abrir Turno (Backend)**
- **Día 49: API para Cerrar Turno (Backend)**
- **Día 50: Pruebas de la API de Turnos**

### Semana 11: 💳 Ventas Transaccionales (Backend)
- **Día 51: Modelos de Venta (Backend)**
- **Día 52: Serializers de Venta (Backend)**
- **Día 53: API de Procesamiento de Ventas (Lógica)**
- **Día 54: API de Procesamiento de Ventas (Transacción)**
- **Día 55: API de Procesamiento de Ventas (Seguridad y Transacción Atómica)**

### Semana 12: ⏳ Flujo de Turnos (Frontend)
- **Día 56: Contexto de Cajero (Gestión de Estado)**
- **Día 57: Vista "Abrir Turno"**
- **Día 58: Conexión "Abrir Turno"**
- **Día 59: Vista "Cerrar Turno"**
- **Día 60: Conexión "Cerrar Turno"**

### Semana 13: 🛒 Interfaz de Punto de Venta (POS) (Frontend)
- **Día 61: Diseño de la Interfaz del POS**
- **Día 62: Componente de Búsqueda de Productos**
- **Día 63: Componente del Carrito de Compras**
- **Día 64: Componente de Totales**
- **Día 65: Componente de Cobro**

### Semana 14: 🧾 Flujo de Venta (Frontend - Conexión)
- **Día 66: Estructuración de Datos de Venta**
- **Día 67: Envío de la Venta a la API**
- **Día 68: Manejo de Respuesta de la Venta (Éxito / Error)**
- **Día 69: Cancelación de Ventas (Full Stack)**
- **Día 70: Impresión de Ticket**

### Semana 15: 🧪 Cierre de Fase 3
- **Días 71-73: Pruebas de Integración**
- **Día 74: Corrección de Errores Críticos**
- **Día 75: 🏁 Revisión y Demostración al Cliente (Fase 3)**

---

## 📊 Fase 4: Reportes y Notificaciones (Semanas 16-17)

_**Objetivo:** Proporcionar información clave para la toma de decisiones y automatizar alertas importantes._

### Semana 16: 📈 Reportes (Full Stack)
- **Día 76: API de Reporte de Cierre de Turno (Backend)**
- **Día 77: Vista de Reporte de Cierre de Turno (Frontend)**
- **Día 78: API de Reporte de Ventas (Backend)**
- **Día 79: Vista de Reporte de Ventas (Frontend)**
- **Día 80: Reportes de Inventario (Productos más vendidos / Bajo stock)**

### Semana 17: 📧 Notificaciones y Cierre
- **Día 81: Configuración de Envío de Email (Backend)**
- **Día 82: Notificación Automática de Stock Bajo (Backend)**
- **Día 83: Notificación Automática de Cierre de Día (Backend)**
- **Día 84: Pruebas y Corrección de Errores Finales**
- **Día 85: 🏁 Revisión y Demostración al Cliente (Fase 4)**

---

## ✅ Fase 5: Despliegue y Cierre (Semana 18)

_**Objetivo:** Instalar el sistema en el servidor local del cliente y capacitar a los usuarios finales._

- **Día 86: 🛠️ Preparación del Servidor**
- **Día 87: ⚙️ Despliegue del Backend (Django + Gunicorn + Nginx)**
- **Día 88: 💻 Despliegue del Frontend (Vue.js + Nginx)**
- **Día 89: 🚀 Marcha Blanca y Carga de Datos Inicial**
- **Día 90: 🎉 Capacitación y Entrega Final**

---

## 💡 Fase 6: Módulo Opcional (Post-Lanzamiento)

> **Duración Estimada:** 3-4 Semanas Adicionales

- **Módulo de Facturación Electrónica (CFDI)**
  - **Análisis:** Definición de requerimientos y selección de un Proveedor Autorizado de Certificación (PAC).
  - **Backend:** Desarrollo de APIs para la conexión con el PAC.
  - **Frontend:** Desarrollo del flujo para que el cliente solicite su factura.
