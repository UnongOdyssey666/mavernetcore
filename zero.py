#!/usr/bin/env python3
"""
ZERO AI AGENT - Main Interface
Redirects to zero_system core implementation
"""

import sys
from pathlib import Path

# Add zero_system to path
zero_system_path = Path(__file__).parent / "zero_system" / "core"
sys.path.insert(0, str(zero_system_path))

try:
    from zero_main import Zero, ZeroCore
    print("✅ Zero system loaded from zero_system/core")
except ImportError as e:
    print(f"❌ Failed to import Zero system: {e}")
    print("📁 Falling back to basic implementation...")

    # Basic fallback implementation
    class Zero:
        def __init__(self, gemini_model=None, admin_mode=False):
            self.name = "Zero"
            self.status = "Online (Basic Mode)"
            self.admin_mode = admin_mode
            self.omega_mode = False
            self.memory = {"entries": []}
            self.autonomous_counter = 0
            print(f"⚠️ [Zero]: Running in basic mode due to import error")

        def get_status(self):
            return f"""🤖 ZERO STATUS (Basic Mode)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔹 Name: {self.name}
🔹 Status: {self.status}
🔹 Mode: Basic (System files missing)
❌ Full system not available
🔧 Run setup to restore full functionality"""

        def interact(self, command):
            return f"⚠️ [Zero Basic]: Command received: '{command}'\n❌ Full Zero system not available. Please check zero_system directory."

        def add_memory(self, entry):
            self.memory["entries"].append(entry)
            print(f"📝 [Zero Basic]: Memory logged (basic mode)")

        def save_memory(self):
            print(f"💾 [Zero Basic]: Memory save attempted (basic mode)")

# Export the Zero class
__all__ = ['Zero', 'ZeroCore']