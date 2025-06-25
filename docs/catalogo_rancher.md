# Catálogo Rancher para comparar patrones de despliegue

Este repositorio incluye un catálogo Helm compatible con Rancher en la carpeta `charts/`.
Cada subcarpeta representa un patrón de despliegue o componentes de monitoreo.

## Uso rápido
1. Agregue este repositorio como catálogo en Rancher.
2. Despliegue el chart `monitoring` para obtener Prometheus y Grafana.
3. Despliegue cualquiera de los patrones (`pattern1-monolithic`, `pattern2-microservices`,
   `pattern3-dynamic-loading`, `pattern4-overlay-workspaces`).
4. Ejecute `scripts/run_tests.sh <patron>` para recopilar métricas y generar
   archivos `CSV` y `JSON` con los resultados.

Los dashboards de Grafana incluyen paneles básicos para latencia, uso de CPU,
memoria y tráfico de red. Puede ampliar las consultas editando los dashboards
desde la interfaz de Grafana.
