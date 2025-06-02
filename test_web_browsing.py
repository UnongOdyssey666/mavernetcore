
#!/usr/bin/env python3
"""
Test Web Browsing Capabilities
"""

import sys
from pathlib import Path

# Add zero_system to path
zero_system_path = Path(__file__).parent / "zero_system" / "core"
sys.path.insert(0, str(zero_system_path))

try:
    from zero_main import ZeroCore
    import google.generativeai as genai
    import os
    
    # Setup Gemini if available
    api_key = os.environ.get("GEMINI_API_KEY")
    gemini_model = None
    
    if api_key:
        try:
            genai.configure(api_key=api_key)
            gemini_model = genai.GenerativeModel('gemini-1.5-flash')
            print("✅ Gemini AI configured")
        except Exception as e:
            print(f"⚠️ Gemini AI error: {e}")
    
    # Initialize Zero
    zero = ZeroCore(gemini_model=gemini_model, admin_mode=True)
    
    print("🌐 TESTING WEB BROWSING CAPABILITIES")
    print("=" * 50)
    
    # Test 1: Check internet connection
    print("\n1. Testing internet connection...")
    result = zero.check_internet_connection()
    print(result)
    
    # Test 2: Visit Google
    print("\n2. Testing Google access...")
    result = zero.web_request("google.com")
    print(result)
    
    # Test 3: Visit YouTube
    print("\n3. Testing YouTube access...")
    result = zero.web_request("youtube.com")
    print(result)
    
    # Test 4: Search functionality
    print("\n4. Testing web search...")
    result = zero.web_search("artificial intelligence")
    print(result)
    
    print("\n✅ Web browsing test completed!")
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()
