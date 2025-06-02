#!/usr/bin/env python3
"""
MAVERNET CORE SYSTEM
Clean UI with Zero-Only Integration
"""

import json
import os
import time
import random
from pathlib import Path
from datetime import datetime

# Gemini AI import
import google.generativeai as genai

# Import MAVERNET Zero unit only
from zero import Zero

class MaverNetSystem:
    def __init__(self):
        print("🚀 MAVERNET CORE - Zero AI System")
        print("=" * 45)

        # Setup Gemini AI
        global_gemini_model = self.setup_gemini_ai()

        # Check admin access
        self.admin_mode = self.check_admin_access()

        # Initialize Zero AI unit only
        print("🤖 Initializing Zero AI Agent...")
        self.zero = Zero(gemini_model=global_gemini_model, admin_mode=self.admin_mode)

        # System status
        self.omega_mode = False
        self.mission_data = self.load_mission_data()

        print("✅ Zero AI Agent Online")

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
        self.zero.omega_mode = True

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

        # Direct web browsing commands
        elif any(site in cmd for site in ['google.com', 'youtube.com', 'github.com', 'facebook.com', 'twitter.com']):
            return self.zero.web_request(cmd)
        elif cmd.startswith("search "):
            query = cmd.replace("search ", "")
            return self.zero.web_search(query)
        elif cmd == "web check":
            return self.zero.check_internet_connection()

        # Omega mode activation  
        elif "omega" in cmd and ("activate" in cmd or "mode" in cmd):
            return self.activate_omega_mode()

        # Zero commands - All operations go through Zero
        elif cmd.startswith("zero"):
            zero_cmd = cmd.replace("zero", "").strip()
            if not zero_cmd:
                return self.zero.get_status()
            return self.zero.interact(zero_cmd)

        # Direct routing to Zero for all other commands
        else:
            return self.zero.interact(command)

    def get_system_status(self):
        """Get clean system status"""
        omega_status = "🔥 OMEGA v1" if self.omega_mode else "⚡ Standard"
        admin_status = "👑 Admin" if self.admin_mode else "👤 User"

        return f"""🚀 MAVERNET SYSTEM STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ Zero    : Online | Mode: {omega_status}

🔐 Access  : {admin_status}
📊 Missions: {len(self.mission_data)} loaded
💾 Memory  : {len(self.zero.memory.get('entries', []))} entries

🎯 Ready for operations!"""

    def get_help(self):
        """Show available commands"""
        omega_help = """
🔥 OMEGA v1 Commands (Admin Mode):
  omega activate      - Activate Omega v1 mode
  zero read file.txt  - Read any file  
  zero write file.txt content - Write files
  zero repair system  - Full system repair""" if self.admin_mode else ""

        return f"""🚀 MAVERNET COMMANDS

📋 System:
  status    - System overview
  help      - This help menu
  shutdown  - Safe system exit

🌐 WEB BROWSING (Direct Commands):
  google.com          - Visit Google
  youtube.com         - Visit YouTube  
  github.com          - Visit GitHub
  search [query]      - Search internet
  web check           - Test connection

🤖 Zero AI Agent:
  zero [cmd]   - Execute with Zero
  zero help    - Zero's full help menu
  zero status  - Zero's detailed status
  zero repair  - Self-repair system

⚡ Quick Examples:
  google.com            - Browse Google
  search artificial intelligence
  zero read config.json - Read file
  zero web youtube.com  - Browse via Zero
  zero autonomous 3     - Run 3 AI cycles{omega_help}

💡 Just type naturally - System understands context!"""

    def shutdown_system(self):
        """Safe system shutdown"""
        print("🔄 Saving all data...")
        self.zero.save_memory()
        print("💾 System data saved")
        return "👋 MAVERNET System shutdown complete. Goodbye!"

def main():
    """Main system entry point"""
    system = MaverNetSystem()

    print(f"\n🎯 MAVERNET READY - Zero AI Agent Active")
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