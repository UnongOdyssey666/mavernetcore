
# main.py
import json
import os

from zero import Zero
from x import XReplica
from nova import Nova
from oracle import Oracle

class MaverNetSystem:
    def __init__(self):
        self.zero = Zero()
        self.x = XReplica()
        self.nova = Nova()
        self.oracle = Oracle()
        self.memory_log_path = "data/memory_log/memory_log.json"
        self.mission_data_path = "data/mission_data.json"
        self.skill_tree_path = "data/skill_tree.json"

    def get_all_missions(self):
        try:
            with open(self.mission_data_path) as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Mission data file not found: {self.mission_data_path}")
            return []

    def system_boot(self):
        print("🔧 [MAVERNET SYSTEM BOOTING...]")
        self.load_all_data()
        self.zero.initiate_protocol()
        self.x.init_logger()
        self.nova.get_status()
        self.oracle.get_status()
        print("✅ [ALL UNITS ONLINE]")

    def load_all_data(self):
        print("📥 [LOADING DATA MODULES]")
        try:
            # Load memory data
            if os.path.exists(self.memory_log_path):
                with open(self.memory_log_path, "r") as f:
                    memory_data = json.load(f)
                    print(f"📌 Memory data loaded for all units")

            # Load mission data
            if os.path.exists(self.mission_data_path):
                self.mission_data = self.get_all_missions()
                print(f"📌 Loaded {len(self.mission_data)} mission entries")

            # Load skill tree
            if os.path.exists(self.skill_tree_path):
                with open(self.skill_tree_path, "r") as f:
                    self.skill_tree = json.load(f)
                    self.zero.load_skills(self.skill_tree.get("Zero", {}))
                    self.x.load_skills(self.skill_tree.get("X", {}))
                    self.nova.load_skills(self.skill_tree.get("Nova", {}))
                    self.oracle.load_skills(self.skill_tree.get("Oracle", {}))
                    print(f"🧬 Skill Trees Loaded for all units")

        except Exception as e:
            print("❌ ERROR loading data:", str(e))

    def system_status(self):
        print("\n🧩 [UNIT STATUS REPORT]")
        print("- ZERO:", self.zero.get_status())
        print("- X-REPLICA:", self.x.get_status())
        print("- NOVA:", self.nova.get_status())
        print("- ORACLE:", self.oracle.get_status())

    def save_all_memory(self):
        print("\n💾 Saving all unit memories...")
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.memory_log_path), exist_ok=True)
        
        all_memory = {
            "Zero": self.zero.memory,
            "X": self.x.memory,
            "Nova": self.nova.memory,
            "Oracle": self.oracle.memory
        }
        
        with open(self.memory_log_path, "w") as f:
            json.dump(all_memory, f, indent=2)
        print(f"✅ All memories saved to {self.memory_log_path}")

# Jalankan MAVERNET
if __name__ == "__main__":
    system = MaverNetSystem()
    system.system_boot()
    system.system_status()
    system.save_all_memory()
