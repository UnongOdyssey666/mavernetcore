
# ZERO SYSTEM - Advanced AI Agent

## Overview
Zero System adalah implementasi lengkap dari AI Agent MAVERNET dengan capabilities gabungan dari semua unit (Zero, X, Nova, Oracle).

## Structure
```
zero_system/
├── core/
│   └── zero_main.py      # Main Zero implementation
├── data/
│   └── zero_memory.json  # Zero memory storage
├── logs/                 # System logs
├── config/
│   └── system_config.json # System configuration
└── modules/              # Extension modules
```

## Features
- ✅ Advanced AI Agent capabilities
- ✅ File system operations with permission control
- ✅ Web interaction and scraping
- ✅ Autonomous operation cycles
- ✅ Self-repair mechanisms
- ✅ Memory management
- ✅ Omega v1 mode (admin-only)
- ✅ Gemini AI integration

## Usage

### Basic Usage
```python
from zero import Zero
zero = Zero(gemini_model=model, admin_mode=True)
response = zero.interact("your command here")
```

### Commands
- `status` - Get system status
- `read file <path>` - Read file contents
- `write file <path> <content>` - Write to file
- `web <url>` - Web request
- `autonomous <cycles>` - Run autonomous cycles
- `repair` - Run self-repair

### Admin Commands (Omega v1)
- `omega` - Activate Omega v1 mode
- Full file system access
- Advanced web scraping
- System administration

## Configuration
Edit `config/system_config.json` to customize:
- Feature toggles
- Permission settings
- Data paths
- Operation limits

## Logs
System logs are stored in `logs/` directory:
- Error logs
- Operation logs
- Performance metrics

## Memory
Zero maintains persistent memory in `data/zero_memory.json`:
- User interactions
- Autonomous actions
- Self-repair cycles
- System events
