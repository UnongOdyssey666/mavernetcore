
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
        self.memory = self.load_memory()
        self.visual_data = {}

    def load_memory(self):
        path = Path("data/memory_log/memory_log.json")
        if path.exists():
            with path.open() as f:
                data = json.load(f)
                return data.get(self.name, {})
        return {}

    def update_visual_data(self, key, value):
        self.visual_data[key] = value
        print(f"[Nova] Visual data updated: {key} = {value}")

    def generate_dashboard(self):
        # Simulasi pembuatan dashboard visual
        print("[Nova] Generating dashboard with current visual data...")
        for k, v in self.visual_data.items():
            print(f" - {k}: {v}")

    def add_memory(self, entry):
        if isinstance(self.memory, dict):
            self.memory = []
        self.memory.append(entry)
        print(f"[Nova] Memory added.")

    def load_skills(self, skills_data):
        print(f"[Nova] Skills loaded: {skills_data}")

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_count": len(self.memory) if isinstance(self.memory, list) else 1,
            "visual_data_keys": list(self.visual_data.keys()),
        }
