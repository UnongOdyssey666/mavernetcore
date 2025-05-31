
# x.py
import json
from pathlib import Path

class XReplica:
    def __init__(self):
        self.name = "X"
        self.skills = ["Dokumentasi", "Webhook Integrasi"]
        self.memory = self.load_memory()

    def load_memory(self):
        path = Path("data/memory_log/memory_log.json")
        if path.exists():
            with path.open() as f:
                data = json.load(f)
                return data.get(self.name, {})
        return {}

    def sync_logs(self):
        print("[X Replica] Sinkronisasi log ke sistem eksternal")

    def add_memory(self, entry):
        if isinstance(self.memory, dict):
            self.memory = []
        self.memory.append(entry)

    def init_logger(self):
        print("[X Replica] Logger initialized")

    def load_skills(self, skills_data):
        print(f"[X Replica] Skills loaded: {skills_data}")

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_count": len(self.memory) if isinstance(self.memory, list) else 1,
        }
