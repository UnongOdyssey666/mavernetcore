
#!/usr/bin/env python3
"""
MAVERNET_CORE GitHub Setup Script
Connects Replit to GitHub repository for seamless sync
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run shell command with error handling"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Success")
            return result.stdout
        else:
            print(f"❌ {description} - Error: {result.stderr}")
            return None
    except Exception as e:
        print(f"❌ {description} - Exception: {str(e)}")
        return None

def setup_github_connection():
    """Setup GitHub connection for MAVERNET_CORE"""
    print("🚀 MAVERNET_CORE GitHub Setup")
    print("=" * 50)
    
    # Configure Git if not already done
    run_command("git config --global user.name 'MAVERNET_CORE'", "Setting Git username")
    run_command("git config --global user.email 'mavernet@replit.dev'", "Setting Git email")
    
    # Add GitHub remote (replace with your actual GitHub repo URL)
    print("\n📡 Setting up GitHub remote...")
    print("⚠️  Please replace 'yourusername' with your actual GitHub username!")
    
    github_url = "https://github.com/yourusername/mavernet_core.git"
    run_command(f"git remote add origin {github_url}", "Adding GitHub remote")
    
    # Create .gitignore for clean repo
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# Replit
.replit
replit.nix
.config/
.upm/

# Logs
*.log
log/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# MAVERNET specific
*.backup
temp/
"""
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content.strip())
    
    print("✅ GitHub setup completed!")
    print("\n📋 Next steps:")
    print("1. Create 'mavernet_core' repository on GitHub")
    print("2. Update the GitHub URL in this script")
    print("3. Run: python setup_github.py")
    print("4. Use Git pane in Replit for future syncs")

if __name__ == "__main__":
    setup_github_connection()
