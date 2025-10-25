# Descripción del Proyecto

Este es un sistema de Punto de Venta (POS) que utiliza un backend de API RESTful construido con Django y un frontend de una sola página (SPA) construido con Vue.js.

El proyecto está dividido en dos directorios principales:
- `BDJANO/`: Contiene el proyecto de Django.
- `VUE/`: Contiene el proyecto de Vue.js.

# Tecnologías

## Backend (`BDJANO/`)

*   **Framework:** Django
*   **API:** Django REST Framework
*   **Middleware:** Django CORS Headers (para comunicación con el frontend)
*   **Base de Datos:** MySQL (Nombre: `pos`, Usuario: `root`, Pass: `root`, Host: `localhost`)
*   **Apps Propias:** `sucursales`

## Frontend (`VUE/`)

*   **Framework:** Vue.js 3
*   **Build Tool:** Vite
*   **Enrutador:** Vue Router
*   **UI Kit:** PrimeVue 4
*   **Estilos:** Tailwind CSS con PrimeUI
*   **Linter:** ESLint