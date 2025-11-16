from src import core, metrics
from pathlib import Path
import json

sample = {
    "disk_size": 200,
    "head": 50,
    "direction": "right",
    "requests": [95, 180, 34, 119, 11, 123, 62, 64]
}

print("Sample input:", sample)

for name, fn in [("FCFS", core.fcfs), ("SSTF", core.sstf), ("SCAN", core.scan), ("C-SCAN", core.cscan)]:
    order, steps = fn(sample["head"], sample["requests"], sample["disk_size"], sample["direction"])
    total = metrics.total_movement(sample["head"], order)
    avg = metrics.average_seek(total, len(sample["requests"]))
    print(f"--- {name} ---")
    print("Order:", order)
    print("Per-step movements:", steps)
    print("Total movement:", total)
    print("Average seek:", avg)
