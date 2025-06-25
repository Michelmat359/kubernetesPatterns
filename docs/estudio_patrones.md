# Comparación de patrones de despliegue de modelos IA con ROS 2 y Kubernetes

Este documento presenta cuatro patrones inspirados en el artículo *"Deploying AI Models in Cloud-Edge Robotics: A Comparative Study of Distribution Patterns with ROS 2"*. Cada patrón incluye una definición, un ejemplo de configuración y un análisis de ventajas y limitaciones.

## 1. Imágenes monolíticas Docker
**Definición**: integrar todos los modelos y dependencias en una sola imagen de contenedor.

### Configuración de ejemplo
- `patterns/pattern1_monolithic/Dockerfile`: imagen con todo el software y modelos.
- `patterns/pattern1_monolithic/k8s-deployment.yaml`: despliegue con un único contenedor.

### Ventajas
- Sencillez de despliegue (una única imagen).
- No depende de la red en tiempo de ejecución para obtener modelos.

### Limitaciones
- Tamaño de imagen elevado y actualizaciones costosas.
- Poca modularidad: cambios de un modelo requieren reconstruir la imagen completa.

## 2. Microservicios con imágenes precompiladas
**Definición**: dividir la aplicación en varios contenedores especializados que se comunican mediante ROS 2.

### Configuración de ejemplo
- `patterns/pattern2_microservices/Dockerfile`: imagen para el microservicio de percepción.
- `patterns/pattern2_microservices/k8s-deployment.yaml`: despliegue con múltiples contenedores (percepción, control, etc.).

### Ventajas
- Mejor modularidad y reutilización de componentes.
- Permite actualizar modelos de forma independiente.

### Limitaciones
- Mayor complejidad operativa y de orquestación.
- Consumo adicional de recursos por múltiples contenedores.

## 3. Carga dinámica de módulos
**Definición**: el contenedor base descarga y carga los modelos de IA al inicio o durante la ejecución desde fuentes remotas.

### Configuración de ejemplo
- `patterns/pattern3_dynamic_loading/Dockerfile`: incluye herramientas de descarga (wget/curl).
- `patterns/pattern3_dynamic_loading/k8s-deployment.yaml`: especifica la URL del modelo mediante una variable de entorno.

### Ventajas
- Flexibilidad máxima: se pueden cambiar los modelos sin reconstruir imágenes.
- Tamaños de imagen reducidos.

### Limitaciones
- Dependencia de la red para descargar los modelos.
- Riesgo de inconsistencias si la descarga falla.

## 4. Workspaces en Overlay para ROS 2
**Definición**: usar una imagen base ligera y añadir paquetes ROS 2 (y modelos) mediante Helm y overlays de workspaces.

### Configuración de ejemplo
- `patterns/pattern4_overlay_workspaces/Dockerfile`: imagen base.
- `patterns/pattern4_overlay_workspaces/chart/`: helm chart que instala paquetes en tiempo de despliegue.

### Ventajas
- Permite combinar paquetes de forma dinámica según el escenario.
- Buen equilibrio entre tamaño de imagen y flexibilidad.

### Limitaciones
- Requiere Helm y un proceso de overlay más complejo.
- Necesidad de acceso temporal a repositorios de paquetes en el despliegue.

## Tabla comparativa

| Patrón | Tamaño de imagen | Tiempo/Complejidad de actualización | Flexibilidad en tiempo de ejecución | Aislamiento de dependencias | Dependencia de red |
|-------|------------------|-------------------------------------|------------------------------------|----------------------------|-------------------|
| **Imágenes monolíticas** | Alto | Alto (reconstrucción completa) | Baja | Bajo | No |
| **Microservicios** | Medio | Medio (imágenes independientes) | Media | Alta (por contenedor) | No |
| **Carga dinámica** | Bajo | Bajo (solo cambia la URL) | Alta | Medio | Sí |
| **Overlay workspaces** | Bajo/Medio | Medio (gestión de Helm) | Alta | Medio | Sí (en despliegue) |

## Escenarios ideales
- **Imágenes monolíticas**: robots con conectividad limitada y modelos que cambian poco.
- **Microservicios**: sistemas complejos que requieren escalabilidad y separación clara de funciones.
- **Carga dinámica**: entornos de investigación o despliegues frecuentes de nuevos modelos.
- **Overlay workspaces**: proyectos que combinan múltiples paquetes ROS 2 y desean flexibilidad sin imágenes pesadas.

