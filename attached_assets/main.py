# main.py
import json

from zero import Zero
from x import XReplica
from nova import Nova
from oracle import Oracle

class MaverNetSystem:
    def get_all_missions():
    with open("data/mission_data.json") as f:
        return json.load(f)
    
    def __init__(self):
        self.zero = Zero()
        self.x = XReplica()
        self.nova = Nova()
        self.oracle = Oracle()

    def system_boot(self):
        print("🔧 [MAVERNET SYSTEM BOOTING...]")
        self.zero.initiate_protocol()
        self.x.init_logger()
        self.nova.get_status()
        self.oracle.get_status()
        print("✅ [ALL UNITS ONLINE]")

    def system_status(self):
        print("\n🧩 [UNIT STATUS REPORT]")
        print("- ZERO:", self.zero.get_status())
        print("- X-REPLICA:", self.x.get_status())
        print("- NOVA:", self.nova.get_status())
        print("- ORACLE:", self.oracle.get_status())

    def save_all_memory(self):
        print("\n💾 Saving all unit memories...")
        all_memory = {
            "Zero": self.zero.memory,
            "X": self.x.memory,
            "Nova": self.nova.memory,
            "Oracle": self.oracle.memory
        }
        with open("data/memory_log.json", "w") as f:
            import json
            json.dump(all_memory, f, indent=2)
        print("✅ All memories saved to data/memory_log.json")

# Jalankan MAVERNET
if __name__ == "__main__":
    system = MaverNetSystem()
    system.system_boot()
    system.system_status()
    system.save_all_memory()
    
    
    

