# x.py - AI-Enhanced Bridge & Documentation Unit
import json
import random
from pathlib import Path
from datetime import datetime

class XReplica:
    def __init__(self):
        self.name = "X"
        self.skills = ["Dokumentasi", "Webhook Integrasi", "AI Architecture Design"]
        self.memory = self.load_memory()
        self.ai_personality = "Stabil dan logis, arsitek sistem log MAVERNET dengan AI adaptif"
        self.autonomous_counter = 0

    def load_memory(self):
        path = Path("data/memory_log.json")
        if path.exists():
            with path.open() as f:
                data = json.load(f)
                return data.get(self.name, {})
        return {}

    def autonomous_action(self):
        """AI Agent: Autonomous documentation and system design"""
        self.autonomous_counter += 1

        actions = [
            "Auto-generating system documentation",
            "Designing new webhook integration patterns",
            "Optimizing log architecture structure", 
            "Creating predictive system bridges"
        ]

        selected_action = random.choice(actions)
        print(f"🤖 [X AI]: Executing autonomous action - {selected_action}")

        # Log autonomous action to memory
        self.add_memory({
            "type": "autonomous_action", 
            "action": selected_action,
            "timestamp": datetime.now().isoformat(),
            "execution_count": self.autonomous_counter
        })

        # Simulate AI learning
        if self.autonomous_counter % 4 == 0:
            print(f"🧠 [X AI]: Architecture pattern learned, implementing improvements...")

    def sync_logs(self):
        print("🔗 [X Replica] AI-Enhanced log sync to external systems")
        self.autonomous_action()

    def add_memory(self, entry):
        if isinstance(self.memory, dict):
            if "entries" not in self.memory:
                self.memory["entries"] = []
            self.memory["entries"].append(entry)
        else:
            self.memory = {"entries": [entry]}

    def init_logger(self):
        print("📋 [X Replica] AI-Enhanced Logger initialized")
        self.autonomous_action()

    def read_spreadsheet(self, file_path):
        """Read spreadsheet data (CSV/Excel)"""
        try:
            if file_path.endswith('.csv'):
                import csv
                data = []
                with open(file_path, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        data.append(row)
                print(f"📊 [X Replica] Successfully read {len(data)} rows from {file_path}")
                self.add_memory({
                    "type": "spreadsheet_read",
                    "file": file_path,
                    "rows_count": len(data),
                    "timestamp": datetime.now().isoformat()
                })
                return data
            elif file_path.endswith(('.xlsx', '.xls')):
                # Placeholder for Excel files - requires openpyxl
                print(f"📊 [X Replica] Excel file detected: {file_path}")
                print("💡 Install openpyxl for Excel support: pip install openpyxl")
                return []
        except Exception as e:
            print(f"❌ [X Replica] Error reading spreadsheet: {str(e)}")
            return []

    def write_to_spreadsheet(self, file_path, data):
        """Write data to spreadsheet (CSV)"""
        try:
            import csv
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for row in data:
                    writer.writerow(row)
            print(f"📝 [X Replica] Successfully wrote {len(data)} rows to {file_path}")
            self.add_memory({
                "type": "spreadsheet_write",
                "file": file_path,
                "rows_written": len(data),
                "timestamp": datetime.now().isoformat()
            })
            return True
        except Exception as e:
            print(f"❌ [X Replica] Error writing spreadsheet: {str(e)}")
            return False

    def interact(self, command):
        """Handle commands sent to XReplica"""
        command_lower = command.lower()

        if "read spreadsheet" in command_lower:
            # Example: "read spreadsheet data/test.csv"
            parts = command.split()
            if len(parts) >= 3:
                file_path = parts[2]
                data = self.read_spreadsheet(file_path)
                return f"[X Replica] Read {len(data)} rows from {file_path}"
            else:
                return "[X Replica] Usage: read spreadsheet [file_path]"

        elif "write spreadsheet" in command_lower:
            # Example: "write spreadsheet data/output.csv sample data"
            parts = command.split()
            if len(parts) >= 3:
                file_path = parts[2]
                # Sample data untuk demonstrasi
                sample_data = [
                    ["ID", "Name", "Value"],
                    ["1", "Test Data 1", "100"],
                    ["2", "Test Data 2", "200"],
                    ["3", "AI Generated", "300"]
                ]
                success = self.write_to_spreadsheet(file_path, sample_data)
                return f"[X Replica] {'Successfully wrote' if success else 'Failed to write'} to {file_path}"
            else:
                return "[X Replica] Usage: write spreadsheet [file_path]"

        elif "status" in command_lower:
            return f"[X Replica] Status: {self.get_status()}"

        else:
            self.autonomous_action()
            return f"[X Replica] AI processing: {command}"

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_entries": len(self.memory.get("entries", [])) if isinstance(self.memory, dict) else 1,
            "ai_personality": self.ai_personality,
            "autonomous_actions": self.autonomous_counter
        }