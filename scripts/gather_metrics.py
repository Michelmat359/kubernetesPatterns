#!/usr/bin/env python3
"""Recopila métricas de un despliegue usando kubectl y Prometheus."""
import csv
import json
import subprocess
import sys
from datetime import datetime

PATTERN = sys.argv[1]
RELEASE = sys.argv[2]
BOOT_TIME = int(sys.argv[3])

result = {
    'pattern': PATTERN,
    'release': RELEASE,
    'boot_time_seconds': BOOT_TIME,
    'timestamp': datetime.utcnow().isoformat() + 'Z',
    'cpu_millicores': None,
    'memory_mebibytes': None,
}

try:
    top_output = subprocess.check_output(
        ['kubectl', 'top', 'pods', '-l', f'app={PATTERN}', '--no-headers'],
        text=True
    )
    first = top_output.strip().split()[1:3]
    cpu = first[0].rstrip('m')
    mem = first[1].rstrip('Mi')
    result['cpu_millicores'] = int(cpu)
    result['memory_mebibytes'] = int(mem)
except Exception as e:
    result['error'] = str(e)

with open(f'{PATTERN}_{RELEASE}_metrics.json', 'w') as f:
    json.dump(result, f, indent=2)

with open(f'{PATTERN}_{RELEASE}_metrics.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=result.keys())
    writer.writeheader()
    writer.writerow(result)
