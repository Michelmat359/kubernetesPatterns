#!/bin/bash
# Script de despliegue y prueba de patrones
set -e
PATTERN=$1
RELEASE=${2:-test}
if [ -z "$PATTERN" ]; then
  echo "Uso: $0 <patron> [release]"
  exit 1
fi
START=$(date +%s)
helm install $RELEASE charts/$PATTERN
kubectl wait --for=condition=available --timeout=120s deployment -l app=$PATTERN
END=$(date +%s)
BOOT_TIME=$((END-START))
python3 scripts/gather_metrics.py $PATTERN $RELEASE $BOOT_TIME
