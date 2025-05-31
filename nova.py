# nova.py
import json
from pathlib import Path


class Nova:
    def __init__(self):
        self.name = "Nova"
        self.skills = [
            "Desain UI",
            "Visualisasi Dashboard",
            "Chart & Grafik Statistik",
        ]
        self.memory = []
        self.visual_data = {}

    def update_visual_data(self, key, value):
        self.visual_data[key] = value
        print(f"[Nova] Visual data updated: {key} = {value}")

    def generate_dashboard(self):
        # Simulasi pembuatan dashboard visual
        print("[Nova] Generating dashboard with current visual data...")
        for k, v in self.visual_data.items():
            print(f" - {k}: {v}")

    def add_memory(self, entry):
        self.memory.append(entry)
        print(f"[Nova] Memory added.")

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_count": len(self.memory),
            "visual_data_keys": list(self.visual_data.keys()),
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