#!/usr/bin/env python3
"""
MAVERNET MAIN SYSTEM - Zero Enhanced Integration
Single entry point for all MAVERNET operations with Zero Enhanced capabilities
"""

import json
import os
import time
import random
import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime

# Gemini AI import
import google.generativeai as genai

# Import Zero Enhanced
from zero_enhanced import ZeroEnhanced

# Import admin access for administrator functions
from admin_access import MaverNetAdministrator

class MaverNetMainSystem:
    def __init__(self):
        print("🚀 MAVERNET MAIN SYSTEM - ZERO ENHANCED")
        print("=" * 50)

        # Check administrator access
        self.admin_mode = self.check_admin_access()

        # Setup Gemini AI
        self.setup_gemini_ai()

        # Initialize Zero Enhanced as the main AI agent
        self.zero_enhanced = ZeroEnhanced(gemini_model=self.gemini_model)

        # Initialize administrator if needed
        self.administrator = None
        if self.admin_mode:
            self.administrator = MaverNetAdministrator()

        # System configuration
        self.system_config = self.load_system_config()

        print("✅ MAVERNET MAIN SYSTEM READY")

    def check_admin_access(self):
        """Check for administrator access"""
        admin_files = [
            "data/admin_privileges.json",
            "data/system_overrides.json", 
            "data/mavernet_admin_config.json",
            "data/emergency_config.json",
            "data/zero_enhanced_config.json"
        ]

        for admin_file in admin_files:
            if os.path.exists(admin_file):
                print(f"👑 Administrator access detected from {admin_file}")
                return True

        return False

    def setup_gemini_ai(self):
        """Setup Gemini AI"""
        api_key = os.environ.get("GEMINI_API_KEY")
        self.gemini_model = None

        if api_key:
            try:
                genai.configure(api_key=api_key)
                model_names = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']

                for model_name in model_names:
                    try:
                        self.gemini_model = genai.GenerativeModel(model_name)
                        test_response = self.gemini_model.generate_content("Hello")
                        print(f"✅ Gemini AI configured with model: {model_name}")
                        break
                    except Exception:
                        continue

                if self.gemini_model is None:
                    print("❌ No Gemini models available")

            except Exception as e:
                print(f"❌ Gemini AI setup error: {e}")
        else:
            print("⚠️ GEMINI_API_KEY not found")

    def load_system_config(self):
        """Load system configuration"""
        config_path = "data/zero_enhanced_config.json"
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Config load error: {e}")

        # Default config
        return {
            "zero_enhanced": {
                "version": "Supreme v3.0",
                "admin_mode": self.admin_mode,
                "autonomous_mode": True
            }
        }

    def system_boot(self):
        """Boot the main system"""
        print("\n🔧 [MAVERNET SYSTEM BOOTING...]")
        print("🚀 Initializing Zero Enhanced Supreme AI...")

        # Load mission data
        self.load_mission_data()

        # Run initial Zero Enhanced cycles
        self.zero_enhanced.autonomous_action()
        self.zero_enhanced.autonomous_self_repair()

        # Create initial dashboard
        self.zero_enhanced.create_system_dashboard()

        print("✅ [ZERO ENHANCED ONLINE WITH SUPREME CAPABILITIES]")

    def load_mission_data(self):
        """Load mission data"""
        mission_path = "data/mission_data.json"
        try:
            if os.path.exists(mission_path):
                with open(mission_path, 'r', encoding='utf-8') as f:
                    self.mission_data = json.load(f)
                print(f"📌 Loaded {len(self.mission_data)} mission entries")
            else:
                self.mission_data = []
                print("📌 No mission data found")
        except Exception as e:
            print(f"❌ Mission data load error: {e}")
            self.mission_data = []

    def process_command(self, command):
        """Process user commands through the integrated system"""
        command_lower = command.lower().strip()

        # System commands
        if "system status" in command_lower:
            return self.get_system_status()

        elif "system shutdown" in command_lower or "mavernet shutdown" in command_lower:
            self.zero_enhanced.save_memory()
            self.zero_enhanced.status = "Offline"
            return "[MAVERNET]: System shutdown initiated. Goodbye!"

        elif "admin" in command_lower and self.administrator:
            # Route to administrator
            admin_command = command.replace("admin", "").strip()
            if admin_command:
                return f"[Admin]: {self.administrator.execute_command(admin_command)}"
            else:
                return "[Admin]: Administrator console active. Available commands: unlock, status, repair, emergency"

        elif "setup enhanced libraries" in command_lower:
            results = self.zero_enhanced.setup_enhanced_libraries()
            successful = sum(results.values())
            return f"[MAVERNET]: Enhanced libraries setup: {successful}/{len(results)} installed"

        elif "autonomous mode" in command_lower:
            # Extract duration if specified
            duration = 60  # Default 60 minutes
            duration_match = re.search(r'(\d+)\s*(minutes?|mins?|hours?)', command_lower)
            if duration_match:
                value = int(duration_match.group(1))
                unit = duration_match.group(2)
                if 'hour' in unit:
                    duration = value * 60
                else:
                    duration = value

            self.zero_enhanced.start_autonomous_operation(duration)
            return f"[MAVERNET]: Autonomous operation started for {duration} minutes"

        elif "run transition" in command_lower or "setup transition" in command_lower:
            return self.run_transition_setup()

        # Route everything else to Zero Enhanced
        else:
            return self.zero_enhanced.interact(command)

    def get_system_status(self):
        """Get comprehensive system status"""
        status = self.zero_enhanced.get_status()

        return f"""[MAVERNET SYSTEM STATUS]:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Zero Enhanced: {status['current_status']}
👑 Admin Mode: {'ENABLED' if self.admin_mode else 'DISABLED'}
🧠 AI Model: {'Gemini Connected' if self.gemini_model else 'Offline'}

📊 PERFORMANCE METRICS:
  🔄 Autonomous Actions: {status['autonomous_actions']}
  🔧 Self Repairs: {status['self_repairs']} 
  💾 Memory Entries: {status['memory_entries']}
  ✅ Success Rate: {status['success_rate']:.1f}%

⚡ CAPABILITIES:
  • Data Processing & Excel Automation
  • Advanced Visualization & Dashboards  
  • Text Analysis & Threat Assessment
  • Web Browsing & Content Analysis
  • Autonomous Self-Repair & Development
  • Library Installation & System Admin

🎯 READY FOR: Any command, analysis, or autonomous operation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

    def run_transition_setup(self):
        """Run transition setup script"""
        try:
            print("🔄 Running transition setup...")
            result = subprocess.run([sys.executable, "setup_transition.py"], 
                                 capture_output=True, text=True, timeout=60)

            if result.returncode == 0:
                return "[MAVERNET]: Transition setup completed successfully"
            else:
                return f"[MAVERNET]: Transition setup failed: {result.stderr}"

        except Exception as e:
            return f"[MAVERNET]: Transition setup error: {e}"

    def save_all_data(self):
        """Save all system data"""
        self.zero_enhanced.save_memory()
        print("💾 [MAVERNET]: All data saved")

def main():
    """Main entry point"""
    # Initialize main system
    system = MaverNetMainSystem()
    system.system_boot()

    print("\n--- MAVERNET MAIN SYSTEM: Zero Enhanced Active ---")
    print("Available commands:")
    print("  • 'system status' - Complete system overview")
    print("  • 'admin [command]' - Administrator functions")
    print("  • 'setup enhanced libraries' - Install AI libraries")
    print("  • 'autonomous mode [duration]' - Start autonomous operation")
    print("  • 'run transition' - Setup transition from old system")
    print("  • Any Zero Enhanced command (data, analysis, visualization, etc.)")
    print("  • 'system shutdown' - Shutdown system")

    while system.zero_enhanced.status != "Offline":
        try:
            user_input = input("\nCommander> ").strip()

            if not user_input:
                continue

            response = system.process_command(user_input)
            print(response)

            if system.zero_enhanced.status == "Offline":
                break

        except KeyboardInterrupt:
            print(f"\n🛑 System shutdown initiated...")
            system.save_all_data()
            break
        except Exception as e:
            print(f"❌ System error: {e}")
            # Auto-repair on error
            try:
                system.zero_enhanced.autonomous_self_repair()
            except:
                pass

    print("\n👋 MAVERNET SYSTEM SHUTDOWN COMPLETE")

if __name__ == "__main__":
    main()