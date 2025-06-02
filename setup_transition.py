
#!/usr/bin/env python3
"""
SETUP TRANSISI MAVERNET KE ZERO ENHANCED
Script untuk backup unit lama dan migrasi ke sistem Zero Enhanced
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime

def backup_old_files():
    """Backup file-file lama"""
    print("📦 Creating backup of old files...")
    
    backup_dir = "backup_old_system"
    os.makedirs(backup_dir, exist_ok=True)
    
    files_to_backup = [
        "nova.py", "oracle.py", "x.py", "ai_agent_demo.py", 
        "ai_enhancement.py", "test_admin.py", "test_gemini_api.py",
        "test_zero_files.py", "system_check.py", "setup_github.py",
        "autonomous_enhancement.py", "x (copy).py"
    ]
    
    backed_up = []
    for file in files_to_backup:
        if os.path.exists(file):
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_name = f"{file}_{timestamp}.backup"
                shutil.move(file, f"{backup_dir}/{backup_name}")
                backed_up.append(file)
                print(f"✅ Moved: {file} -> backup")
            except Exception as e:
                print(f"❌ Failed to backup {file}: {e}")
    
    return backed_up

def migrate_memory_data():
    """Migrasi data memori ke format Zero Enhanced"""
    print("🧠 Migrating memory data...")
    
    # Collect all existing memory data
    memory_files = [
        "data/memory_log.json",
        "data/zero_memory_log.json",
        "data/x_replica_memory_log.json", 
        "data/nova_memory_log.json",
        "data/oracle_memory_log.json"
    ]
    
    combined_memory = {
        "zero_enhanced": {
            "entries": [],
            "autonomous_actions": [],
            "self_repairs": [],
            "migration_info": {
                "migrated_from": "old_mavernet_units",
                "migration_date": datetime.now().isoformat(),
                "combined_units": ["Zero", "X", "Nova", "Oracle"]
            }
        }
    }
    
    total_entries = 0
    
    for memory_file in memory_files:
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
                                combined_memory["zero_enhanced"]["entries"].append(entry)
                                total_entries += 1
                
                print(f"✅ Migrated: {memory_file}")
                
            except Exception as e:
                print(f"❌ Migration failed for {memory_file}: {e}")
    
    # Save migrated memory
    with open("data/zero_enhanced_memory.json", "w", encoding="utf-8") as f:
        json.dump(combined_memory, f, indent=2)
    
    print(f"✅ Memory migration completed: {total_entries} entries migrated")
    return total_entries

def cleanup_directories():
    """Cleanup unnecessary directories and files"""
    print("🧹 Cleaning up directories...")
    
    # Clean up memory log directory if it's empty or contains only system files
    memory_log_dir = "data/memory_log"
    if os.path.exists(memory_log_dir):
        try:
            files_in_dir = os.listdir(memory_log_dir)
            if not files_in_dir or all(f.startswith('.') for f in files_in_dir):
                shutil.rmtree(memory_log_dir)
                print("✅ Removed empty memory_log directory")
        except Exception as e:
            print(f"⚠️ Could not remove memory_log directory: {e}")
    
    # Remove unnecessary attached assets
    attached_dir = "attached_assets"
    if os.path.exists(attached_dir):
        try:
            shutil.rmtree(attached_dir)
            print("✅ Removed attached_assets directory")
        except Exception as e:
            print(f"⚠️ Could not remove attached_assets: {e}")

def main():
    """Main transition function"""
    print("🚀 MAVERNET TRANSITION TO ZERO ENHANCED")
    print("=" * 50)
    
    try:
        # 1. Backup old files
        backed_up = backup_old_files()
        print(f"📦 Backup completed: {len(backed_up)} files")
        
        # 2. Migrate memory data
        total_entries = migrate_memory_data()
        
        # 3. Cleanup directories
        cleanup_directories()
        
        # 4. Create Zero Enhanced config
        config = {
            "zero_enhanced": {
                "version": "Supreme v3.0",
                "transition_date": datetime.now().isoformat(),
                "admin_mode": True,
                "autonomous_mode": True,
                "main_entry_point": "main.py",
                "backup_location": "backup_old_system"
            }
        }
        
        with open("data/zero_enhanced_config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)
        
        print("\n🎯 TRANSITION COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        print("✅ Old files backed up")
        print(f"✅ {total_entries} memory entries migrated")
        print("✅ Directories cleaned")
        print("✅ Zero Enhanced configuration created")
        
        print("\n🚀 READY TO USE:")
        print("  - python main.py (Main system)")
        print("  - All functions now integrated into main.py")
        
        return True
        
    except Exception as e:
        print(f"❌ Transition error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 Transition to Zero Enhanced successful!")
    else:
        print("\n😞 Transition encountered errors")
