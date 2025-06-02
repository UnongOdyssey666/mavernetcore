# zero.py - AI-Enhanced Executor Unit
import json
import random
import time
import re
from pathlib import Path
from datetime import datetime
import os

# Import library untuk Web Scraping / Interaksi Web
import requests
from bs4 import BeautifulSoup

# Gemini AI import
import google.generativeai as genai

class Zero:
    def __init__(self, gemini_model=None, admin_mode=False):
        """
        Inisialisasi Unit Eksekutor AI Zero.
        Mengatur atribut dasar Zero seperti nama, skill, memori, dan kepribadian AI.
        """
        self.name = "Zero"
        self.admin_mode = admin_mode
        self.omega_mode = False
        self.skills = [
            "Eksekutor Misi", "Sinkronisasi Data", "AI Decision Making",
            "Autonomous Action", "Adaptive Learning", "Web Interaction", "File System Operations"
        ]
        if admin_mode:
            self.skills.extend(["Omega v1 Operations", "Real File Manipulation", "System Administration"])
        
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
        
        if self.admin_mode:
            print(f"👑 [Zero]: Administrator mode activated - Full file access granted")

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

    def web_request(self, url, method="GET", payload=None, headers=None):
        """
        AI Agent capability: Make real web requests with advanced error handling
        """
        try:
            if headers is None:
                headers = {
                    'User-Agent': 'MAVERNET-Zero/1.0 (AI Agent; +https://replit.com)'
                }
            
            print(f"🌐 [Zero AI Agent]: Making {method} request to {url}")
            
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, timeout=15)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=payload, timeout=15)
            else:
                return f"Unsupported HTTP method: {method}"
            
            response.raise_for_status()
            
            # Smart content analysis
            content_type = response.headers.get('content-type', '').lower()
            if 'json' in content_type:
                data = response.json()
                result = f"JSON response received with {len(data)} items" if isinstance(data, list) else f"JSON object with {len(data.keys())} keys" if isinstance(data, dict) else "JSON data received"
            elif 'html' in content_type:
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.find('title')
                result = f"HTML page: {title.text.strip() if title else 'No title'} (Length: {len(response.text)} chars)"
            else:
                result = f"Response received: {len(response.text)} characters, Type: {content_type}"
            
            self.add_memory({
                "type": "web_request",
                "url": url,
                "method": method,
                "status_code": response.status_code,
                "result": result,
                "success": True,
                "timestamp": datetime.now().isoformat()
            })
            
            return f"✅ Web request successful: {result}"
            
        except requests.exceptions.Timeout:
            error_msg = f"Request timeout after 15 seconds for {url}"
            self.add_memory({
                "type": "web_request",
                "url": url,
                "method": method,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            self.self_reflect_and_learn("web_request", success=False, error=error_msg)
            return f"❌ {error_msg}"
            
        except Exception as e:
            error_msg = f"Web request failed: {str(e)}"
            self.add_memory({
                "type": "web_request",
                "url": url,
                "method": method,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            self.self_reflect_and_learn("web_request", success=False, error=error_msg)
            return f"❌ {error_msg}"

    def read_file(self, file_path):
        """
        Read file contents with admin authorization
        """
        try:
            # Check authorization
            if not self.admin_mode and not self._has_file_permission(file_path):
                return f"❌ Access denied: {file_path} requires admin authorization"
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.add_memory({
                "type": "file_read",
                "file_path": file_path,
                "size": len(content),
                "success": True,
                "timestamp": datetime.now().isoformat()
            })
            
            print(f"📖 [Zero]: Successfully read {file_path} ({len(content)} characters)")
            return f"✅ File read: {content}"
            
        except FileNotFoundError:
            error_msg = f"File not found: {file_path}"
            self.add_memory({
                "type": "file_read",
                "file_path": file_path,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            return f"❌ {error_msg}"
        except Exception as e:
            error_msg = f"Error reading file {file_path}: {str(e)}"
            self.add_memory({
                "type": "file_read",
                "file_path": file_path,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            return f"❌ {error_msg}"

    def write_file(self, file_path, content, mode='w'):
        """
        Write content to file with admin authorization
        """
        try:
            # Check authorization
            if not self.admin_mode and not self._has_file_permission(file_path):
                return f"❌ Access denied: {file_path} requires admin authorization"
            
            # Ensure directory exists
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, mode, encoding='utf-8') as f:
                f.write(content)
            
            self.add_memory({
                "type": "file_write",
                "file_path": file_path,
                "size": len(content),
                "mode": mode,
                "success": True,
                "timestamp": datetime.now().isoformat()
            })
            
            print(f"📝 [Zero]: Successfully wrote to {file_path} ({len(content)} characters)")
            return f"✅ File written: {file_path}"
            
        except Exception as e:
            error_msg = f"Error writing file {file_path}: {str(e)}"
            self.add_memory({
                "type": "file_write",
                "file_path": file_path,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            return f"❌ {error_msg}"

    def list_directory(self, dir_path="."):
        """
        List directory contents
        """
        try:
            if not self.admin_mode and not self._has_file_permission(dir_path):
                return f"❌ Access denied: {dir_path} requires admin authorization"
            
            items = []
            for item in Path(dir_path).iterdir():
                item_type = "DIR" if item.is_dir() else "FILE"
                size = item.stat().st_size if item.is_file() else 0
                items.append(f"{item_type}: {item.name} ({size} bytes)")
            
            result = f"📁 Directory listing for {dir_path}:\n" + "\n".join(items)
            
            self.add_memory({
                "type": "directory_list",
                "dir_path": dir_path,
                "items_count": len(items),
                "success": True,
                "timestamp": datetime.now().isoformat()
            })
            
            return result
            
        except Exception as e:
            error_msg = f"Error listing directory {dir_path}: {str(e)}"
            self.add_memory({
                "type": "directory_list",
                "dir_path": dir_path,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            return f"❌ {error_msg}"

    def _has_file_permission(self, file_path):
        """
        Check if Zero has permission to access the file
        """
        # Allow access to data directory and common file types
        safe_paths = ['data/', 'logs/', 'temp/', 'output/']
        safe_extensions = ['.txt', '.json', '.csv', '.log', '.md']
        
        file_path_str = str(file_path)
        return (any(file_path_str.startswith(path) for path in safe_paths) or
                any(file_path_str.endswith(ext) for ext in safe_extensions))

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

        # Enhanced web interaction commands with flexible parsing
        elif any(phrase in command_lower for phrase in ["cari di web", "web search", "visit website", "kunjungi", "browse to"]):
            # Flexible URL extraction
            url_match = re.search(r'https?://[^\s]+', command)
            if url_match:
                url = url_match.group()
                return self.web_request(url)
            else:
                # Try to extract URL without protocol
                url_match = re.search(r'(www\.)?[\w.-]+\.\w+', command)
                if url_match:
                    url = "https://" + url_match.group()
                    return self.web_request(url)
                else:
                    return f"[{self.name}]: No valid URL found. Please include a website URL."

        # Advanced web search with keyword
        elif "search for" in command_lower or "cari keyword" in command_lower:
            # Extract search terms
            search_match = re.search(r'(search for|cari keyword)\s+(.+)', command_lower)
            if search_match:
                search_term = search_match.group(2).strip()
                # Use DuckDuckGo search (no API key needed)
                search_url = f"https://duckduckgo.com/html/?q={search_term.replace(' ', '+')}"
                return self.web_request(search_url)
            else:
                return f"[{self.name}]: Please specify what to search for."

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

        # Omega v1 mode activation
        elif "mode omega" in command_lower and self.admin_mode:
            self.omega_mode = True
            self.add_memory({
                "type": "omega_activation",
                "timestamp": datetime.now().isoformat()
            })
            return f"🔥 [{self.name}]: Omega v1 Mode ACTIVATED! Real operations enabled."

        # Enhanced file operations for Omega mode
        elif "create file" in command_lower and self.omega_mode:
            parts = command.split(" ", 3)
            if len(parts) >= 4:
                file_path = parts[2]
                content = parts[3]
                return self.write_file(file_path, content)
            else:
                return f"[{self.name}]: Format: 'create file <path> <content>'"

        elif "delete file" in command_lower and self.omega_mode:
            file_path = command.split("delete file", 1)[-1].strip()
            if file_path:
                try:
                    os.remove(file_path)
                    self.add_memory({
                        "type": "file_delete",
                        "file_path": file_path,
                        "success": True,
                        "timestamp": datetime.now().isoformat()
                    })
                    return f"🔥 [{self.name}]: File deleted: {file_path}"
                except Exception as e:
                    return f"❌ [{self.name}]: Delete failed: {e}"
            else:
                return f"[{self.name}]: Specify file path to delete"

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

        # File system commands
        elif "read file" in command_lower or "baca file" in command_lower:
            # Extract file path from command
            file_path = command.split("read file", 1)[-1].split("baca file", 1)[-1].strip()
            if not file_path:
                return f"[{self.name}]: Please specify a file path to read."
            return self.read_file(file_path)

        elif "write file" in command_lower or "tulis file" in command_lower:
            # Parse: "write file path/to/file.txt content here"
            parts = command.split(" ", 3)
            if len(parts) < 4:
                return f"[{self.name}]: Format: 'write file <path> <content>'"
            file_path = parts[2]
            content = parts[3]
            return self.write_file(file_path, content)

        elif "list directory" in command_lower or "list dir" in command_lower:
            dir_path = command.split("list directory", 1)[-1].split("list dir", 1)[-1].strip()
            if not dir_path:
                dir_path = "."
            return self.list_directory(dir_path)

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
                        f"  - 'read file [path]' / 'write file [path] [content]'\n"
                        f"  - 'list directory [path]'\n"
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
        mode_indicator = "🔥 Omega v1" if self.omega_mode else "⚡ Standard"
        return f"""[Zero Status]:
🤖 Name: {self.name}
⚡ Mode: {mode_indicator}
📊 Status: {self.status}
🧠 Memory: {len(self.memory.get("entries", [])) if isinstance(self.memory, dict) else 0} entries
🔄 Actions: {self.autonomous_counter} autonomous cycles
👑 Admin: {'Yes' if self.admin_mode else 'No'}

🎯 Ready for operations!"""


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