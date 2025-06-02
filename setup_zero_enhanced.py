
#!/usr/bin/env python3
"""
SETUP ZERO ENHANCED
Script untuk transisi ke sistem Zero Enhanced dan cleanup unit lama
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime

def backup_old_units():
    """Backup old unit files"""
    print("📦 Creating backup of old units...")
    
    backup_dir = "backup_old_units"
    os.makedirs(backup_dir, exist_ok=True)
    
    old_files = ["nova.py", "oracle.py", "x.py", "main.py"]
    backed_up = []
    
    for file in old_files:
        if os.path.exists(file):
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_name = f"{file}_{timestamp}.backup"
                shutil.copy2(file, f"{backup_dir}/{backup_name}")
                backed_up.append(file)
                print(f"✅ Backed up: {file} -> {backup_dir}/{backup_name}")
            except Exception as e:
                print(f"❌ Backup failed for {file}: {e}")
    
    return backed_up

def create_enhanced_config():
    """Create configuration for Zero Enhanced"""
    print("⚙️ Creating Zero Enhanced configuration...")
    
    config = {
        "zero_enhanced": {
            "version": "Supreme v3.0",
            "created": datetime.now().isoformat(),
            "admin_mode": True,
            "autonomous_mode": True,
            "combined_skills": [
                "All Zero capabilities",
                "All X Replica capabilities", 
                "All Nova capabilities",
                "All Oracle capabilities",
                "Enhanced self-repair",
                "Autonomous development",
                "LLM integration"
            ],
            "auto_install_libraries": True,
            "self_repair_interval": 300,
            "autonomous_cycle_interval": 30,
            "dashboard_update_interval": 1800
        }
    }
    
    os.makedirs("data", exist_ok=True)
    with open("data/zero_enhanced_config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    
    print("✅ Zero Enhanced configuration created")

def migrate_memory_data():
    """Migrate memory data from old units to Zero Enhanced"""
    print("🧠 Migrating memory data...")
    
    old_memory_files = [
        "data/memory_log.json",
        "data/zero_memory_log.json", 
        "data/x_replica_memory_log.json",
        "data/nova_memory_log.json",
        "data/oracle_memory_log.json"
    ]
    
    combined_memories = {
        "entries": [],
        "autonomous_actions": [],
        "self_repairs": [],
        "migration_info": {
            "migrated_from": old_memory_files,
            "migration_date": datetime.now().isoformat()
        }
    }
    
    for memory_file in old_memory_files:
        if os.path.exists(memory_file):
            try:
                with open(memory_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Extract entries from different formats
                if isinstance(data, dict):
                    for unit_name, unit_data in data.items():
                        if isinstance(unit_data, dict) and "entries" in unit_data:
                            entries = unit_data["entries"]
                            for entry in entries:
                                entry["original_unit"] = unit_name
                                entry["migrated"] = True
                                combined_memories["entries"].append(entry)
                
                print(f"✅ Migrated: {memory_file}")
                
            except Exception as e:
                print(f"❌ Migration failed for {memory_file}: {e}")
    
    # Save combined memory
    with open("data/zero_enhanced_memory.json", "w", encoding="utf-8") as f:
        json.dump(combined_memories, f, indent=2)
    
    print(f"✅ Memory migration completed: {len(combined_memories['entries'])} entries migrated")

def setup_enhanced_workflows():
    """Setup enhanced workflows for Zero Enhanced"""
    print("🔄 Setting up enhanced workflows...")
    
    # This would typically update .replit file, but we'll create a guide instead
    workflow_guide = """
# ZERO ENHANCED WORKFLOWS

## Primary Workflow (Run Button):
python main_zero_enhanced.py

## Autonomous Mode:
python zero_autonomous_runner.py

## Interactive Mode:
python zero_enhanced.py

## Setup Enhanced Libraries:
python -c "from zero_enhanced import ZeroEnhanced; z = ZeroEnhanced(); z.setup_enhanced_libraries()"

## Self-Repair Check:
python -c "from zero_enhanced import ZeroEnhanced; z = ZeroEnhanced(); z.autonomous_self_repair()"
"""
    
    with open("ZERO_ENHANCED_WORKFLOWS.md", "w", encoding="utf-8") as f:
        f.write(workflow_guide)
    
    print("✅ Workflow guide created: ZERO_ENHANCED_WORKFLOWS.md")

def install_enhanced_dependencies():
    """Install enhanced dependencies"""
    print("📦 Installing enhanced dependencies...")
    
    import subprocess
    import sys
    
    enhanced_packages = [
        "ollama",
        "transformers", 
        "torch",
        "langchain",
        "chromadb",
        "faiss-cpu",
        "sentence-transformers"
    ]
    
    installed = []
    failed = []
    
    for package in enhanced_packages:
        try:
            print(f"Installing {package}...")
            result = subprocess.run([sys.executable, "-m", "pip", "install", package], 
                                 capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                installed.append(package)
                print(f"✅ Installed: {package}")
            else:
                failed.append(package)
                print(f"❌ Failed: {package}")
                
        except subprocess.TimeoutExpired:
            failed.append(f"{package} (timeout)")
            print(f"⏰ Timeout: {package}")
        except Exception as e:
            failed.append(f"{package} (error)")
            print(f"❌ Error installing {package}: {e}")
    
    print(f"\n📊 Installation Summary:")
    print(f"✅ Installed: {len(installed)}/{len(enhanced_packages)}")
    print(f"❌ Failed: {len(failed)}")
    
    if failed:
        print(f"Failed packages: {failed}")
    
    return installed, failed

def create_startup_script():
    """Create startup script for Zero Enhanced"""
    startup_script = '''#!/usr/bin/env python3
"""
ZERO ENHANCED STARTUP SCRIPT
Quick startup for Zero Enhanced system
"""

import os
import sys

def main():
    print("🚀 ZERO ENHANCED QUICK START")
    print("=" * 40)
    
    print("1. Interactive Mode - python zero_enhanced.py")
    print("2. System Mode - python main_zero_enhanced.py") 
    print("3. Autonomous Mode - python zero_autonomous_runner.py")
    print("4. Setup Libraries - setup libraries")
    print("5. Status Check - check status")
    
    while True:
        choice = input("\\nSelect mode (1-5 or 'quit'): ").strip()
        
        if choice == '1':
            os.system("python zero_enhanced.py")
            break
        elif choice == '2':
            os.system("python main_zero_enhanced.py")
            break
        elif choice == '3':
            os.system("python zero_autonomous_runner.py")
            break
        elif choice == '4':
            os.system("python -c \\"from zero_enhanced import ZeroEnhanced; z = ZeroEnhanced(); z.setup_enhanced_libraries()\\"")
            break
        elif choice == '5':
            os.system("python -c \\"from zero_enhanced import ZeroEnhanced; z = ZeroEnhanced(); print(z.get_status())\\"")
            break
        elif choice.lower() == 'quit':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
'''
    
    with open("start_zero_enhanced.py", "w", encoding="utf-8") as f:
        f.write(startup_script)
    
    print("✅ Startup script created: start_zero_enhanced.py")

def main():
    """Main setup function"""
    print("🚀 ZERO ENHANCED SETUP")
    print("=" * 50)
    print("Transitioning MAVERNET to Zero Enhanced system...")
    print("")
    
    try:
        # 1. Backup old units
        backed_up = backup_old_units()
        print(f"📦 Backup completed: {len(backed_up)} files")
        
        # 2. Create enhanced config
        create_enhanced_config()
        
        # 3. Migrate memory data
        migrate_memory_data()
        
        # 4. Setup workflows
        setup_enhanced_workflows()
        
        # 5. Create startup script
        create_startup_script()
        
        # 6. Install enhanced dependencies (optional)
        print("\\n📦 Enhanced dependency installation:")
        install_deps = input("Install enhanced AI libraries? (y/n): ").lower().strip()
        
        if install_deps == 'y':
            installed, failed = install_enhanced_dependencies()
        else:
            print("⏭️ Skipping enhanced dependency installation")
        
        # 7. Final summary
        print("\\n🎯 ZERO ENHANCED SETUP COMPLETED!")
        print("=" * 50)
        print("✅ Old units backed up")
        print("✅ Configuration created")
        print("✅ Memory data migrated")
        print("✅ Workflows configured")
        print("✅ Startup script created")
        
        print("\\n🚀 READY TO START ZERO ENHANCED:")
        print("  - Interactive: python zero_enhanced.py")
        print("  - System Mode: python main_zero_enhanced.py")
        print("  - Autonomous: python zero_autonomous_runner.py")
        print("  - Quick Start: python start_zero_enhanced.py")
        
        print("\\n👑 Zero Enhanced is ready with:")
        print("  - All unit capabilities combined")
        print("  - Autonomous self-repair")
        print("  - Supreme administrator access")
        print("  - LLM integration ready")
        print("  - Continuous autonomous operation")
        
    except Exception as e:
        print(f"❌ Setup error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\\n🎉 Zero Enhanced setup successful!")
    else:
        print("\\n😞 Setup encountered errors")
