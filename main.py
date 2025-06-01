# main.py - MAVERNET Core Orchestrator
import json
import os
import time
import random
import re
from datetime import datetime
from pathlib import Path

# Impor library Gemini API
import google.generativeai as genai

# Impor semua unit AI Anda
# Pastikan Anda memiliki file-file ini di folder yang sama: zero.py, x.py, nova.py, oracle.py
from zero import Zero
from x import XReplica
from nova import Nova
from oracle import Oracle

# --- Konfigurasi Global Gemini API ---
# Pastikan GEMINI_API_KEY sudah disimpan di Replit Secrets Anda
api_key = os.environ.get("GEMINI_API_KEY")
global_gemini_model = None

if not api_key:
    print("❌ ERROR: GEMINI_API_KEY not found in Replit Secrets. Gemini AI features will be limited.")
else:
    try:
        # Konfigurasi genai di level global, hanya sekali
        genai.configure(api_key=api_key)
        
        # Try different model names in order of preference
        model_names = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
        
        for model_name in model_names:
            try:
                global_gemini_model = genai.GenerativeModel(model_name)
                # Test the model with a simple request
                test_response = global_gemini_model.generate_content("Hello")
                print(f"✅ Gemini AI configured successfully with model: {model_name}")
                break
            except Exception as model_error:
                print(f"⚠️ Model {model_name} not available: {str(model_error)}")
                continue
        
        if global_gemini_model is None:
            print("❌ ERROR: No Gemini models are available. Running without AI features.")
            
    except Exception as e:
        print(f"❌ ERROR configuring Gemini AI: {str(e)}. Running without AI features.")
        global_gemini_model = None


class MaverNetSystem:
    def __init__(self):
        # Check for administrator access override
        self.admin_mode = self.check_admin_access()
        if self.admin_mode:
            print("👑 ADMINISTRATOR ACCESS DETECTED - FULL PRIVILEGES GRANTED")
        
        # Inisialisasi semua unit AI dengan meneruskan model Gemini
        self.zero = Zero(gemini_model=global_gemini_model, admin_mode=self.admin_mode)
        self.x = XReplica(gemini_model=global_gemini_model, admin_mode=self.admin_mode)
        self.nova = Nova(gemini_model=global_gemini_model, admin_mode=self.admin_mode)
        self.oracle = Oracle(gemini_model=global_gemini_model, admin_mode=self.admin_mode)

        self.memory_log_path = "data/memory_log.json"
        self.mission_data_path = "data/mission_data.json"
        self.ai_thoughts = {}

        # Pastikan direktori 'data' ada
        os.makedirs("data", exist_ok=True)

    def check_admin_access(self):
        """Check if administrator access is granted"""
        try:
            admin_files = [
                "data/admin_privileges.json",
                "data/system_overrides.json",
                "data/mavernet_admin_config.json"
            ]
            
            for admin_file in admin_files:
                if os.path.exists(admin_file):
                    with open(admin_file, 'r', encoding='utf-8') as f:
                        admin_config = json.load(f)
                        if admin_config:
                            return True
            return False
        except Exception:
            return False

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
        # Pastikan method 'autonomous_action' ada di setiap unit
        self.zero.autonomous_action()
        self.x.autonomous_action()
        self.nova.autonomous_action()
        self.oracle.autonomous_action()

    def system_boot(self):
        """
        Fungsi ini menginisialisasi sistem utama dan semua unit AI.
        """
        print("🔧 [MAVERNET SYSTEM BOOTING...]")
        print("🚀 Initializing AI-Enhanced Characters...")

        self.load_all_data() # Memuat semua data (memori dan misi)

        # Menginisialisasi Zero dengan loop otonom singkat saat boot
        # Ini akan membuat Zero langsung melakukan beberapa aksi mandiri
        self.zero.autonomous_loop_controlled(num_cycles=1) 
        # Unit lain juga bisa punya loop otonom saat boot jika diperlukan
        # self.x.autonomous_loop_controlled(num_cycles=1) 

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
            # Setiap unit memuat memorinya sendiri via Zero.load_memory()
            print("📌 Memory data loaded for all units (via individual unit loads).") 

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
        # Asumsi X, Nova, Oracle memiliki method get_status() yang valid
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

        # Setiap unit akan memanggil save_memory() mereka sendiri.
        # Ini lebih modular daripada mencoba mengumpulkannya di sini.
        self.zero.save_memory()
        self.x.save_memory()
        self.nova.save_memory()
        self.oracle.save_memory()

        # Simpan juga AI thoughts global jika diperlukan
        global_mavernet_memory = {
            "ai_thoughts_global": self.ai_thoughts,
            "last_updated_global": datetime.now().isoformat()
        }
        # Anda bisa menyimpan ini ke file terpisah jika tidak ingin menimpa memory_log.json utama
        # Misalnya, save ke 'data/mavernet_global_memory.json'
        # with open("data/mavernet_global_memory.json", "w", encoding='utf-8') as f:
        #     json.dump(global_mavernet_memory, f, indent=2)

        print(f"✅ All unit memories saved to their respective files in 'data/'.")


    def auto_github_sync(self):
        """
        Simulasi sinkronisasi otomatis ke GitHub repository.
        Fungsi ini hanya mencetak pesan, sinkronisasi Git dilakukan secara eksternal (manual atau CI/CD).
        """
        print("\n📡 [AUTO GITHUB SYNC INITIATED]")
        print("🔄 Preparing MAVERNET_CORE for GitHub synchronization...")
        print("📋 Repository: mavernet_core")
        print("🌐 Remote sync will be handled by Git integration")


    def process_system_command(self, command):
        """
        Memproses perintah yang ditujukan untuk keseluruhan sistem MaverNet.
        """
        command_lower = command.lower().strip()

        if "system status" in command_lower:
            self.system_status()
            return "[MaverNet]: Laporan status sistem ditampilkan di atas."
        elif "save all memory" in command_lower:
            self.save_all_memory()
            return "[MaverNet]: Memori seluruh sistem berhasil disimpan."
        elif "auto github sync" in command_lower:
            self.auto_github_sync()
            return "[MaverNet]: Permintaan sinkronisasi GitHub diproses."
        elif "mavernet shutdown" in command_lower:
            # Panggil shutdown Zero, yang akan mengubah status dan mengakhiri loop utama
            response = self.zero.interact("shutdown")
            # Pastikan unit lain juga mematikan diri dan menyimpan memori
            self.x.save_memory()
            self.nova.save_memory()
            self.oracle.save_memory()
            return f"[MaverNet]: Memulai pematian sistem...\n{response}"
        else:
            return None # Perintah sistem tidak dikenali

    def route_command_to_unit(self, unit_name, unit_command):
        """
        Mengarahkan perintah ke unit AI spesifik.
        """
        unit = None
        if unit_name.lower() == "zero":
            unit = self.zero
        elif unit_name.lower() == "x":
            unit = self.x
        elif unit_name.lower() == "nova":
            unit = self.nova
        elif unit_name.lower() == "oracle":
            unit = self.oracle

        if unit:
            print(f"[MaverNet]: Mengarahkan perintah '{unit_command}' ke {unit_name}.")
            # Asumsi setiap unit memiliki metode 'interact'
            if hasattr(unit, 'interact'):
                return unit.interact(unit_command)
            else:
                return f"[MaverNet]: Unit {unit_name} tidak memiliki metode 'interact' yang dapat dipanggil."
        else:
            return f"[MaverNet]: Unit '{unit_name}' tidak dikenal."

    def process_overall_command(self, command):
        """
        Pemroses perintah utama untuk seluruh sistem MaverNet dengan AI Agent-like parsing.
        Mencoba perintah sistem, lalu perintah unit dengan parsing fleksibel, atau fallback ke Zero.
        """
        # 1. Coba perintah sistem terlebih dahulu
        system_response = self.process_system_command(command)
        if system_response:
            return system_response

        # 2. Flexible unit targeting dengan berbagai pola
        # Pola 1: "Zero, [command]" atau "X, [command]"
        comma_match = re.match(r'^(zero|x|nova|oracle|x\s*replica)\s*,\s*(.+)', command, re.IGNORECASE)
        if comma_match:
            unit_name = comma_match.group(1).strip()
            unit_command = comma_match.group(2).strip()
            return self.route_command_to_unit(unit_name, unit_command)

        # Pola 2: "Tell Zero to [command]" atau "Ask Nova to [command]"
        tell_match = re.match(r'^(tell|ask|command)\s+(zero|x|nova|oracle|x\s*replica)\s+to\s+(.+)', command, re.IGNORECASE)
        if tell_match:
            unit_name = tell_match.group(2).strip()
            unit_command = tell_match.group(3).strip()
            return self.route_command_to_unit(unit_name, unit_command)

        # Pola 3: "[Unit] [command]" tanpa koma
        unit_direct_match = re.match(r'^(zero|x|nova|oracle|x\s*replica)\s+(.+)', command, re.IGNORECASE)
        if unit_direct_match:
            unit_name = unit_direct_match.group(1).strip()
            unit_command = unit_direct_match.group(2).strip()
            return self.route_command_to_unit(unit_name, unit_command)

        # Pola 4: Deteksi kata kunci untuk auto-routing ke unit yang tepat
        command_lower = command.lower()
        
        # Auto-route berdasarkan kata kunci
        if any(keyword in command_lower for keyword in ['excel', 'csv', 'spreadsheet', 'data automation', 'webhook']):
            print(f"[MaverNet]: Auto-routing to X (Data specialist) based on keywords.")
            return self.x.interact(command)
        elif any(keyword in command_lower for keyword in ['chart', 'graph', 'visual', 'html', 'ui', 'dashboard']):
            print(f"[MaverNet]: Auto-routing to Nova (Visual specialist) based on keywords.")
            return self.nova.interact(command)
        elif any(keyword in command_lower for keyword in ['analyze', 'statistics', 'predict', 'intelligence', 'threat', 'strategic']):
            print(f"[MaverNet]: Auto-routing to Oracle (Analysis specialist) based on keywords.")
            return self.oracle.interact(command)

        # 3. Fallback ke Zero sebagai default
        print(f"[MaverNet]: No specific unit detected, routing to Zero (Default executor).")
        return self.zero.interact(command)


# --- Jalankan MAVERNET Core Orchestrator ---
if __name__ == "__main__":
    system = MaverNetSystem()
    system.system_boot() # Menjalankan proses booting dan inisialisasi

    print("\n--- MAVERNET Core Orchestrator: Sistem Aktif ---")
    print("Ketik perintah. Contoh:")
    print("  - 'System status' (untuk laporan sistem)")
    print("  - 'Zero, jalankan misi [deskripsi]' (untuk Zero)")
    print("  - 'X, baca excel data/sample.xlsx' (untuk X)")
    print("  - 'Nova, buat grafik bar data 10' (untuk Nova)")
    print("  - 'Oracle, analisis teks ini adalah contoh' (untuk Oracle)")
    print("  - 'MaverNet shutdown' (untuk mematikan seluruh sistem)")


    while system.zero.get_status()['current_status'] != "Offline":
        user_input = input("Komandan: ") # Ganti prompt menjadi 'Komandan' atau sesuai keinginan

        # Proses perintah melalui MaverNetSystem
        response = system.process_overall_command(user_input)
        print(response)

        # Cek status Zero lagi setelah perintah diproses (jika ada shutdown)
        if system.zero.get_status()['current_status'] == "Offline":
            break 

    # Perintah simpan dan sync akan dipanggil saat system_boot (awal)
    # dan juga saat MaverNet shutdown (di process_system_command)
    # jadi tidak perlu dipanggil lagi di sini setelah loop

    print("\n[Sistem MAVERNET]: Sistem telah dimatikan sepenuhnya. Sampai jumpa!")

