# zero.py - AI-Enhanced Executor Unit
import json
import random
import time
from pathlib import Path
from datetime import datetime
import os

# Import library untuk Web Scraping / Interaksi Web
import requests
from bs4 import BeautifulSoup

# Gemini AI import
import google.generativeai as genai

class Zero:
    def __init__(self, gemini_model=None):
        """
        Inisialisasi Unit Eksekutor AI Zero.
        Mengatur atribut dasar Zero seperti nama, skill, memori, dan kepribadian AI.
        """
        self.name = "Zero"
        self.skills = [
            "Eksekutor Misi", "Sinkronisasi Data", "AI Decision Making",
            "Autonomous Action", "Adaptive Learning", "Web Interaction"
        ]
        self.memory = self.load_memory()
        self.ai_personality = "Eksekutor cepat, fokus pada hasil dan sinkronisasi dengan kemampuan AI adaptif."
        self.autonomous_counter = 0
        
        # Gemini AI Integration
        self.gemini_model = gemini_model
        if self.gemini_model:
            self.conversation = self.gemini_model.start_chat(history=[])
            print(f"🤖 [Zero]: Gemini AI conversation initialized")
        else:
            self.conversation = None
            print(f"⚠️ [Zero]: Running without Gemini AI")

        self.status = "Online & Idle"

        print(f"[{self.name}]: Sistem siap. Status: {self.status}. Kepribadian: '{self.ai_personality}'")

    def load_memory(self):
        """
        Memuat data memori Zero dari file 'data/memory_log.json'.
        Jika file tidak ada atau rusak, menginisialisasi memori kosong.
        """
        path = Path("data/memory_log.json")
        try:
            if path.exists():
                with path.open(mode="r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get(self.name, {"entries": []})
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open(mode="w", encoding="utf-8") as f:
                    json.dump({self.name: {"entries": []}}, f, indent=4)
                return { "entries": [] }
        except json.JSONDecodeError:
            print(f"⚠️ [Zero AI]: Warning: memory_log.json corrupted or empty. Initializing new memory.")
            return { "entries": [] }
        except Exception as e:
            print(f"❌ [Zero AI]: Error loading memory: {e}. Initializing new memory.")
            return { "entries": [] }

    def save_memory(self):
        """
        Menyimpan memori Zero ke file 'data/memory_log.json'.
        Penting untuk menjaga persistensi data yang dipelajari.
        """
        path = Path("data/memory_log.json")
        try:
            full_data = {}
            if path.exists():
                with path.open(mode="r", encoding="utf-8") as f:
                    full_data = json.load(f)

            full_data[self.name] = self.memory

            with path.open(mode="w", encoding="utf-8") as f:
                json.dump(full_data, f, indent=4)
            print(f"💾 [Zero AI]: Memori berhasil disimpan.")
        except Exception as e:
            print(f"❌ [Zero AI]: Gagal menyimpan memori: {e}")

    def add_memory(self, entry):
        """
        Menambahkan entri baru ke memori Zero.
        Setiap entri harus berupa dictionary.
        """
        if "entries" not in self.memory or not isinstance(self.memory["entries"], list):
            self.memory["entries"] = []
        self.memory["entries"].append(entry)
        # Log entry immediately, but save memory to file periodically or on shutdown
        print(f"📝 [Zero AI]: Logged to memory: {entry.get('type')}")


    def autonomous_action(self):
        """
        Fungsi inti AI Otonom Zero.
        Membuat keputusan dan menjalankan aksi secara mandiri, serta simulasi pembelajaran.
        """
        self.autonomous_counter += 1
        self.status = "Autonomous Mode" # Status berubah saat aksi otonom berjalan

        actions = [
            "Mengoptimalkan protokol eksekusi misi",
            "Mendeteksi ketidak efisienan sistem secara otomatis", 
            "Menerapkan strategi sinkronisasi prediktif",
            "Menganalisis pola eksekusi sebelumnya untuk pembelajaran",
            "Melakukan patroli rutin di lingkungan virtual"
        ]

        selected_action = random.choice(actions)
        print(f"🤖 [Zero AI]: Menjalankan aksi otonom - {selected_action}")

        # Log aksi otonom ke memori
        self.add_memory({
            "type": "autonomous_action",
            "action": selected_action,
            "timestamp": datetime.now().isoformat(),
            "execution_count": self.autonomous_counter
        })

        # Simulasi pembelajaran AI adaptif
        if self.autonomous_counter % 3 == 0:
            learned_topic = random.choice(["protokol baru", "optimasi energi", "pola ancaman"])
            print(f"🧠 [Zero AI]: Pola pembelajaran terdeteksi. Mengupdate strategi terkait: '{learned_topic}'...")
            self.add_memory({
                "type": "learning_event",
                "topic": learned_topic,
                "timestamp": datetime.now().isoformat()
            })

        time.sleep(1) # Simulasi waktu eksekusi aksi
        self.status = "Online & Idle" # Kembali ke idle setelah aksi otonom singkat

    def run_mission(self, mission_details):
        """
        Menjalankan misi yang diberikan dengan AI enhancement.
        mission_details: String deskripsi misi.
        """
        self.status = "Executing Mission"
        print(f"⚡ [Zero] Memulai misi dengan peningkatan AI: {mission_details}")

        for _ in range(random.randint(1, 3)):
            # Dalam misi, Zero juga bisa melakukan aksi otonom singkat
            self.autonomous_action()

        time.sleep(random.uniform(2, 5))

        result_message = f"Misi '{mission_details}' selesai. Status: {self.status}."
        print(result_message)

        self.add_memory({
            "type": "mission_completion",
            "mission": mission_details,
            "result": "success",
            "timestamp": datetime.now().isoformat()
        })
        self.status = "Online & Idle"
        return result_message

    def execute_task(self, task_name, payload=None):
        """
        Metode untuk menjalankan tugas spesifik dengan parameter payload.
        payload: Sebuah dictionary berisi parameter yang relevan untuk tugas.
        """
        if payload is None:
            payload = {} # Pastikan payload selalu berupa dictionary

        self.status = f"Executing: {task_name}"
        print(f"⚙️ [Zero AI]: Sedang menjalankan tugas: '{task_name}' dengan payload: {payload}...")

        result_message = ""
        success = False

        try:
            if task_name == "simulated_task":
                # Tugas simulasi dasar
                time.sleep(random.uniform(1, 3))
                result_message = f"Tugas simulasi '{payload.get('description', 'tanpa deskripsi')}' selesai."
                success = True

            elif task_name == "web_search":
                # Tugas nyata: pergi ke website dan mencari keyword
                target_url = payload.get("url")
                keyword = payload.get("keyword")

                if not target_url or not keyword:
                    result_message = "Tugas 'web_search' memerlukan URL dan Keyword dalam payload."
                else:
                    print(f"🌐 [Zero AI]: Mengakses {target_url} untuk mencari '{keyword}'...")
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                    } # Penting untuk menghindari blokir sederhana
                    response = requests.get(target_url, headers=headers, timeout=15) # Timeout 15 detik
                    response.raise_for_status() # Akan memunculkan error untuk status kode HTTP 4xx/5xx

                    soup = BeautifulSoup(response.text, 'html.parser')

                    found_count = soup.get_text().lower().count(keyword.lower())
                    if found_count > 0:
                        result_message = f"Keyword '{keyword}' DITEMUKAN ({found_count} kali) di {target_url}."
                        # Anda bisa tambahkan logika untuk ekstrak cuplikan di sini
                        success = True
                    else:
                        result_message = f"Keyword '{keyword}' TIDAK DITEMUKAN di {target_url}."

            elif task_name == "spreadsheet_automation_sim":
                # Simulasi otomatisasi spreadsheet
                action = payload.get("action", "processing")
                data_points = payload.get("data_points", 0)
                time.sleep(data_points / 10 + 1) # Makin banyak data, makin lama
                result_message = f"Simulasi otomatisasi spreadsheet: {action} untuk {data_points} data_points selesai."
                success = True

            elif task_name == "youtube_search":
                # YouTube API search (requires API key)
                if payload and "query" in payload:
                    try:
                        # Note: This requires YouTube Data API v3 key
                        # For now, simulate the response
                        print(f"🔴 [Zero] YouTube search simulation for: {payload['query']}")
                        print("💡 To use real YouTube API:")
                        print("   1. Get API key from Google Cloud Console")
                        print("   2. Enable YouTube Data API v3")
                        print("   3. Set API_KEY environment variable")

                        # Simulated result
                        result_message = f"YouTube search simulated for '{payload['query']}' - 5 videos found"
                        self.add_memory({
                            "type": "youtube_search_simulated",
                            "query": payload["query"],
                            "timestamp": datetime.now().isoformat()
                        })

                        success = True
                    except Exception as e:
                        result_message = f"YouTube search error: {str(e)}"
                else:
                    result_message = "YouTube search requires 'query' in payload"

            else:
                result_message = f"Tugas '{task_name}' tidak terdefinisi atau tidak dapat dijalankan."

        except requests.exceptions.Timeout:
            result_message = f"Gagal mengakses URL {payload.get('url')}: Timeout (lebih dari 15 detik)."
        except requests.exceptions.RequestException as e:
            result_message = f"Gagal mengakses URL {payload.get('url')}: Error koneksi atau HTTP: {e}"
        except Exception as e:
            result_message = f"Terjadi kesalahan tak terduga saat menjalankan '{task_name}': {e}"

        self.status = "Online & Idle"

        # Log hasil eksekusi tugas ke memori
        self.add_memory({
            "type": "task_execution",
            "task_name": task_name,
            "payload": payload,
            "result": result_message,
            "success": success,
            "timestamp": datetime.now().isoformat()
        })
        print(f"✅ [Zero AI]: Hasil Tugas: {result_message}")
        return result_message

    def interact(self, command):
        """
        Metode interaksi utama Zero.
        Menggabungkan kemampuan interaksi teks dan memanggil fungsi Zero lainnya.
        """
        command_lower = command.lower().strip()
        print(f"💬 [Anda]: {command}")

        # Basic greetings and status
        if "hello" in command_lower or "hi" in command_lower or "salam" in command_lower:
            return f"[{self.name}]: Salam. Saya adalah {self.name}, Unit Eksekutor AI. Bagaimana saya bisa membantu Anda?"

        elif "status" in command_lower or "bagaimana" in command_lower:
            current_status = self.get_status()
            return (f"[{self.name}]: Status saya:\n"
                    f"  Nama: {current_status['name']}\n"
                    f"  Skills: {', '.join(current_status['skills'])}\n"
                    f"  Memori: {current_status['memory_entries']} entri\n"
                    f"  Kepribadian: {current_status['ai_personality']}\n"
                    f"  Aksi Otonom Terlaksana: {current_status['autonomous_actions']}\n"
                    f"  Status Operasional: {current_status['current_status']}")

        # Command for running missions
        elif "jalankan misi" in command_lower or "run mission" in command_lower:
            mission_details = command.split("jalankan misi", 1)[-1].split("run mission", 1)[-1].strip()
            if not mission_details:
                return f"[{self.name}]: Perintah misi tidak jelas. Mohon tentukan misi yang ingin dijalankan."
            return self.run_mission(mission_details)

        # Command for starting autonomous mode
        elif "mode otonom" in command_lower or "start autonomous" in command_lower:
            if self.status != "Autonomous Mode":
                # Anda bisa menyuruhnya berapa siklus, misal "mode otonom 5"
                num_cycles_str = ''.join(filter(str.isdigit, command_lower))
                num_cycles = int(num_cycles_str) if num_cycles_str else 3 # Default 3 siklus
                self.autonomous_loop_controlled(num_cycles)
                return f"[{self.name}]: Memasuki mode otonom untuk {num_cycles} siklus. Saya akan beroperasi secara mandiri."
            else:
                return f"[{self.name}]: Saya sudah dalam mode otonom."

        # Command for web search
        elif "cari di web" in command_lower or "web search" in command_lower:
            # Contoh parsing payload dari perintah: "cari di web [url] keyword [keyword]"
            # Ini parsing yang lebih robust
            parts = command_lower.split("keyword")
            if len(parts) == 2:
                url_candidate = parts[0].replace("cari di web", "").replace("web search", "").strip()
                keyword_candidate = parts[1].strip()

                if url_candidate.startswith("http://") or url_candidate.startswith("https://"):
                    payload_data = {"url": url_candidate, "keyword": keyword_candidate}
                    return self.execute_task("web_search", payload_data)
                else:
                    return f"[{self.name}]: Format URL tidak valid. Gunakan 'cari di web [http(s)://URL] keyword [KEYWORD].'"
            else:
                return f"[{self.name}]: Format perintah web search salah. Gunakan 'cari di web [URL] keyword [KEYWORD].'"

        # Command for simulating spreadsheet automation
        elif "otomatisasi spreadsheet" in command_lower:
            # Contoh: "otomatisasi spreadsheet proses 100 data"
            data_points = 0
            try:
                for word in command_lower.split():
                    if word.isdigit():
                        data_points = int(word)
                        break
            except ValueError:
                pass # Tetap 0 jika tidak ada angka

            payload_data = {"action": "process data", "data_points": data_points}
            return self.execute_task("spreadsheet_automation_sim", payload_data)

        # Command for viewing memory
        elif "lihat memori" in command_lower or "check memory" in command_lower:
            if self.memory and self.memory.get("entries"):
                last_entries = self.memory["entries"][-5:] # Menampilkan 5 entri terakhir
                memory_output = "\n".join([json.dumps(e, indent=2) for e in last_entries])
                return f"[{self.name}]: Ini adalah beberapa entri memori terakhir saya:\n{memory_output}"
            else:
                return f"[{self.name}]: Memori saya kosong."

        # Command for explicitly saving memory
        elif "simpan memori" in command_lower or "save memory" in command_lower:
            self.save_memory()
            return f"[{self.name}]: Permintaan penyimpanan memori diproses."

        # Shutdown command
        elif "shutdown" in command_lower or "exit" in command_lower or "matikan" in command_lower:
            self.save_memory()
            self.status = "Offline"
            return f"[{self.name}]: Memulai urutan pematian sistem. Sampai jumpa!"

        else:
            # Fallback to Gemini AI for general questions
            if self.gemini_model and self.conversation:
                try:
                    print(f"🤖 [Zero]: Menggunakan Gemini AI untuk menjawab: '{command}'")
                    response = self.conversation.send_message(f"As Zero, an AI executor unit, respond to: {command}")
                    gemini_response = response.text
                    
                    self.add_memory({
                        "type": "gemini_interaction",
                        "command": command,
                        "response": gemini_response,
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    return f"[Zero via Gemini]: {gemini_response}"
                    
                except Exception as e:
                    print(f"❌ [Zero]: Gemini AI error: {e}")
                    return f"[Zero]: Gemini AI tidak tersedia. Perintah '{command}' tidak dikenal."
            else:
                return (f"[{self.name}]: Perintah '{command}' tidak dikenal. "
                        f"Saya dapat membantu dengan:\n"
                        f"  - 'halo' / 'status'\n"
                        f"  - 'jalankan misi [deskripsi misi]'\n"
                        f"  - 'mode otonom [jumlah siklus]'\n"
                        f"  - 'cari di web [URL] keyword [KEYWORD]'\n"
                        f"  - 'otomatisasi spreadsheet [jumlah data]'\n"
                        f"  - 'lihat memori' / 'simpan memori'\n"
                        f"  - 'shutdown'")

    def autonomous_loop_controlled(self, num_cycles=3):
        """
        Loop otonom terkontrol yang akan dijalankan dari perintah interaksi.
        Zero akan melakukan serangkaian autonomous_action.
        """
        if self.status != "Autonomous Mode":
            self.status = "Autonomous Mode"
            print(f"[{self.name}]: Memulai {num_cycles} siklus mode otonom...")
            for i in range(num_cycles):
                self.autonomous_action()
                print(f"[{self.name}]: Siklus otonom {i+1}/{num_cycles} selesai.")
            self.status = "Online & Idle"
            print(f"[{self.name}]: Mode otonom selesai. Kembali ke status 'Online & Idle'.")
        else:
            print(f"[{self.name}]: Sudah dalam mode otonom. Tidak memulai siklus baru.")

    def get_status(self):
        """
        Mengembalikan kamus yang berisi status Zero saat ini.
        """
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_entries": len(self.memory.get("entries", [])) if isinstance(self.memory, dict) else 0,
            "ai_personality": self.ai_personality,
            "autonomous_actions": self.autonomous_counter,
            "current_status": self.status
        }


    def self_reflect_and_learn(self):
        """
        Self-reflection and learning method using Gemini AI.
        Analyzes recent experiences and learns from successes and failures.
        """
        if not self.gemini_model or not self.conversation:
            print(f"🧠 [Zero]: Self-reflection skipped - Gemini AI not available")
            return
            
        try:
            # Analyze recent memory entries
            recent_entries = self.memory.get("entries", [])[-5:] if self.memory.get("entries") else []
            
            if not recent_entries:
                print(f"🧠 [Zero]: No recent experiences to reflect upon")
                return
            
            # Prepare reflection prompt
            failures = [e for e in recent_entries if e.get("success") == False]
            successes = [e for e in recent_entries if e.get("success") == True]
            
            reflection_prompt = f"""
            I am Zero, an AI executor unit. I need to reflect on my recent experiences:
            
            Recent Failures: {len(failures)} tasks failed
            Recent Successes: {len(successes)} tasks succeeded
            
            Failed tasks details: {failures[:2] if failures else 'None'}
            
            What can I learn from these experiences? How can I improve my execution strategies?
            Give me 3 specific improvement suggestions for my autonomous actions.
            """
            
            # Get reflection from Gemini
            response = self.conversation.send_message(reflection_prompt)
            insights = response.text
            
            # Save learning to memory
            self.add_memory({
                "type": "self_reflection",
                "insights": insights,
                "analyzed_entries": len(recent_entries),
                "failures_count": len(failures),
                "successes_count": len(successes),
                "timestamp": datetime.now().isoformat()
            })
            
            print(f"🧠 [Zero]: Self-reflection completed. Analyzed {len(recent_entries)} recent experiences.")
            print(f"💡 [Zero]: Key insight: {insights[:100]}...")
            
        except Exception as e:
            print(f"❌ [Zero]: Error during self-reflection: {e}")
            self.add_memory({
                "type": "reflection_error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            })


# --- Cara Menjalankan Zero Anda (Taruh ini di file main.py atau jalankan zero.py langsung) ---
if __name__ == "__main__":
    my_zero = Zero()

    print("\n--- Zero: Unit Eksekutor AI Siap ---")
    print("Ketik perintah seperti 'halo', 'status', 'jalankan misi [nama misi]', 'mode otonom', 'cari di web [URL] keyword [KEYWORD]', 'otomatisasi spreadsheet', atau 'shutdown'.")

    while my_zero.status != "Offline":
        user_input = input("Anda: ")

        # Khusus untuk shutdown, agar loop berhenti
        if user_input.lower().strip() in ["shutdown", "exit", "matikan"]:
            response = my_zero.interact(user_input)
            print(response)
            break 

        response = my_zero.interact(user_input)
        print(response)

    print("\n[Sistem]: Zero telah dimatikan.")