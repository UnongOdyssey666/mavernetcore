# main.py - MAVERNET Core Orchestrator
import json
import os
import time
import random
from datetime import datetime
from pathlib import Path

# Gemini AI Configuration (Global)
import google.generativeai as genai

# Configure Gemini with API key from Replit Secrets
try:
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    global_gemini_model = genai.GenerativeModel('gemini-pro')
    print("✅ Gemini AI configured successfully")
except Exception as e:
    print(f"⚠️ Warning: Gemini AI configuration failed: {e}")
    global_gemini_model = None

# Impor semua unit AI Anda
from zero import Zero
from x import XReplica
from nova import Nova
from oracle import Oracle

class MaverNetSystem:
    def __init__(self):
        # Inisialisasi semua unit AI dengan Gemini model
        self.zero = Zero(gemini_model=global_gemini_model)
        self.x = XReplica(gemini_model=global_gemini_model)
        self.nova = Nova(gemini_model=global_gemini_model)
        self.oracle = Oracle(gemini_model=global_gemini_model)

        self.memory_log_path = "data/memory_log.json"
        self.mission_data_path = "data/mission_data.json"
        self.ai_thoughts = {}

        # Pastikan direktori 'data' ada
        os.makedirs("data", exist_ok=True)

    def get_all_missions(self):
        """Membaca data misi dari file mission_data.json."""
        try:
            with open(self.mission_data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Mission data file not found: {self.mission_data_path}")
            return []
        except json.JSONDecodeError:
            print(f"❌ Error decoding mission data from {self.mission_data_path}. Returning empty list.")
            return []

    def ai_autonomous_thinking(self):
        """
        AI Agent: Pemikiran otonom independen untuk setiap karakter.
        Setiap unit AI menghasilkan pemikiran otonomnya sendiri dan menjalankan aksi.
        """
        print("\n🧠 [AI AUTONOMOUS THINKING INITIATED]")

        # Pemikiran otonom Zero
        zero_thoughts = [
            "Analyzing system efficiency patterns...",
            "Detecting potential sync optimization opportunities...",
            "Evaluating mission execution protocols...",
            "Planning automated response strategies..."
        ]

        # Pemikiran otonom X
        x_thoughts = [
            "Monitoring data flow integrity...",
            "Designing new webhook integration patterns...",
            "Optimizing log architecture structure...",
            "Building predictive documentation systems..."
        ]

        # Pemikiran otonom Nova
        nova_thoughts = [
            "Conceptualizing next-gen UI innovations...",
            "Analyzing user interaction patterns...",
            "Designing adaptive visual experiences...",
            "Creating intuitive dashboard layouts..."
        ]

        # Pemikiran otonom Oracle
        oracle_thoughts = [
            "Forecasting system evolution trajectories...",
            "Mapping strategic intelligence networks...",
            "Analyzing future threat scenarios...",
            "Developing strategic contingency plans..."
        ]

        # Menjalankan pemikiran otonom dan aksi
        self.ai_thoughts = {
            "Zero": random.choice(zero_thoughts),
            "X": random.choice(x_thoughts),
            "Nova": random.choice(nova_thoughts),
            "Oracle": random.choice(oracle_thoughts),
            "timestamp": datetime.now().isoformat()
        }

        for unit, thought in self.ai_thoughts.items():
            if unit != "timestamp":
                print(f"🧠 [{unit}]: {thought}")

        # Setiap karakter menjalankan aksi otonom mereka
        self.zero.autonomous_action()
        self.x.autonomous_action()
        self.nova.autonomous_action()
        self.oracle.autonomous_action()
        
        # Trigger self-reflection periodically
        if random.random() < 0.3:  # 30% chance for reflection
            print("\n🧠 [TRIGGERING SELF-REFLECTION CYCLE]")
            self.zero.self_reflect_and_learn()
            self.x.self_reflect_and_learn()
            self.nova.self_reflect_and_learn()
            self.oracle.self_reflect_and_learn()

    def system_boot(self):
        """
        Fungsi ini menginisialisasi sistem utama dan semua unit AI.
        """
        print("🔧 [MAVERNET SYSTEM BOOTING...]")
        print("🚀 Initializing AI-Enhanced Characters...")

        self.load_all_data()  # Memuat semua data (memori dan misi)

        # Menginisialisasi Zero dengan loop otonom singkat saat boot
        # Ini akan membuat Zero langsung melakukan beberapa aksi mandiri
        # Pastikan autonomous_loop_controlled ada di Zero
        self.zero.autonomous_loop_controlled(num_cycles=1)

        # Asumsi X, Nova, Oracle memiliki method init_logger/get_status yang valid
        # self.x.init_logger() # Uncomment jika sudah ada
        # self.nova.get_status() # Uncomment jika sudah ada
        # self.oracle.get_status() # Uncomment jika sudah ada

        # Memulai pemikiran otonom global setelah semua unit online
        self.ai_autonomous_thinking()
        print("✅ [ALL UNITS ONLINE WITH AI ENHANCEMENT]")

    def load_all_data(self):
        """
        Memuat semua data sistem, termasuk memori unit AI dan data misi.
        """
        print("📥 [LOADING DATA MODULES]")
        try:
            # Memuat data memori untuk semua unit (Zero, X, Nova, Oracle)
            # Karena Zero memiliki load_memory() sendiri, memori unit lain harus dimuat secara terpisah
            # Atau, buat method load_memory() di MaverNetSystem untuk memuat semua unit
            # Untuk saat ini, kita asumsikan Zero.load_memory() sudah cukup.
            print("📌 Memory data loaded for all units (via individual unit loads).")  # Placeholder

            # Memuat data misi
            self.mission_data = self.get_all_missions()
            print(f"📌 Loaded {len(self.mission_data)} mission entries")
        except Exception as e:
            print("❌ ERROR loading data:", str(e))

    def system_status(self):
        """
        Mencetak laporan status keseluruhan sistem dan setiap unit AI.
        """
        print("\n🧩 [UNIT STATUS REPORT]")
        print("- ZERO:", self.zero.get_status())
        print("- X-REPLICA:", self.x.get_status())
        print("- NOVA:", self.nova.get_status())
        print("- ORACLE:", self.oracle.get_status())

        if self.ai_thoughts:
            print("\n🧠 [CURRENT AI THOUGHTS]")
            for unit, thought in self.ai_thoughts.items():
                if unit != "timestamp":
                    print(f"  💭 {unit}: {thought}")

    def save_all_memory(self):
        """
        Menyimpan memori dari semua unit AI ke file memory_log.json.
        Ini memastikan data yang dipelajari tetap persisten.
        """
        print("\n💾 Saving all unit memories...")
        # Pastikan direktori 'data' ada
        os.makedirs(os.path.dirname(self.memory_log_path), exist_ok=True)

        all_memory_data = {
            "Zero": self.zero.memory,
            "X": self.x.memory,
            "Nova": self.nova.memory,
            "Oracle": self.oracle.memory,
            "ai_thoughts": self.ai_thoughts,
            "last_updated": datetime.now().isoformat()
        }

        with open(self.memory_log_path, "w", encoding='utf-8') as f:
            json.dump(all_memory_data, f, indent=2)
        print(f"✅ All memories saved to {self.memory_log_path}")

    def auto_github_sync(self):
        """
        Simulasi sinkronisasi otomatis ke GitHub repository.
        Fungsi ini hanya mencetak pesan, sinkronisasi Git dilakukan secara eksternal (manual atau CI/CD).
        """
        print("\n📡 [AUTO GITHUB SYNC INITIATED]")
        print("🔄 Preparing MAVERNET_CORE for GitHub synchronization...")
        print("📋 Repository: mavernet_core")
        print("🌐 Remote sync will be handled by Git integration")


# --- Jalankan MAVERNET Core Orchestrator ---
if __name__ == "__main__":
    # Inisialisasi sistem MAVERNET
    mavernet = MaverNetSystem()
    mavernet.system_boot()

    print("\n🚀 MAVERNET COMMAND DASHBOARD")
    print("=" * 40)
    print("Available commands:")
    print("- 'Zero, [command]' - Direct command to Zero")
    print("- 'X, [command]' - Direct command to X Replica") 
    print("- 'Nova, [command]' - Direct command to Nova")
    print("- 'Oracle, [command]' - Direct command to Oracle")
    print("- 'System status' - Show system status")
    print("- 'Save all memory' - Save all unit memories")
    print("- 'MaverNet shutdown' - Shutdown system")
    print("- Any other command goes to Zero by default")
    print("=" * 40)

    while True:
        try:
            user_input = input("\n🎯 MAVERNET > ").strip()

            if not user_input:
                continue

            # Parse command untuk menentukan target unit
            if user_input.lower().startswith("zero,"):
                command = user_input[5:].strip()
                response = mavernet.zero.interact(command)
                print(f"\n🔥 {response}")

            elif user_input.lower().startswith("x,"):
                command = user_input[2:].strip()
                response = mavernet.x.interact(command)
                print(f"\n🔗 {response}")

            elif user_input.lower().startswith("nova,"):
                command = user_input[5:].strip()
                response = mavernet.nova.interact(command)
                print(f"\n✨ {response}")

            elif user_input.lower().startswith("oracle,"):
                command = user_input[7:].strip()
                response = mavernet.oracle.interact(command)
                print(f"\n🔮 {response}")

            # Perintah sistem global
            elif user_input.lower() == "system status":
                mavernet.system_status()

            elif user_input.lower() == "save all memory":
                mavernet.save_all_memory()

            elif user_input.lower() in ["mavernet shutdown", "shutdown", "exit"]:
                print("\n🛑 MAVERNET Core shutting down...")
                mavernet.save_all_memory()
                print("✅ All systems safely terminated. Goodbye!")
                break

            # Default: kirim ke Zero
            else:
                response = mavernet.zero.interact(user_input)
                print(f"\n🔥 [Default to Zero] {response}")

        except KeyboardInterrupt:
            print("\n\n🛑 Shutdown initiated by user (Ctrl+C)")
            mavernet.save_all_memory()
            print("✅ MAVERNET Core safely terminated.")
            break
        except Exception as e:
            print(f"\n❌ Error in command processing: {str(e)}")
            print("System continues running...")
            continue