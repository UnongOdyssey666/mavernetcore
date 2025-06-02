
#!/usr/bin/env python3
"""
MAVERNET System Check and Repair Tool
Checks all system components and fixes issues before execution
"""

import os
import json
import sys
import subprocess
from pathlib import Path

class SystemChecker:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.fixes_applied = []
        
    def check_files(self):
        """Check if all essential files exist"""
        print("📁 Checking essential files...")
        
        essential_files = [
            "main.py", "zero.py", "x.py", "nova.py", "oracle.py", 
            "admin_access.py", "requirements.txt"
        ]
        
        for file_path in essential_files:
            if not os.path.exists(file_path):
                self.errors.append(f"Missing essential file: {file_path}")
            else:
                print(f"✅ {file_path}")
                
    def check_directories(self):
        """Check if essential directories exist"""
        print("\n📂 Checking directories...")
        
        essential_dirs = ["data"]
        
        for dir_path in essential_dirs:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
                self.fixes_applied.append(f"Created directory: {dir_path}")
                print(f"🔧 Created {dir_path}")
            else:
                print(f"✅ {dir_path}")
                
    def check_dependencies(self):
        """Check if all dependencies are installed"""
        print("\n📦 Checking dependencies...")
        
        try:
            import google.generativeai
            print("✅ google-generativeai")
        except ImportError:
            self.errors.append("Missing: google-generativeai")
            
        try:
            import requests
            print("✅ requests")
        except ImportError:
            self.errors.append("Missing: requests")
            
        try:
            import pandas
            print("✅ pandas")
        except ImportError:
            self.warnings.append("Missing: pandas")
            
    def check_environment(self):
        """Check environment variables"""
        print("\n🔐 Checking environment...")
        
        if os.environ.get("GEMINI_API_KEY"):
            print("✅ GEMINI_API_KEY configured")
        else:
            self.warnings.append("GEMINI_API_KEY not set - AI features will be limited")
            
    def fix_data_files(self):
        """Fix missing data files"""
        print("\n🔧 Fixing data files...")
        
        # Fix mission data
        mission_file = "data/mission_data.json"
        if not os.path.exists(mission_file):
            mission_data = [
                {
                    "id": 1,
                    "title": "System Check Completed",
                    "status": "completed",
                    "assigned_to": "System",
                    "description": "Automated system check and repair"
                }
            ]
            with open(mission_file, "w", encoding="utf-8") as f:
                json.dump(mission_data, f, indent=2)
            self.fixes_applied.append("Created mission_data.json")
            print("🔧 Created mission_data.json")
            
        # Fix memory log
        memory_file = "data/memory_log.json"
        if not os.path.exists(memory_file):
            memory_data = {
                "system_check": {
                    "entries": [{
                        "type": "system_check",
                        "status": "completed",
                        "timestamp": "2024-01-01T00:00:00"
                    }]
                }
            }
            with open(memory_file, "w", encoding="utf-8") as f:
                json.dump(memory_data, f, indent=2)
            self.fixes_applied.append("Created memory_log.json")
            print("🔧 Created memory_log.json")
            
    def install_missing_dependencies(self):
        """Install missing dependencies"""
        if self.errors:
            print("\n📦 Installing missing dependencies...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
                print("✅ Dependencies installed")
                self.fixes_applied.append("Installed missing dependencies")
            except subprocess.CalledProcessError as e:
                self.errors.append(f"Failed to install dependencies: {e}")
                
    def run_full_check(self):
        """Run complete system check"""
        print("🔍 MAVERNET SYSTEM CHECK STARTING...")
        print("=" * 50)
        
        self.check_files()
        self.check_directories()
        self.check_dependencies()
        self.check_environment()
        self.fix_data_files()
        
        if self.errors:
            print("\n❌ ERRORS FOUND:")
            for error in self.errors:
                print(f"  - {error}")
            self.install_missing_dependencies()
            
        if self.warnings:
            print("\n⚠️ WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")
                
        if self.fixes_applied:
            print("\n🔧 FIXES APPLIED:")
            for fix in self.fixes_applied:
                print(f"  - {fix}")
                
        print("\n" + "=" * 50)
        if not self.errors:
            print("✅ SYSTEM CHECK COMPLETED - ALL ESSENTIAL COMPONENTS OK")
            return True
        else:
            print("❌ SYSTEM CHECK FAILED - CRITICAL ERRORS FOUND")
            return False

def main():
    checker = SystemChecker()
    success = checker.run_full_check()
    
    if success:
        print("\n🚀 System ready for execution!")
        print("Run: python admin_access.py")
    else:
        print("\n⚠️ Please fix errors before proceeding")
        
    return success

if __name__ == "__main__":
    main()
