# Propuesta de Sistema de Punto de Venta (POS) para Tienda de Abarrotes

## 1. Objetivo del Sistema

Desarrollar una solución integral de punto de venta (POS) diseñada específicamente para optimizar la operación de tiendas de abarrotes. El sistema centralizará el control de ventas, inventarios y administración de personal en una o varias sucursales, proporcionando información en tiempo real para una toma de decisiones ágil y efectiva.

## 2. Arquitectura Tecnológica

Este proyecto está compuesto por dos partes principales:

*   **Backend (API REST):** Desarrollado con **Django**, ubicado en el directorio `/BDJANO`. Se encargará de toda la lógica de negocio, gestión de la base de datos, y de exponer los datos a través de endpoints.
*   **Frontend (Aplicación Cliente):** Desarrollado con **Vue.js**, ubicado en el directorio `/VUE`. Será la interfaz con la que interactúen los usuarios (cajeros, supervisores, administradores). Consumirá los datos expuestos por la API de Django.

## 3. Módulos del Sistema

A continuación, se describen los módulos principales que compondrán el sistema y sus funcionalidades clave.

### Módulo 1: Punto de Venta y Gestión de Cajas (POS)

Este es el corazón del sistema, donde se procesan todas las transacciones. La interfaz será intuitiva y rápida para minimizar el tiempo de espera del cliente.

#### Funcionalidades:

*   **Interfaz de Venta Rápida:**
    *   Registro de productos mediante escaneo de código de barras.
    *   Búsqueda de productos por nombre, código o categoría.
    *   Teclas de acceso rápido para productos de alta rotación (ej. refrescos, pan).
*   **Gestión de Pagos:**
    *   Soporte para múltiples métodos de pago: efectivo, tarjeta de crédito/débito, vales de despensa y pagos móviles.
    *   Cálculo automático de cambio.
*   **Sesiones de Caja (Turnos):**
    *   **Apertura de Turno:** El cajero inicia su sesión registrando un fondo inicial de efectivo.
    *   **Cierre de Turno (Corte de Caja):** Al finalizar, el sistema genera un resumen con las ventas totales, desglosando los montos por método de pago. El cajero realiza el conteo de efectivo y el sistema reporta cualquier sobrante o faltante.
    *   **Regla de Negocio Clave:** El sistema impedirá abrir un nuevo turno en una caja si ya existe uno activo, evitando duplicidades y errores contables.
*   **Funciones Adicionales:**
    *   Gestión de devoluciones y cancelaciones (requiere permisos de supervisor).
    *   Aplicación de descuentos y promociones de forma manual o automática.
    *   Generación e impresión de tickets de compra personalizables.
    *   Capacidad para poner ventas en espera y recuperarlas posteriormente.

### Módulo 2: Gestión de Inventario

Un control de inventario preciso es fundamental para evitar pérdidas y asegurar la disponibilidad de productos.

#### Funcionalidades:

*   **Catálogo de Productos:**
    *   Alta y edición de productos con detalles: nombre, descripción, SKU, categoría, precio de compra y precio de venta.
    *   Gestión de productos a granel (ej. frutas, semillas) y con variantes (ej. refrescos de distintos sabores).
    *   Carga masiva de productos mediante plantillas de Excel.
*   **Control de Existencias (Stock):**
    *   Actualización del inventario en tiempo real con cada transacción.
    *   Alertas de stock mínimo para gestionar el reabastecimiento.
*   **Movimientos de Inventario:**
    *   Registro de entradas de mercancía (compras).
    *   Transferencias de inventario entre sucursales.
    *   Ajustes manuales por mermas (productos caducados, dañados) o conteo físico.
*   **Gestión de Proveedores:**
    *   Base de datos de proveedores con información de contacto.
    *   Historial de compras por proveedor.

### Módulo 3: Reportes y Análisis

Este módulo proporcionará una visión clara del rendimiento del negocio a través de datos consolidados.

#### Funcionalidades:

*   **Reportes de Ventas:**
    *   **Reporte de Cierre Diario (Corte Z):** Resumen de ventas, métodos de pago, impuestos y ganancias.
    *   Ventas por período (día, semana, mes).
    *   Ventas por sucursal, cajero y caja.
*   **Reportes de Productos:**
    *   Ranking de productos más vendidos.
    *   Identificación de productos con baja rotación.
    *   Análisis de márgenes de ganancia por producto o categoría.
*   **Reportes de Inventario:**
    *   Valor total del inventario.
    *   Reporte de mermas y ajustes.
    *   Historial de movimientos de un producto (Kardex).
*   **Dashboard Principal:**
    *   Panel de control visual con gráficos y métricas clave (KPIs) para una vista rápida del estado del negocio en tiempo real.

### Módulo 4: Administración del Sistema

Desde aquí se gestiona la configuración global, la seguridad y el acceso a la plataforma.

#### Funcionalidades:

*   **Gestión Multi-Sucursal:**
    *   Administración centralizada de todas las sucursales.
    *   Gestión de catálogos y precios de forma global o por sucursal.
    *   Consolidación de reportes de todas las sucursales.
*   **Gestión de Usuarios y Roles:**
    *   Creación de cuentas de usuario.
    *   Asignación de roles y permisos (Cajero, Supervisor, Gerente, Administrador) para controlar el acceso a las funcionalidades.
*   **Configuración General:**
    *   Personalización de datos del negocio (nombre, dirección, RFC).
    *   Configuración de impuestos.
    *   Personalización de formatos de tickets.

## 4. Funcionalidades Adicionales Recomendadas

Para hacer el sistema más competitivo, se sugiere incluir a futuro:

*   **Programa de Lealtad:** Sistema de puntos o monedero electrónico.
*   **Gestión de Compras:** Generación y seguimiento de órdenes de compra.
*   **Facturación Electrónica (CFDI):** Integración con un PAC para emitir facturas fiscales.
*   **Modo Offline:** Permitir que el punto de venta siga operando sin conexión a internet, sincronizando los datos al reconectar.
*   **Compatibilidad con Hardware:** Garantizar compatibilidad con lectores de códigos, impresoras, cajones de dinero y básculas.
