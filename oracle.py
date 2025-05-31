
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
        self.memory = self.load_memory()
        self.map_data = {}

    def load_memory(self):
        path = Path("data/memory_log/memory_log.json")
        if path.exists():
            with path.open() as f:
                data = json.load(f)
                return data.get(self.name, {})
        return {}

    def update_map(self, area, data):
        self.map_data[area] = data
        print(f"[Oracle] Map updated for area: {area}")

    def generate_briefing(self):
        # Simulasi pembuatan briefing dari data intelijen
        print("[Oracle] Generating briefing report...")
        for area, info in self.map_data.items():
            print(f" - {area}: {info}")

    def add_memory(self, entry):
        if isinstance(self.memory, dict):
            self.memory = []
        self.memory.append(entry)
        print(f"[Oracle] Memory added.")

    def load_skills(self, skills_data):
        print(f"[Oracle] Skills loaded: {skills_data}")

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_count": len(self.memory) if isinstance(self.memory, list) else 1,
            "mapped_areas": list(self.map_data.keys()),
        }
