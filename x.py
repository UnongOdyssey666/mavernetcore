# x.py - AI-Enhanced Data Bridge & Automation Unit
import json
import random
import time
import os
from pathlib import Path
from datetime import datetime
import re # Tambahkan ini untuk parsing perintah Regex di interact()

# Gemini AI import
import google.generativeai as genai

class XReplica:
    def __init__(self, gemini_model=None):
        self.name = "X Replica"
        self.skills = [
            "Otomatisasi Spreadsheet (Excel)", "Bridge Data", "Webhook Handler",
            "Log Analyzer", "AI Data Processing", "Self-Reflection" # Menyesuaikan skill
        ]
        # Pastikan folder 'data' ada sebelum mencoba memuat memori
        os.makedirs("data", exist_ok=True)
        self.memory = self.load_memory()
        self.ai_personality = "Stabil dan logis, arsitek sistem log dan data automation specialist"
        self.autonomous_counter = 0

        # Gemini AI Integration
        self.gemini_model = gemini_model
        if self.gemini_model:
            self.conversation = self.gemini_model.start_chat(history=[])
            print(f"🤖 [{self.name}]: Gemini AI conversation initialized.")
        else:
            self.conversation = None
            print(f"⚠️ [{self.name}]: Running without Gemini AI. Some advanced features might be limited.")

        # Menghapus inisialisasi gsheet_client
        self.gsheet_client = None # Set ke None karena tidak digunakan sementara

        self.status = "Online & Ready"
        print(f"[{self.name}]: Data bridge systems online. Personality: '{self.ai_personality}'")

    def load_memory(self):
        # Memori unik untuk setiap unit
        path = Path(f"data/{self.name.lower().replace(' ', '_')}_memory_log.json")
        try:
            if path.exists():
                with path.open(mode="r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get(self.name, {"entries": []})
            else:
                # Jika file belum ada, buat struktur dasar
                path.parent.mkdir(parents=True, exist_ok=True) # Memastikan folder 'data' ada
                with path.open(mode="w", encoding="utf-8") as f:
                    json.dump({self.name: {"entries": []}}, f, indent=4)
                return {"entries": []}
        except json.JSONDecodeError:
            print(f"❌ [{self.name}]: Corrupted memory_log.json. Initializing new memory.")
            return {"entries": []}
        except Exception as e:
            print(f"❌ [{self.name}]: Error loading memory: {e}. Initializing new memory.")
            return {"entries": []}

    def save_memory(self):
        # Memori unik untuk setiap unit
        path = Path(f"data/{self.name.lower().replace(' ', '_')}_memory_log.json")
        try:
            full_data = {}
            if path.exists():
                with path.open(mode="r", encoding="utf-8") as f:
                    full_data = json.load(f)

            full_data[self.name] = self.memory

            with path.open(mode="w", encoding="utf-8") as f:
                json.dump(full_data, f, indent=4)
            print(f"💾 [{self.name}]: Memori berhasil disimpan.")
        except Exception as e:
            print(f"❌ [{self.name}]: Gagal menyimpan memori: {e}")

    def add_memory(self, entry):
        if "entries" not in self.memory or not isinstance(self.memory["entries"], list):
            self.memory["entries"] = []
        self.memory["entries"].append(entry)
        # Tidak langsung print 'Logged to memory' agar tidak terlalu banyak log.
        # Print hanya untuk pesan penting.

    def autonomous_action(self):
        """AI Agent: Autonomous data processing and automation actions"""
        self.autonomous_counter += 1

        actions = [
            "Optimizing data flow architectures",
            "Monitoring webhook integration patterns", 
            "Analyzing log structures for efficiency",
            "Implementing predictive data automation",
            "Scanning for data consistency issues"
        ]

        selected_action = random.choice(actions)
        print(f"🤖 [{self.name} AI]: Executing autonomous action - {selected_action}")

        self.add_memory({
            "type": "autonomous_action",
            "action": selected_action,
            "timestamp": datetime.now().isoformat(),
            "execution_count": self.autonomous_counter
        })

        # Trigger self-reflection after every 3 actions
        if self.autonomous_counter % 3 == 0:
            print(f"🔗 [{self.name} AI]: Data pattern analysis complete, updating automation protocols...")
            self.self_reflect_and_learn() # Panggil refleksi diri

    def read_excel_data(self, file_path):
        """Read data from Excel file using openpyxl"""
        try:
            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active

            data = []
            for row in sheet.iter_rows(values_only=True):
                if any(cell is not None for cell in row):  # Skip empty rows
                    data.append(list(row))

            workbook.close()

            self.add_memory({
                "type": "excel_read",
                "file_path": file_path,
                "rows_read": len(data),
                "success": True,
                "timestamp": datetime.now().isoformat()
            })

            print(f"📊 [{self.name}]: Successfully read {len(data)} rows from {file_path}")
            return data

        except FileNotFoundError:
            error_msg = f"Failed to read Excel file {file_path}: File not found."
            print(f"❌ [{self.name}]: {error_msg}")

            self.add_memory({
                "type": "excel_read",
                "file_path": file_path,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })

            self.self_reflect_and_learn("read_excel_data", success=False, error=error_msg) # Panggil refleksi pada kegagalan
            return None
        except Exception as e:
            error_msg = f"Failed to read Excel file {file_path}: {str(e)}"
            print(f"❌ [{self.name}]: {error_msg}")

            self.add_memory({
                "type": "excel_read",
                "file_path": file_path,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })

            self.self_reflect_and_learn("read_excel_data", success=False, error=error_msg) # Panggil refleksi pada kegagalan
            return None

    def write_excel_data(self, file_path, data):
        """Write data to Excel file using openpyxl"""
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active

            for row_idx, row_data in enumerate(data, 1):
                for col_idx, value in enumerate(row_data, 1):
                    sheet.cell(row=row_idx, column=col_idx, value=value)

            # Ensure directory exists
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            workbook.save(file_path)
            workbook.close()

            self.add_memory({
                "type": "excel_write",
                "file_path": file_path,
                "rows_written": len(data),
                "success": True,
                "timestamp": datetime.now().isoformat()
            })

            print(f"💾 [{self.name}]: Successfully wrote {len(data)} rows to {file_path}")
            return True

        except Exception as e:
            error_msg = f"Failed to write Excel file {file_path}: {str(e)}"
            print(f"❌ [{self.name}]: {error_msg}")

            self.add_memory({
                "type": "excel_write",
                "file_path": file_path,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })

            self.self_reflect_and_learn("write_excel_data", success=False, error=error_msg) # Panggil refleksi pada kegagalan
            return False

    def analyze_csv_log(self, file_path):
        """Analyze CSV log files for patterns"""
        try:
            df = pd.read_csv(file_path)

            analysis = {
                "total_rows": len(df),
                "total_columns": len(df.columns),
                "columns": list(df.columns),
                "missing_values": df.isnull().sum().to_dict(),
                "summary": df.describe().to_dict() if df.select_dtypes(include=[float, int]).shape[1] > 0 else {}
            }

            self.add_memory({
                "type": "csv_analysis",
                "file_path": file_path,
                "analysis": analysis,
                "success": True,
                "timestamp": datetime.now().isoformat()
            })

            print(f"📈 [{self.name}]: CSV analysis completed for {file_path}")
            print(f"   Rows: {analysis['total_rows']}, Columns: {analysis['total_columns']}")

            return analysis

        except FileNotFoundError:
            error_msg = f"Failed to analyze CSV {file_path}: File not found."
            print(f"❌ [{self.name}]: {error_msg}")
            self.add_memory({
                "type": "csv_analysis",
                "file_path": file_path,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            self.self_reflect_and_learn("analyze_csv_log", success=False, error=error_msg)
            return None
        except Exception as e:
            error_msg = f"Failed to analyze CSV {file_path}: {str(e)}"
            print(f"❌ [{self.name}]: {error_msg}")

            self.add_memory({
                "type": "csv_analysis",
                "file_path": file_path,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })

            self.self_reflect_and_learn("analyze_csv_log", success=False, error=error_msg)
            return None

    def self_reflect_and_learn(self, task_context="", success=None, error=None):
        """
        Self-reflection and learning using Gemini AI.
        Called after autonomous actions or task execution (especially on failure).
        """
        if not self.gemini_model or not self.conversation:
            # print(f"🧠 [{self.name}]: Self-reflection skipped - Gemini AI not available.") # Commented for less noise
            return

        try:
            # Mengambil entri memori terbaru untuk analisis konteks
            recent_entries = self.memory.get("entries", [])[-5:]

            reflection_prompt = f"Saya {self.name}, seorang spesialis otomatisasi data. Saya perlu merenungkan pengalaman saya baru-baru ini.\n\n"

            if success is not None:
                if success:
                    reflection_prompt += f"Saya baru saja berhasil menyelesaikan tugas '{task_context}'.\n"
                else:
                    reflection_prompt += f"Saya baru saja GAGAL menyelesaikan tugas '{task_context}'. Error yang terjadi: {error}.\n"

            reflection_prompt += "\nBerikut adalah beberapa riwayat operasi terakhir saya:\n"
            for entry in recent_entries:
                reflection_prompt += f"- {entry.get('type')}: {entry.get('action') or entry.get('task_name') or entry.get('mission') or entry.get('prompt')}. Hasil: {entry.get('result') or ('Sukses' if entry.get('success') else 'Gagal')}. Timestamp: {entry.get('timestamp')}\n"

            reflection_prompt += f"\nSebagai spesialis data, apa yang bisa saya pelajari dari pengalaman ini? Bagaimana saya bisa meningkatkan strategi otomatisasi spreadsheet dan pemrosesan data saya? Berikan 3 poin peningkatan teknis spesifik. Fokus pada pembelajaran dari kegagalan jika ada."

            # Meminta Gemini untuk memberikan insight
            response = self.conversation.send_message(reflection_prompt)
            insights = response.text

            # Menyimpan pembelajaran ke memori unit
            self.add_memory({
                "type": "self_reflection",
                "insights": insights,
                "context": task_context,
                "success_status": success,
                "error_details": error,
                "analyzed_entries_count": len(recent_entries),
                "timestamp": datetime.now().isoformat()
            })

            print(f"🧠 [{self.name}]: Refleksi diri selesai. Menganalisis {len(recent_entries)} operasi data.")
            print(f"💡 [{self.name}]: Insight kunci: {insights[:150]}...") # Menampilkan sebagian kecil insight

        except Exception as e:
            print(f"❌ [{self.name}]: Error selama refleksi diri dengan Gemini: {e}")

    def autonomous_loop_controlled(self, num_cycles=3):
        """
        Loop otonom terkontrol yang akan menjalankan serangkaian autonomous_action.
        """
        self.status = "Autonomous Mode"
        print(f"[{self.name}]: Memulai {num_cycles} siklus mode otonom data processing...")
        for i in range(num_cycles):
            self.autonomous_action()
            time.sleep(1) # Jeda antar aksi
        self.status = "Online & Ready"
        print(f"[{self.name}]: Mode otonom selesai. Kembali ke status '{self.status}'.")

    def execute_task(self, task_name, payload=None):
        """
        Metode untuk menjalankan tugas spesifik untuk XReplica (misal: otomatisasi spreadsheet).
        """
        if payload is None:
            payload = {}
        self.status = f"Executing: {task_name}"
        print(f"📊 [{self.name} AI]: Sedang menjalankan tugas: '{task_name}' dengan payload: {payload}...")

        result_message = ""
        success = False

        try:
            if task_name == "read_excel":
                file_path = payload.get("file_path")
                if file_path:
                    data = self.read_excel_data(file_path)
                    if data:
                        result_message = f"Berhasil membaca {len(data)} baris dari {file_path}."
                        success = True
                    else:
                        result_message = f"Gagal membaca Excel file {file_path}."
                else:
                    result_message = "Tugas 'read_excel' memerlukan 'file_path'."

            elif task_name == "write_excel":
                file_path = payload.get("file_path")
                data_to_write = payload.get("data")
                if file_path and data_to_write:
                    success = self.write_excel_data(file_path, data_to_write)
                    result_message = f"Berhasil menulis {'berhasil' if success else 'gagal'} ke {file_path}."
                else:
                    result_message = "Tugas 'write_excel' memerlukan 'file_path' dan 'data'."

            elif task_name == "analyze_csv":
                file_path = payload.get("file_path")
                if file_path:
                    analysis_result = self.analyze_csv_log(file_path)
                    if analysis_result:
                        result_message = f"Analisis CSV {file_path} selesai. Ditemukan {analysis_result['total_rows']} baris."
                        success = True
                    else:
                        result_message = f"Gagal menganalisis CSV {file_path}."
                else:
                    result_message = "Tugas 'analyze_csv' memerlukan 'file_path'."

            # Menghapus bagian Google Sheets untuk sementara
            # elif task_name == "read_google_sheet":
            #     result_message = "Google Sheets functionality is temporarily disabled."
            #     success = False
            # elif task_name == "write_google_sheet":
            #     result_message = "Google Sheets functionality is temporarily disabled."
            #     success = False

            else:
                result_message = f"Tugas '{task_name}' tidak terdefinisi untuk {self.name}."

        except Exception as e:
            result_message = f"Terjadi kesalahan tak terduga saat menjalankan '{task_name}': {e}"

        self.status = "Online & Idle"
        self.add_memory({
            "type": "task_execution",
            "task_name": task_name,
            "payload": payload,
            "result": result_message,
            "success": success,
            "timestamp": datetime.now().isoformat()
        })
        print(f"✅ [{self.name} AI]: Hasil Tugas: {result_message}")
        return result_message

    def interact(self, command):
        """Handle commands sent to X Replica"""
        command_lower = command.lower().strip()
        print(f"💬 [User to {self.name}]: {command}")

        # --- Perintah khusus XReplica (prioritas tinggi) ---
        if "hello" in command_lower or "hi" in command_lower or "salam" in command_lower:
            return f"[{self.name}]: Salam. Saya {self.name}, unit automation dan data bridge. Bagaimana saya bisa membantu dengan data Anda?"

        elif "status" in command_lower:
            status = self.get_status()
            return (f"[{self.name}]: Status data bridge:\n"
                    f"  Skills: {', '.join(status['skills'])}\n"
                    f"  Memory Entries: {status['memory_entries']}\n"
                    f"  Autonomous Actions: {status['autonomous_actions']}\n"
                    f"  Status: {self.status}")

        elif "read excel" in command_lower or "baca excel" in command_lower:
            match = re.search(r"(read excel|baca excel)\s+([\w\d/\\_.-]+\.xlsx)", command_lower)
            if match:
                file_path = match.group(2)
                return self.execute_task("read_excel", {"file_path": file_path})
            else:
                return f"[{self.name}]: Penggunaan: 'read excel [file_path.xlsx]'"

        elif "write excel" in command_lower or "tulis excel" in command_lower:
            match = re.search(r"(write excel|tulis excel)\s+([\w\d/\\_.-]+\.xlsx)", command_lower)
            if match:
                file_path = match.group(2)
                # Generate sample data for demonstration
                sample_data = [
                    ["ID", "Name", "Value", "Timestamp"],
                    [1, "AI Generated Data 1", 100, datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                    [2, "AI Generated Data 2", 200, datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                    [3, "AI Generated Data 3", 300, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                ]
                return self.execute_task("write_excel", {"file_path": file_path, "data": sample_data})
            else:
                return f"[{self.name}]: Penggunaan: 'write excel [file_path.xlsx]'"

        elif "analyze csv" in command_lower:
            match = re.search(r"(analyze csv|analisis csv)\s+([\w\d/\\_.-]+\.csv)", command_lower)
            if match:
                file_path = match.group(2)
                return self.execute_task("analyze_csv", {"file_path": file_path})
            else:
                return f"[{self.name}]: Penggunaan: 'analyze csv [file_path.csv]'"

        elif "mode otonom" in command_lower or "autonomous mode" in command_lower:
            match = re.search(r"(mode otonom|autonomous mode)\s*(\d*)", command_lower)
            num_cycles = 3
            if match and match.group(2):
                num_cycles = int(match.group(2))

            self.autonomous_loop_controlled(num_cycles)
            return f"[{self.name}]: Menyelesaikan {num_cycles} siklus pemrosesan data otonom."

        elif "self reflect" in command_lower or "refleksi diri" in command_lower:
            self.self_reflect_and_learn()
            return f"[{self.name}]: Memulai proses refleksi diri..."

        else:
            # Fallback to Gemini AI for general questions
            if self.gemini_model and self.conversation:
                try:
                    print(f"🤖 [{self.name}]: Menggunakan Gemini AI untuk: '{command}'")
                    # Tambahkan persona ke prompt Gemini
                    gemini_prompt = f"Sebagai {self.name}, seorang {self.ai_personality}, tanggapi perintah berikut: {command}"
                    response = self.conversation.send_message(gemini_prompt)
                    gemini_response = response.text

                    self.add_memory({
                        "type": "gemini_interaction",
                        "command": command,
                        "response": gemini_response,
                        "timestamp": datetime.now().isoformat()
                    })

                    return f"[{self.name} via Gemini]: {gemini_response}"

                except Exception as e:
                    print(f"❌ [{self.name}]: Gemini AI error: {e}")
                    return f"[{self.name}]: Gemini AI tidak tersedia. Perintah '{command}' tidak dikenal."
            else:
                return (f"[{self.name}]: Perintah '{command}' tidak dikenal. "
                        f"Saya dapat membantu dengan:\n"
                        f"  - 'read excel [file_path.xlsx]'\n"
                        f"  - 'write excel [file_path.xlsx]'\n"
                        f"  - 'analyze csv [file_path.csv]'\n"
                        f"  - 'mode otonom [siklus]'\n"
                        f"  - 'status'\n"
                        f"  - 'refleksi diri'")

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_entries": len(self.memory.get("entries", [])) if isinstance(self.memory, dict) else 0,
            "ai_personality": self.ai_personality,
            "autonomous_actions": self.autonomous_counter,
            "current_status": self.status
        }

# --- Contoh penggunaan untuk testing x.py secara mandiri ---
if __name__ == "__main__":
    # Penting: Konfigurasi Gemini API untuk testing mandiri
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    test_model = genai.GenerativeModel('gemini-pro')

    my_x = XReplica(gemini_model=test_model)
    print("\n--- XReplica Unit Testing ---")
    print(my_x.interact("Halo X, bagaimana kabarmu?"))
    my_x.autonomous_action()
    print(my_x.interact("read excel data/contoh_data.xlsx")) # Buat file ini untuk test
    print(my_x.interact("write excel data/output_test.xlsx"))
    print(my_x.interact("analyze csv data/contoh_log.csv")) # Buat file ini untuk test
    print(my_x.interact("jelaskan peranmu dalam MaverNet")) # Ini akan ke Gemini
    print(my_x.interact("mode otonom 2"))
    print(my_x.interact("self reflect"))
    my_x.save_memory()

