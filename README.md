# kubernetesPatterns

Este repositorio reúne ejemplos básicos para comparar diferentes patrones de despliegue de modelos de inteligencia artificial en aplicaciones robóticas con ROS 2 y Kubernetes. Los patrones están descritos en `docs/estudio_patrones.md` y cada uno cuenta con una configuración mínima dentro de la carpeta `patterns/`.

La carpeta `charts/` contiene los Helm charts listos para usarse como catálogo en Rancher. El script `scripts/run_tests.sh` automatiza el despliegue de un patrón y utiliza `scripts/gather_metrics.py` para recoger métricas de rendimiento.

Para obtener más detalles de uso consulte `docs/catalogo_rancher.md`.
