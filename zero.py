
# zero.py
import json
from pathlib import Path

class Zero:
    def __init__(self):
        self.name = "Zero"
        self.skills = ["Eksekutor Misi", "Sinkronisasi"]
        self.memory = self.load_memory()

    def load_memory(self):
        path = Path("data/memory_log/memory_log.json")
        if path.exists():
            with path.open() as f:
                data = json.load(f)
                return data.get(self.name, {})
        return {}

    def load_data(self, data):
        self.memory = data.get("memory", [])

    def run_mission(self, mission):
        # Logika pelaksanaan misi Zero
        print(f"[Zero] menjalankan misi: {mission}")

    def add_memory(self, entry):
        if isinstance(self.memory, dict):
            self.memory = []
        self.memory.append(entry)

    def initiate_protocol(self):
        print("[Zero] Protocol initiated")

    def load_skills(self, skills_data):
        print(f"[Zero] Skills loaded: {skills_data}")

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_count": len(self.memory) if isinstance(self.memory, list) else 1,
        }
