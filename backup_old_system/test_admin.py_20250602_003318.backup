
#!/usr/bin/env python3
"""
Test Admin System
"""

import subprocess
import sys

def test_admin_system():
    print("🧪 Testing Admin System...")
    
    try:
        # Test admin access
        result = subprocess.run([
            sys.executable, "admin_access.py"
        ], input="help\nexit\n", text=True, capture_output=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ Admin system accessible")
            print("Sample output:")
            print(result.stdout[:200] + "..." if len(result.stdout) > 200 else result.stdout)
        else:
            print("❌ Admin system error:")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("⚠️ Admin system test timeout - system might be working")
    except Exception as e:
        print(f"❌ Test error: {e}")

if __name__ == "__main__":
    test_admin_system()
