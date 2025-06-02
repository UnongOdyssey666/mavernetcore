
#!/usr/bin/env python3
"""
MAVERNET AI Enhancement Monitor
Real-time monitoring of AI agent activities and autonomous actions
"""

import json
import time
from datetime import datetime
from main import MaverNetSystem

class AIMonitor:
    def __init__(self):
        self.system = MaverNetSystem()
        self.monitoring = True
        
    def monitor_ai_activities(self):
        """Monitor AI autonomous activities in real-time"""
        print("🧠 MAVERNET AI ENHANCEMENT MONITOR")
        print("=" * 50)
        print("Monitoring AI autonomous activities...")
        print("Press Ctrl+C to stop monitoring\n")
        
        while self.monitoring:
            try:
                # Trigger AI thinking cycle
                self.system.ai_autonomous_thinking()
                
                # Display current AI status
                print(f"\n⏰ {datetime.now().strftime('%H:%M:%S')} - AI Status Update")
                print("-" * 30)
                
                for unit_name, unit in [("Zero", self.system.zero), 
                                       ("X", self.system.x),
                                       ("Nova", self.system.nova), 
                                       ("Oracle", self.system.oracle)]:
                    status = unit.get_status()
                    print(f"🤖 {unit_name}: {status.get('autonomous_actions', 0)} autonomous actions")
                
                # Save memory after each cycle
                self.system.save_all_memory()
                
                # Wait before next cycle
                time.sleep(10)
                
            except KeyboardInterrupt:
                print("\n🛑 AI monitoring stopped by user")
                self.monitoring = False
            except Exception as e:
                print(f"❌ Error in AI monitoring: {str(e)}")
                time.sleep(5)

    def generate_ai_report(self):
        """Generate AI activity report"""
        print("\n📊 GENERATING AI ACTIVITY REPORT")
        print("=" * 40)
        
        try:
            with open("data/memory_log.json", "r") as f:
                memory_data = json.load(f)
            
            for unit_name, unit_data in memory_data.items():
                if unit_name in ["Zero", "X", "Nova", "Oracle"]:
                    entries = unit_data.get("entries", [])
                    autonomous_actions = [e for e in entries if e.get("type") == "autonomous_action"]
                    
                    print(f"\n🤖 {unit_name} AI Report:")
                    print(f"   Total autonomous actions: {len(autonomous_actions)}")
                    if autonomous_actions:
                        latest = autonomous_actions[-1]
                        print(f"   Latest action: {latest.get('action', 'N/A')}")
                        print(f"   Timestamp: {latest.get('timestamp', 'N/A')}")
        
        except Exception as e:
            print(f"❌ Error generating report: {str(e)}")

if __name__ == "__main__":
    monitor = AIMonitor()
    
    print("Choose option:")
    print("1. Start AI monitoring")
    print("2. Generate AI report")
    print("3. Exit")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        monitor.monitor_ai_activities()
    elif choice == "2":
        monitor.generate_ai_report()
    else:
        print("👋 Goodbye!")
