#!/usr/bin/env python3
"""
MAVERNET CORE SYSTEM
Clean UI with Omega v1 Integration
"""

import json
import os
import time
import random
from pathlib import Path
from datetime import datetime

# Gemini AI import
import google.generativeai as genai

# Import MAVERNET units
from zero import Zero

class MaverNetSystem:
    def __init__(self):
        print("🚀 MAVERNET CORE - AI Multi-Agent System")
        print("=" * 45)

        # Setup Gemini AI
        global_gemini_model = self.setup_gemini_ai()

        # Check admin access
        self.admin_mode = self.check_admin_access()

        # Initialize AI units
        print("🤖 Initializing AI Agents...")
        self.zero = Zero(gemini_model=global_gemini_model, admin_mode=self.admin_mode)
        self.x = X(gemini_model=global_gemini_model)
        self.nova = Nova(gemini_model=global_gemini_model)
        self.oracle = Oracle(gemini_model=global_gemini_model)

        # System status
        self.omega_mode = False
        self.mission_data = self.load_mission_data()

        print("✅ All AI Agents Online")

    def setup_gemini_ai(self):
        """Setup Gemini AI"""
        api_key = os.environ.get("GEMINI_API_KEY")
        if api_key:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                print("✅ Gemini AI configured successfully")
                return model
            except Exception as e:
                print(f"⚠️ Gemini AI error: {e}")
        else:
            print("⚠️ GEMINI_API_KEY not found")
        return None

    def check_admin_access(self):
        """Check for admin privileges"""
        admin_files = ["data/admin_privileges.json", "data/mavernet_admin_config.json"]
        for file in admin_files:
            if os.path.exists(file):
                print("👑 Administrator Access Detected")
                return True
        return False

    def load_mission_data(self):
        """Load mission data"""
        try:
            if os.path.exists("data/mission_data.json"):
                with open("data/mission_data.json", 'r') as f:
                    return json.load(f)
        except:
            pass
        return []

    def activate_omega_mode(self):
        """Activate Omega v1 Mode for real operations"""
        if not self.admin_mode:
            return "❌ Omega v1 requires Administrator access"

        self.omega_mode = True
        self.zero.admin_mode = True

        print("🔥 OMEGA v1 MODE ACTIVATED")
        print("⚡ Real file operations enabled")
        print("🌐 Advanced web interaction enabled")
        print("🔧 System automation unlocked")

        # Log omega activation
        self.zero.add_memory({
            "type": "omega_activation",
            "timestamp": datetime.now().isoformat(),
            "capabilities": ["real_file_ops", "advanced_web", "system_automation"]
        })

        return "🔥 Omega v1 Mode ACTIVATED - Real operations enabled!"

    def process_command(self, command):
        """Process user commands with simplified interface"""
        cmd = command.lower().strip()

        # System commands
        if cmd == "status":
            return self.get_system_status()
        elif cmd == "help":
            return self.get_help()
        elif "shutdown" in cmd or "exit" in cmd:
            return self.shutdown_system()

        # Omega mode activation
        elif "omega" in cmd and "zero" in cmd:
            return self.activate_omega_mode()

        # Zero commands
        elif cmd.startswith("zero"):
            zero_cmd = cmd.replace("zero", "").strip()
            if not zero_cmd:
                return self.zero.get_status()
            return self.zero.interact(zero_cmd)

        # X commands
        elif cmd.startswith("x"):
            x_cmd = cmd.replace("x", "").strip()
            if not x_cmd:
                return f"[X]: {self.x.get_status()}"
            return self.x.interact(x_cmd)

        # Nova commands
        elif cmd.startswith("nova"):
            nova_cmd = cmd.replace("nova", "").strip()
            if not nova_cmd:
                return f"[Nova]: {self.nova.get_status()}"
            return self.nova.interact(nova_cmd)

        # Oracle commands  
        elif cmd.startswith("oracle"):
            oracle_cmd = cmd.replace("oracle", "").strip()
            if not oracle_cmd:
                return f"[Oracle]: {self.oracle.get_status()}"
            return self.oracle.interact(oracle_cmd)

        # Auto-route intelligent commands
        elif any(word in cmd for word in ["read", "write", "file", "web", "search"]):
            return self.zero.interact(command)
        elif any(word in cmd for word in ["excel", "spreadsheet", "data", "csv"]):
            return self.x.interact(command)
        elif any(word in cmd for word in ["chart", "graph", "visual", "dashboard"]):
            return self.nova.interact(command)
        elif any(word in cmd for word in ["analyze", "predict", "threat", "intelligence"]):
            return self.oracle.interact(command)

        else:
            return self.get_help()

    def get_system_status(self):
        """Get clean system status"""
        omega_status = "🔥 OMEGA v1" if self.omega_mode else "⚡ Standard"
        admin_status = "👑 Admin" if self.admin_mode else "👤 User"

        return f"""🚀 MAVERNET SYSTEM STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ Zero    : {self.zero.status} | Mode: {omega_status}
🔗 X       : Online | Data Processing Ready
🎨 Nova    : Online | Visualization Ready  
🔮 Oracle  : Online | Analysis Ready

🔐 Access  : {admin_status}
📊 Missions: {len(self.mission_data)} loaded
💾 Memory  : {len(self.zero.memory.get('entries', []))} entries

🎯 Ready for operations!"""

    def get_help(self):
        """Show available commands"""
        omega_help = """
🔥 OMEGA v1 Commands (Admin Mode):
  zero mode omega     - Activate Omega v1
  zero read file.txt  - Read any file
  zero write file.txt content - Write files
  zero web scrape url - Real web scraping""" if self.admin_mode else ""

        return f"""🚀 MAVERNET COMMANDS

📋 System:
  status    - System overview
  help      - This help menu
  shutdown  - Safe system exit

🤖 AI Agents:
  zero [cmd]   - Execute with Zero
  x [cmd]      - Data operations with X
  nova [cmd]   - Visualization with Nova
  oracle [cmd] - Analysis with Oracle

⚡ Quick Examples:
  zero status           - Zero's status
  x read excel data.xlsx - Process Excel
  nova create chart     - Generate chart
  oracle analyze text   - Text analysis{omega_help}

💡 Just type naturally - AI will understand!"""

    def shutdown_system(self):
        """Safe system shutdown"""
        print("🔄 Saving all data...")
        self.zero.save_memory()
        print("💾 System data saved")
        return "👋 MAVERNET System shutdown complete. Goodbye!"

def main():
    """Main system entry point"""
    system = MaverNetSystem()

    print(f"\n🎯 MAVERNET READY")
    print("Type 'help' for commands or 'status' for system info")

    while True:
        try:
            user_input = input("\nCommander> ").strip()

            if not user_input:
                continue

            response = system.process_command(user_input)
            print(response)

            if "shutdown complete" in response:
                break

        except KeyboardInterrupt:
            print("\n🛑 Emergency shutdown...")
            system.zero.save_memory()
            break
        except Exception as e:
            print(f"❌ System error: {e}")
            print("💡 Try 'help' for available commands")

if __name__ == "__main__":
    main()