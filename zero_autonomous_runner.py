
#!/usr/bin/env python3
"""
ZERO ENHANCED AUTONOMOUS RUNNER
Script untuk menjalankan Zero Enhanced secara otonom tanpa interaksi manusia
"""

import time
import threading
import signal
import sys
from datetime import datetime, timedelta
from zero_enhanced import ZeroEnhanced
import google.generativeai as genai
import os

class ZeroAutonomousRunner:
    def __init__(self):
        self.running = True
        self.zero = None
        self.setup_signal_handlers()
        
    def setup_signal_handlers(self):
        """Setup signal handlers for graceful shutdown"""
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        print(f"\n🛑 Shutdown signal received ({signum})")
        self.running = False
        if self.zero:
            self.zero.save_memory()
    
    def initialize_zero(self):
        """Initialize Zero Enhanced"""
        print("🚀 ZERO AUTONOMOUS RUNNER - INITIALIZING")
        print("=" * 50)
        
        # Setup Gemini AI
        api_key = os.environ.get("GEMINI_API_KEY")
        gemini_model = None
        
        if api_key:
            try:
                genai.configure(api_key=api_key)
                gemini_model = genai.GenerativeModel('gemini-1.5-flash')
                print("✅ Gemini AI configured for autonomous operation")
            except Exception as e:
                print(f"⚠️ Gemini AI setup failed: {e}")
        
        # Initialize Zero Enhanced
        self.zero = ZeroEnhanced(gemini_model=gemini_model)
        print("✅ Zero Enhanced initialized for autonomous operation")
        
    def autonomous_task_scheduler(self):
        """Autonomous task scheduler"""
        tasks = [
            {"name": "self_repair", "interval": 300, "last_run": 0},  # Every 5 minutes
            {"name": "system_analysis", "interval": 600, "last_run": 0},  # Every 10 minutes
            {"name": "threat_assessment", "interval": 900, "last_run": 0},  # Every 15 minutes
            {"name": "create_dashboard", "interval": 1800, "last_run": 0},  # Every 30 minutes
            {"name": "memory_save", "interval": 180, "last_run": 0},  # Every 3 minutes
            {"name": "library_check", "interval": 3600, "last_run": 0},  # Every hour
        ]
        
        current_time = time.time()
        
        for task in tasks:
            if current_time - task["last_run"] >= task["interval"]:
                self.execute_autonomous_task(task["name"])
                task["last_run"] = current_time
    
    def execute_autonomous_task(self, task_name):
        """Execute specific autonomous task"""
        try:
            print(f"🤖 [Autonomous]: Executing task: {task_name}")
            
            if task_name == "self_repair":
                result = self.zero.autonomous_self_repair()
                print(f"🔧 Self-repair: {'Success' if result else 'Issues detected'}")
                
            elif task_name == "system_analysis":
                result = self.zero.analyze_system_data()
                print(f"📊 System analysis: {'Completed' if result else 'Failed'}")
                
            elif task_name == "threat_assessment":
                result = self.zero.threat_assessment()
                if result:
                    print(f"🔮 Threat assessment: {result['threat_level']} risk level")
                
            elif task_name == "create_dashboard":
                result = self.zero.create_system_dashboard()
                print(f"🎨 Dashboard: {'Created' if result else 'Failed'}")
                
            elif task_name == "memory_save":
                self.zero.save_memory()
                print(f"💾 Memory saved successfully")
                
            elif task_name == "library_check":
                # Check if critical libraries are available
                critical_libs = ["requests", "pandas", "matplotlib", "numpy"]
                missing = []
                for lib in critical_libs:
                    try:
                        __import__(lib)
                    except ImportError:
                        missing.append(lib)
                
                if missing:
                    print(f"📦 Missing libraries detected: {missing}")
                    for lib in missing:
                        self.zero.install_library(lib)
                else:
                    print(f"📦 All critical libraries available")
                    
        except Exception as e:
            print(f"❌ Autonomous task error ({task_name}): {e}")
            # Self-repair on error
            try:
                self.zero.autonomous_self_repair()
            except:
                pass
    
    def autonomous_learning_cycle(self):
        """Autonomous learning and improvement cycle"""
        try:
            # Analyze recent performance
            recent_memories = self.zero.memory.get("entries", [])[-20:]
            failures = [m for m in recent_memories if m.get("success") == False]
            
            if len(failures) > 5:  # Too many failures
                print(f"⚠️ [Autonomous]: High failure rate detected ({len(failures)}/20)")
                self.zero.autonomous_self_repair()
            
            # Performance optimization
            if self.zero.autonomous_counter % 10 == 0:
                print(f"🧠 [Autonomous]: Running learning cycle...")
                
                if self.zero.gemini_model and self.zero.conversation:
                    try:
                        learning_prompt = f"""
                        Analisis performa otonom saya:
                        - Total aksi otonom: {self.zero.autonomous_counter}
                        - Self-repair cycles: {self.zero.self_repair_counter}
                        - Kegagalan terakhir: {len(failures)}/20
                        
                        Berikan 3 optimasi spesifik untuk meningkatkan performa otonom saya.
                        """
                        
                        response = self.zero.conversation.send_message(learning_prompt)
                        insights = response.text
                        
                        self.zero.add_memory({
                            "type": "autonomous_learning",
                            "insights": insights,
                            "failure_rate": len(failures)/20,
                            "timestamp": datetime.now().isoformat()
                        })
                        
                        print(f"🧠 [Autonomous]: Learning insights generated")
                        
                    except Exception as e:
                        print(f"❌ Learning cycle error: {e}")
                        
        except Exception as e:
            print(f"❌ Autonomous learning error: {e}")
    
    def status_report(self):
        """Generate status report"""
        try:
            status = self.zero.get_status()
            uptime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"\n📊 AUTONOMOUS STATUS REPORT - {uptime}")
            print(f"🤖 Autonomous Actions: {status['autonomous_actions']}")
            print(f"🔧 Self Repairs: {status['self_repairs']}")
            print(f"💾 Memory Entries: {status['memory_entries']}")
            print(f"✅ Success Rate: {status['success_rate']:.1f}%")
            print(f"🎯 Status: {status['current_status']}")
            print("-" * 50)
            
        except Exception as e:
            print(f"❌ Status report error: {e}")
    
    def run_autonomous_mode(self):
        """Main autonomous operation loop"""
        self.initialize_zero()
        
        print(f"🚀 ZERO ENHANCED AUTONOMOUS MODE STARTED")
        print(f"⏰ Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🔄 Autonomous operation will run continuously...")
        print(f"🛑 Press Ctrl+C to stop")
        
        cycle_count = 0
        last_status_report = time.time()
        
        try:
            while self.running:
                cycle_count += 1
                current_time = time.time()
                
                # Run autonomous action
                self.zero.autonomous_action()
                
                # Run scheduled tasks
                self.autonomous_task_scheduler()
                
                # Learning cycle (every 5 autonomous actions)
                if cycle_count % 5 == 0:
                    self.autonomous_learning_cycle()
                
                # Status report (every 10 minutes)
                if current_time - last_status_report >= 600:
                    self.status_report()
                    last_status_report = current_time
                
                # Sleep between cycles (30 seconds)
                time.sleep(30)
                
        except KeyboardInterrupt:
            print(f"\n🛑 Autonomous mode interrupted by user")
        except Exception as e:
            print(f"❌ Autonomous mode error: {e}")
            # Try to self-repair
            try:
                self.zero.autonomous_self_repair()
            except:
                pass
        finally:
            # Cleanup
            if self.zero:
                self.zero.save_memory()
                print(f"💾 Final memory save completed")
            
            print(f"🏁 Autonomous mode completed after {cycle_count} cycles")
            print(f"⏰ End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """Main function"""
    print("🤖 ZERO ENHANCED AUTONOMOUS RUNNER")
    print("This script will run Zero Enhanced autonomously without human interaction")
    print("The system will self-monitor, self-repair, and continuously improve")
    print("")
    
    runner = ZeroAutonomousRunner()
    runner.run_autonomous_mode()

if __name__ == "__main__":
    main()
