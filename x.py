# x_replica.py
import json
from pathlib import Path


class XReplica:
    def __init__(self):
        self.name = "X Replica"
        self.skills = ["Dokumentasi", "Webhook Integrasi"]
        self.memory = []

    def sync_logs(self):
        print("[X Replica] Sinkronisasi log ke sistem eksternal")

    def add_memory(self, entry):
        self.memory.append(entry)
        
    def __init__(self):
        self.name = "Zero"
        self.memory = self.load_memory()

    def load_memory(self):
        path = Path("data/memory_log.json")
        if path.exists():
            with path.open() as f:
                data = json.load(f)
                return data.get(self.name, {})
        return {}