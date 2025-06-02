
#!/usr/bin/env python3
"""
MAVERNET ZERO ENHANCED - SUPREME SYSTEM
Focusing only on Zero Enhanced with all combined capabilities
"""

import os
import json
from datetime import datetime
from pathlib import Path

# Import our enhanced Zero
from zero_enhanced import ZeroEnhanced

# Setup Gemini AI
import google.generativeai as genai

class ZeroEnhancedSystem:
    def __init__(self):
        print("🚀 MAVERNET ZERO ENHANCED SYSTEM STARTING...")
        print("=" * 50)
        
        # Check for admin access
        self.admin_mode = self.check_admin_access()
        
        # Setup Gemini AI
        self.setup_gemini_ai()
        
        # Initialize Zero Enhanced
        self.zero_enhanced = ZeroEnhanced(gemini_model=self.gemini_model)
        
        # Ensure data directory
        os.makedirs("data", exist_ok=True)
        
        print("✅ ZERO ENHANCED SYSTEM READY")

    def check_admin_access(self):
        """Check for administrator access"""
        admin_files = [
            "data/admin_privileges.json",
            "data/system_overrides.json", 
            "data/mavernet_admin_config.json",
            "data/emergency_config.json"
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

    def system_boot(self):
        """Boot the Zero Enhanced system"""
        print("\n🔧 [ZERO ENHANCED SYSTEM BOOTING...]")
        print("🚀 Initializing Supreme AI Agent...")
        
        # Run initial autonomous cycle
        self.zero_enhanced.autonomous_action()
        
        # Run initial self-repair
        self.zero_enhanced.autonomous_self_repair()
        
        # Create initial dashboard
        self.zero_enhanced.create_system_dashboard()
        
        print("✅ [ZERO ENHANCED ONLINE WITH SUPREME CAPABILITIES]")

    def process_command(self, command):
        """Process commands through Zero Enhanced"""
        return self.zero_enhanced.interact(command)

    def cleanup_old_units(self):
        """Remove old unit files (optional - for cleanup)"""
        old_files = ["nova.py", "oracle.py", "x.py"]
        
        for file in old_files:
            if os.path.exists(file):
                try:
                    # Backup first
                    backup_dir = "backup_old_units"
                    os.makedirs(backup_dir, exist_ok=True)
                    
                    import shutil
                    shutil.move(file, f"{backup_dir}/{file}")
                    print(f"📦 Moved {file} to backup")
                except Exception as e:
                    print(f"⚠️ Could not move {file}: {e}")

if __name__ == "__main__":
    # Initialize system
    system = ZeroEnhancedSystem()
    system.system_boot()
    
    print("\n--- ZERO ENHANCED SYSTEM: SUPREME MODE ACTIVE ---")
    print("Commands:")
    print("  - 'status' - System status")
    print("  - 'self repair' - Run self-repair")
    print("  - 'autonomous mode' - Run autonomous cycles")
    print("  - 'setup enhanced libraries' - Install AI libraries")
    print("  - 'create chart [type]' - Generate visualizations")
    print("  - 'read excel [file]' - Process spreadsheets")
    print("  - 'text analysis [text]' - Analyze text")
    print("  - 'threat assessment' - Security analysis")
    print("  - 'web request [url]' - Web analysis")
    print("  - 'start autonomous [minutes]' - Continuous operation")
    print("  - 'cleanup old units' - Remove old unit files")
    print("  - 'shutdown' - System shutdown")
    
    while system.zero_enhanced.status != "Offline":
        try:
            user_input = input("\nSupreme Commander> ").strip()
            
            if not user_input:
                continue
            
            # Special system commands
            if user_input.lower() == "cleanup old units":
                system.cleanup_old_units()
                print("✅ Old unit files moved to backup")
                continue
            
            # Process through Zero Enhanced
            response = system.process_command(user_input)
            print(response)
            
            if system.zero_enhanced.status == "Offline":
                break
                
        except KeyboardInterrupt:
            print(f"\n🛑 System shutdown initiated...")
            system.zero_enhanced.save_memory()
            break
        except Exception as e:
            print(f"❌ System error: {e}")
            # Auto-repair on error
            system.zero_enhanced.autonomous_self_repair()
    
    print("\n👋 ZERO ENHANCED SYSTEM SHUTDOWN COMPLETE")
