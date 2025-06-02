
#!/usr/bin/env python3
"""
MAVERNET AI Agent Demonstration
Showcasing advanced AI Agent capabilities of all units
"""

import time
from main import MaverNetSystem

def demonstrate_ai_agent_capabilities():
    """Demonstrate AI Agent capabilities of all MAVERNET units"""
    
    print("🚀 MAVERNET AI AGENT CAPABILITIES DEMONSTRATION")
    print("=" * 60)
    print("Initializing MAVERNET System with AI Agent enhancements...")
    
    # Initialize system
    system = MaverNetSystem()
    system.system_boot()
    
    print("\n🤖 TESTING AI AGENT FEATURES:")
    print("-" * 40)
    
    # Test flexible command routing
    test_commands = [
        "Zero visit website https://httpbin.org/json",
        "Ask X to download data from https://jsonplaceholder.typicode.com/posts",
        "Tell Nova to create real-time dashboard",
        "Oracle conduct threat assessment",
        "analyze security for website https://example.com",
        "create advanced chart with system data",
        "automated pipeline csv sample_data",
        "intelligence gathering from https://httpbin.org/html"
    ]
    
    for i, command in enumerate(test_commands, 1):
        print(f"\n🧪 Test {i}: {command}")
        print("-" * 30)
        
        try:
            response = system.process_overall_command(command)
            print(f"✅ Response: {response}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        time.sleep(2)  # Brief pause between tests
    
    # Test self-reflection capabilities
    print("\n🧠 TESTING SELF-REFLECTION CAPABILITIES:")
    print("-" * 45)
    
    units = [
        ("Zero", system.zero),
        ("X Replica", system.x),
        ("Nova", system.nova),
        ("Oracle", system.oracle)
    ]
    
    for unit_name, unit in units:
        print(f"\n🔍 {unit_name} Self-Reflection:")
        try:
            if hasattr(unit, 'self_reflect_and_learn'):
                unit.self_reflect_and_learn()
                print(f"✅ {unit_name} completed self-reflection")
            else:
                print(f"⚠️ {unit_name} does not have self-reflection capability")
        except Exception as e:
            print(f"❌ {unit_name} self-reflection error: {str(e)}")
    
    # Final system status
    print("\n📊 FINAL SYSTEM STATUS:")
    print("-" * 25)
    system.system_status()
    
    # Save all memories
    print("\n💾 Saving all AI Agent experiences...")
    system.save_all_memory()
    
    print("\n🎯 AI AGENT DEMONSTRATION COMPLETED!")
    print("Check the 'data/' directory for generated reports and analysis files.")

if __name__ == "__main__":
    demonstrate_ai_agent_capabilities()
