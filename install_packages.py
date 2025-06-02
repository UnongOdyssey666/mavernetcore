
#!/usr/bin/env python3
"""
MAVERNET Package Installer
Installs all required packages for full functionality
"""

import subprocess
import sys
import os

def install_packages():
    """Install all required packages"""
    
    packages = [
        'requests',
        'beautifulsoup4', 
        'google-generativeai',
        'pandas',
        'numpy',
        'matplotlib',
        'pillow',
        'openpyxl'
    ]
    
    print("🚀 MAVERNET PACKAGE INSTALLER")
    print("=" * 40)
    print(f"Installing {len(packages)} packages...")
    
    for package in packages:
        try:
            print(f"📦 Installing {package}...")
            result = subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ {package} installed successfully")
            else:
                print(f"❌ {package} installation failed: {result.stderr}")
                
        except Exception as e:
            print(f"❌ Error installing {package}: {e}")
    
    print("\n🔍 Testing installations...")
    
    # Test imports
    test_results = {}
    
    test_imports = {
        'requests': 'requests',
        'beautifulsoup4': 'bs4',
        'google-generativeai': 'google.generativeai',
        'pandas': 'pandas',
        'numpy': 'numpy', 
        'matplotlib': 'matplotlib',
        'pillow': 'PIL',
        'openpyxl': 'openpyxl'
    }
    
    for package, import_name in test_imports.items():
        try:
            __import__(import_name)
            test_results[package] = "✅ OK"
        except ImportError:
            test_results[package] = "❌ FAILED"
    
    print("\n📊 INSTALLATION RESULTS:")
    print("-" * 30)
    for package, status in test_results.items():
        print(f"{package:<20} {status}")
    
    # Check web connectivity
    print("\n🌐 Testing web connectivity...")
    try:
        import requests
        response = requests.get('https://google.com', timeout=10)
        print("✅ Internet connection working!")
    except:
        print("❌ Internet connection issue")
    
    print("\n🎯 Setup complete! Run 'python main.py' to start MAVERNET")

if __name__ == "__main__":
    install_packages()
