# oracle.py
import json
from pathlib import Path

class Oracle:
    def __init__(self):
        self.name = "Oracle"
        self.skills = [
            "Intelijen Data",
            "Pemetaan & Visualisasi",
            "Briefing & Analisis",
        ]
        self.memory = []
        self.map_data = {}

    def update_map(self, area, data):
        self.map_data[area] = data
        print(f"[Oracle] Map updated for area: {area}")

    def generate_briefing(self):
        # Simulasi pembuatan briefing dari data intelijen
        print("[Oracle] Generating briefing report...")
        for area, info in self.map_data.items():
            print(f" - {area}: {info}")

    def add_memory(self, entry):
        self.memory.append(entry)
        print(f"[Oracle] Memory added.")

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_count": len(self.memory),
            "mapped_areas": list(self.map_data.keys()),
        }
        
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