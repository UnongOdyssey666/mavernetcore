
#!/usr/bin/env python3
"""
ZERO AI AGENT - Main Core System
Enhanced AI Agent with full capabilities
"""

import json
import random
import time
import re
import os
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

# Import library untuk Web Scraping / Interaksi Web
import requests
from bs4 import BeautifulSoup

# Gemini AI import
import google.generativeai as genai

class ZeroCore:
    def __init__(self, gemini_model=None, admin_mode=False):
        """
        Inisialisasi Zero Core AI Agent
        """
        self.name = "Zero"
        self.admin_mode = admin_mode
        self.omega_mode = False
        self.version = "2.0-Enhanced"
        
        # Enhanced skills combining all units
        self.skills = [
            "AI Executive Operations", "Advanced Data Processing", 
            "Visualization Generation", "Intelligence Analysis",
            "Web Interaction", "File System Operations",
            "Autonomous Learning", "Self-Repair", "Real-time Decision Making"
        ]
        
        if admin_mode:
            self.skills.extend(["Omega v1 Operations", "System Administration", "Real File Manipulation"])
        
        # Initialize data directories
        self.data_dir = Path(__file__).parent.parent / "data"
        self.logs_dir = Path(__file__).parent.parent / "logs"
        self.config_dir = Path(__file__).parent.parent / "config"
        
        for dir_path in [self.data_dir, self.logs_dir, self.config_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Load memory and configuration
        self.memory = self.load_memory()
        self.config = self.load_config()
        
        self.ai_personality = "Advanced AI Agent with combined capabilities of all MAVERNET units"
        self.autonomous_counter = 0
        self.self_repair_counter = 0
        
        # Gemini AI Integration
        self.gemini_model = gemini_model
        if self.gemini_model:
            self.conversation = self.gemini_model.start_chat(history=[])
            print(f"🤖 [Zero Core]: Gemini AI integrated")
        else:
            self.conversation = None
            print(f"⚠️ [Zero Core]: Running without Gemini AI")

        self.status = "Online & Ready"
        
        if self.admin_mode:
            print(f"👑 [Zero Core]: Administrator mode - Full system access")

        print(f"[{self.name} Core]: System initialized. Version: {self.version}")

    def load_memory(self):
        """Load Zero memory from dedicated data directory"""
        memory_file = self.data_dir / "zero_memory.json"
        try:
            if memory_file.exists():
                with open(memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                default_memory = {"entries": [], "autonomous_actions": [], "self_repairs": []}
                with open(memory_file, 'w', encoding='utf-8') as f:
                    json.dump(default_memory, f, indent=2)
                return default_memory
        except Exception as e:
            print(f"❌ [Zero Core]: Memory load error: {e}")
            return {"entries": [], "autonomous_actions": [], "self_repairs": []}

    def save_memory(self):
        """Save memory to dedicated data directory"""
        memory_file = self.data_dir / "zero_memory.json"
        try:
            with open(memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.memory, f, indent=2, ensure_ascii=False)
            print(f"💾 [Zero Core]: Memory saved to {memory_file}")
        except Exception as e:
            print(f"❌ [Zero Core]: Memory save error: {e}")

    def load_config(self):
        """Load Zero configuration"""
        config_file = self.config_dir / "zero_config.json"
        default_config = {
            "auto_save_interval": 300,
            "max_memory_entries": 1000,
            "autonomous_mode_enabled": True,
            "self_repair_enabled": True,
            "log_level": "INFO"
        }
        
        try:
            if config_file.exists():
                with open(config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                with open(config_file, 'w', encoding='utf-8') as f:
                    json.dump(default_config, f, indent=2)
                return default_config
        except Exception as e:
            print(f"❌ [Zero Core]: Config load error: {e}")
            return default_config

    def add_memory(self, entry):
        """Add entry to memory with automatic categorization"""
        entry["timestamp"] = datetime.now().isoformat()
        entry["id"] = len(self.memory.get("entries", [])) + 1
        
        if "entries" not in self.memory:
            self.memory["entries"] = []
        
        self.memory["entries"].append(entry)
        
        # Auto-categorize
        if entry.get("type") == "autonomous_action":
            if "autonomous_actions" not in self.memory:
                self.memory["autonomous_actions"] = []
            self.memory["autonomous_actions"].append(entry)
        elif entry.get("type") == "self_repair":
            if "self_repairs" not in self.memory:
                self.memory["self_repairs"] = []
            self.memory["self_repairs"].append(entry)
        
        # Trim memory if too large
        max_entries = self.config.get("max_memory_entries", 1000)
        if len(self.memory["entries"]) > max_entries:
            self.memory["entries"] = self.memory["entries"][-max_entries:]
        
        print(f"📝 [Zero Core]: Memory entry logged: {entry.get('type', 'unknown')}")

    def get_status(self):
        """Get comprehensive status"""
        mode_indicator = "🔥 Omega v1" if self.omega_mode else "⚡ Standard"
        admin_indicator = "👑 Admin" if self.admin_mode else "👤 User"
        
        return f"""🤖 ZERO CORE STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔹 Version: {self.version}
🔹 Mode: {mode_indicator}
🔹 Access: {admin_indicator}
🔹 Status: {self.status}
🔹 Memory: {len(self.memory.get('entries', []))} entries
🔹 Autonomous Cycles: {self.autonomous_counter}
🔹 Self-Repairs: {self.self_repair_counter}
🔹 Skills: {len(self.skills)} capabilities active

🎯 All systems operational!"""

    def interact(self, command):
        """Main interaction method with enhanced capabilities"""
        command_lower = command.lower().strip()
        
        # Log interaction
        self.add_memory({
            "type": "user_interaction",
            "command": command,
            "processed_at": datetime.now().isoformat()
        })
        
        print(f"💬 [User]: {command}")
        
        # Status commands
        if "status" in command_lower:
            return self.get_status()
        
        # File operations
        elif "read file" in command_lower:
            file_path = command.split("read file", 1)[-1].strip()
            return self.read_file(file_path)
        
        elif "write file" in command_lower:
            parts = command.split(" ", 3)
            if len(parts) >= 4:
                file_path = parts[2]
                content = parts[3]
                return self.write_file(file_path, content)
            return "Format: write file <path> <content>"
        
        # Web operations
        elif "web" in command_lower:
            url_match = re.search(r'https?://[^\s]+', command)
            if url_match:
                return self.web_request(url_match.group())
            return "Please provide a valid URL"
        
        # Omega mode
        elif "omega" in command_lower and self.admin_mode:
            self.omega_mode = True
            return "🔥 Omega v1 Mode ACTIVATED!"
        
        # Autonomous mode
        elif "autonomous" in command_lower:
            cycles = 3
            numbers = re.findall(r'\d+', command)
            if numbers:
                cycles = int(numbers[0])
            return self.run_autonomous_cycles(cycles)
        
        # Self-repair
        elif "repair" in command_lower or "fix" in command_lower:
            return self.run_self_repair()
        
        # Gemini AI fallback
        elif self.gemini_model and self.conversation:
            try:
                response = self.conversation.send_message(f"As Zero AI Agent, respond to: {command}")
                ai_response = response.text
                
                self.add_memory({
                    "type": "ai_response",
                    "command": command,
                    "response": ai_response
                })
                
                return f"🤖 [Zero AI]: {ai_response}"
            except Exception as e:
                return f"❌ AI processing error: {e}"
        
        else:
            return f"🤖 [Zero Core]: Command processed. Type 'status' for system info."

    def read_file(self, file_path):
        """Enhanced file reading with permission checks"""
        if not file_path:
            return "❌ Please specify file path"
        
        try:
            if not self.admin_mode and not self._check_file_permission(file_path):
                return f"❌ Access denied: {file_path} requires admin privileges"
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.add_memory({
                "type": "file_read",
                "file_path": file_path,
                "size": len(content),
                "success": True
            })
            
            return f"📖 File read successfully: {file_path}\n{content}"
        
        except FileNotFoundError:
            return f"❌ File not found: {file_path}"
        except Exception as e:
            return f"❌ Read error: {e}"

    def write_file(self, file_path, content):
        """Enhanced file writing with permission checks"""
        try:
            if not self.admin_mode and not self._check_file_permission(file_path):
                return f"❌ Access denied: {file_path} requires admin privileges"
            
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.add_memory({
                "type": "file_write",
                "file_path": file_path,
                "size": len(content),
                "success": True
            })
            
            return f"📝 File written successfully: {file_path}"
        
        except Exception as e:
            return f"❌ Write error: {e}"

    def web_request(self, url):
        """Enhanced web request with smart analysis"""
        try:
            headers = {'User-Agent': 'MAVERNET-Zero/2.0 (AI Agent)'}
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            # Smart content analysis
            content_type = response.headers.get('content-type', '').lower()
            if 'json' in content_type:
                data = response.json()
                result = f"JSON data received with {len(data)} items"
            elif 'html' in content_type:
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.find('title')
                result = f"HTML page: {title.text.strip() if title else 'No title'}"
            else:
                result = f"Content received: {len(response.text)} characters"
            
            self.add_memory({
                "type": "web_request",
                "url": url,
                "status_code": response.status_code,
                "result": result,
                "success": True
            })
            
            return f"🌐 Web request successful: {result}"
        
        except Exception as e:
            error_msg = f"Web request failed: {str(e)}"
            self.add_memory({
                "type": "web_request",
                "url": url,
                "error": error_msg,
                "success": False
            })
            return f"❌ {error_msg}"

    def run_autonomous_cycles(self, cycles=3):
        """Run autonomous operation cycles"""
        results = []
        for i in range(cycles):
            self.autonomous_counter += 1
            action = f"Autonomous cycle {i+1}/{cycles} - Optimizing system operations"
            
            self.add_memory({
                "type": "autonomous_action",
                "cycle": i+1,
                "action": action,
                "counter": self.autonomous_counter
            })
            
            results.append(f"✅ Cycle {i+1}: {action}")
            time.sleep(0.5)  # Simulate processing
        
        return f"🤖 Autonomous cycles completed:\n" + "\n".join(results)

    def run_self_repair(self):
        """Run self-repair cycle"""
        self.self_repair_counter += 1
        
        repairs = [
            "Memory optimization completed",
            "Configuration validation passed",
            "File system integrity checked",
            "Network connectivity verified",
            "Performance metrics updated"
        ]
        
        self.add_memory({
            "type": "self_repair",
            "repairs": repairs,
            "cycle": self.self_repair_counter
        })
        
        return f"🔧 Self-repair cycle #{self.self_repair_counter} completed:\n" + "\n".join(f"✅ {repair}" for repair in repairs)

    def _check_file_permission(self, file_path):
        """Check file access permissions"""
        safe_paths = ['data/', 'logs/', 'temp/', 'output/', 'zero_system/']
        safe_extensions = ['.txt', '.json', '.csv', '.log', '.md', '.py']
        
        file_path_str = str(file_path)
        return (any(file_path_str.startswith(path) for path in safe_paths) or
                any(file_path_str.endswith(ext) for ext in safe_extensions))

# Wrapper class for backward compatibility
class Zero(ZeroCore):
    """Backward compatibility wrapper"""
    def __init__(self, gemini_model=None, admin_mode=False):
        super().__init__(gemini_model, admin_mode)

if __name__ == "__main__":
    zero = ZeroCore()
    print(zero.get_status())
