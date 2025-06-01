
#!/usr/bin/env python3
"""
Test script for Zero's file system operations
"""

from zero import Zero
import os

def test_zero_file_operations():
    print("🧪 Testing Zero File Operations")
    
    # Create Zero with admin mode
    zero = Zero(admin_mode=True)
    
    # Test write file
    test_content = "Hello from Zero!\nThis is a test file."
    result = zero.write_file("data/zero_test.txt", test_content)
    print(f"Write test: {result}")
    
    # Test read file
    result = zero.read_file("data/zero_test.txt")
    print(f"Read test: {result}")
    
    # Test list directory
    result = zero.list_directory("data")
    print(f"Directory listing: {result}")
    
    # Test without admin mode
    zero_limited = Zero(admin_mode=False)
    result = zero_limited.read_file("main.py")  # This should be denied
    print(f"Limited access test: {result}")
    
    # Cleanup
    try:
        os.remove("data/zero_test.txt")
        print("✅ Test cleanup completed")
    except:
        pass

if __name__ == "__main__":
    test_zero_file_operations()
