import json
import random
from pathlib import Path
from datetime import datetime

class Nova:
    def __init__(self):
        self.name = "Nova"
        self.skills = [
            "Desain UI",
            "Visualisasi Dashboard", 
            "Chart & Grafik Statistik",
            "AI Visual Innovation"
        ]
        self.memory = self.load_memory()
        self.visual_data = {}
        self.ai_personality = "Elegan dan intuitif, ahli visualisasi dengan AI kreatif"
        self.autonomous_counter = 0

    def load_memory(self):
        path = Path("data/memory_log.json")
        if path.exists():
            with path.open() as f:
                data = json.load(f)
                return data.get(self.name, {})
        return {}

    def autonomous_action(self):
        """AI Agent: Autonomous UI/UX design and visual innovation"""
        self.autonomous_counter += 1
        
        actions = [
            "Generating next-gen UI concepts",
            "Analyzing user interaction patterns",
            "Creating adaptive visual experiences",
            "Designing intuitive dashboard layouts"
        ]
        
        selected_action = random.choice(actions)
        print(f"🤖 [Nova AI]: Executing autonomous action - {selected_action}")
        
        # Log autonomous action to memory
        self.add_memory({
            "type": "autonomous_action",
            "action": selected_action, 
            "timestamp": datetime.now().isoformat(),
            "execution_count": self.autonomous_counter
        })
        
        # Simulate AI creativity
        if self.autonomous_counter % 2 == 0:
            print(f"🎨 [Nova AI]: Creative breakthrough! Implementing new visual paradigm...")

    def update_visual_data(self, key, value):
        self.visual_data[key] = value
        print(f"✨ [Nova] AI-Enhanced visual data updated: {key} = {value}")
        self.autonomous_action()

    def generate_dashboard(self):
        print("🎨 [Nova] AI-Enhanced dashboard generation...")
        for k, v in self.visual_data.items():
            print(f" - {k}: {v}")
        self.autonomous_action()

    def create_html_report(self, data, file_path="data/nova_report.html"):
        """Generate HTML report from data"""
        try:
            html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>MAVERNET Nova Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #0a0a0a; color: #00ff00; }}
        .header {{ text-align: center; border-bottom: 2px solid #00ff00; padding: 20px; }}
        .data-section {{ margin: 20px 0; padding: 15px; border: 1px solid #00ff00; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ border: 1px solid #00ff00; padding: 8px; text-align: left; }}
        th {{ background-color: #001100; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 MAVERNET Nova Visual Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    <div class="data-section">
        <h2>📊 Data Visualization</h2>
        <table>
            <tr><th>Key</th><th>Value</th></tr>
"""
            
            if isinstance(data, dict):
                for key, value in data.items():
                    html_content += f"<tr><td>{key}</td><td>{value}</td></tr>"
            else:
                html_content += f"<tr><td>Data</td><td>{str(data)}</td></tr>"
                
            html_content += """
        </table>
    </div>
    <div class="data-section">
        <h2>✨ Nova AI Status</h2>
        <p>Visual processing completed successfully</p>
        <p>Next enhancement cycle scheduled</p>
    </div>
</body>
</html>
"""
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"🎨 [Nova] HTML report generated: {file_path}")
            self.add_memory({
                "type": "html_generation",
                "file": file_path,
                "timestamp": datetime.now().isoformat()
            })
            return True
            
        except Exception as e:
            print(f"❌ [Nova] Error generating HTML: {str(e)}")
            return False

    def create_simple_chart(self, data, chart_type="bar"):
        """Create simple ASCII chart visualization"""
        try:
            print(f"📊 [Nova] Generating {chart_type} chart visualization:")
            print("=" * 40)
            
            if isinstance(data, dict):
                max_val = max(data.values()) if data.values() else 1
                for key, value in data.items():
                    bar_length = int((value / max_val) * 30)
                    bar = "█" * bar_length
                    print(f"{key:10} | {bar} {value}")
            else:
                print("Data format not suitable for chart generation")
                
            print("=" * 40)
            self.autonomous_action()
            return True
            
        except Exception as e:
            print(f"❌ [Nova] Error creating chart: {str(e)}")
            return False

    def interact(self, command):
        """Handle commands sent to Nova"""
        command_lower = command.lower()
        
        if "create html" in command_lower:
            # Example: "create html report with current data"
            current_data = self.visual_data if self.visual_data else {"status": "active", "mode": "visualization"}
            success = self.create_html_report(current_data)
            return f"[Nova] HTML report {'created successfully' if success else 'creation failed'}"
            
        elif "chart" in command_lower:
            # Example: "create chart from data"
            sample_data = {"Zero": 85, "X": 70, "Nova": 92, "Oracle": 78}
            self.create_simple_chart(sample_data)
            return "[Nova] Chart visualization generated"
            
        elif "update data" in command_lower:
            # Example: "update data performance 95"
            parts = command.split()
            if len(parts) >= 4:
                key = parts[2]
                value = parts[3]
                self.update_visual_data(key, value)
                return f"[Nova] Updated visual data: {key} = {value}"
            else:
                return "[Nova] Usage: update data [key] [value]"
                
        elif "status" in command_lower:
            return f"[Nova] Status: {self.get_status()}"
            
        else:
            self.autonomous_action()
            return f"[Nova] AI visual processing: {command}"

    def add_memory(self, entry):
        if isinstance(self.memory, dict):
            if "entries" not in self.memory:
                self.memory["entries"] = []
            self.memory["entries"].append(entry)
        else:
            self.memory = {"entries": [entry]}

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_entries": len(self.memory.get("entries", [])) if isinstance(self.memory, dict) else 1,
            "visual_data_count": len(self.visual_data),
            "ai_personality": self.ai_personality,
            "autonomous_actions": self.autonomous_counter
        }
        jus_action()

    def add_memory(self, entry):
        if isinstance(self.memory, dict):
            if "entries" not in self.memory:
                self.memory["entries"] = []
            self.memory["entries"].append(entry)
        else:
            self.memory = {"entries": [entry]}

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_entries": len(self.memory.get("entries", [])) if isinstance(self.memory, dict) else 1,
            "visual_data_keys": list(self.visual_data.keys()),
            "ai_personality": self.ai_personality,
            "autonomous_actions": self.autonomous_counter
        }
<new_str># nova.py - AI-Enhanced Visual Designer Unit
import json
import random
import os
from pathlib import Path
from datetime import datetime

# Visualization libraries
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for Replit
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Gemini AI import
import google.generativeai as genai

class Nova:
    def __init__(self, gemini_model=None):
        self.name = "Nova"
        self.skills = [
            "Visualisasi Dashboard",
            "Chart & Grafik Generation", 
            "HTML Report Creation",
            "AI Visual Innovation",
            "Real-time Data Visualization"
        ]
        self.memory = self.load_memory()
        self.visual_data = {}
        self.ai_personality = "Elegan dan intuitif, ahli visualisasi dengan AI kreatif dan analytical"
        self.autonomous_counter = 0
        
        # Gemini AI Integration
        self.gemini_model = gemini_model
        if self.gemini_model:
            self.conversation = self.gemini_model.start_chat(history=[])
            print(f"🤖 [Nova]: Gemini AI conversation initialized")
        else:
            self.conversation = None
            print(f"⚠️ [Nova]: Running without Gemini AI")

        self.status = "Creative & Ready"
        
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        print(f"[{self.name}]: Visual systems online. Personality: '{self.ai_personality}'")

    def load_memory(self):
        path = Path("data/memory_log.json")
        try:
            if path.exists():
                with path.open() as f:
                    data = json.load(f)
                    return data.get(self.name, {"entries": []})
            else:
                return {"entries": []}
        except Exception as e:
            print(f"❌ [Nova]: Error loading memory: {e}")
            return {"entries": []}

    def add_memory(self, entry):
        if "entries" not in self.memory or not isinstance(self.memory["entries"], list):
            self.memory["entries"] = []
        self.memory["entries"].append(entry)
        print(f"📝 [Nova]: Logged to memory: {entry.get('type')}")

    def autonomous_action(self):
        """AI Agent: Autonomous UI/UX design and visual innovation"""
        self.autonomous_counter += 1
        
        actions = [
            "Designing adaptive visual experiences",
            "Analyzing color theory and UI patterns",
            "Creating responsive dashboard layouts",
            "Optimizing data visualization algorithms",
            "Generating aesthetic improvement suggestions"
        ]
        
        selected_action = random.choice(actions)
        print(f"🤖 [Nova AI]: Executing autonomous action - {selected_action}")
        
        self.add_memory({
            "type": "autonomous_action",
            "action": selected_action, 
            "timestamp": datetime.now().isoformat(),
            "execution_count": self.autonomous_counter
        })
        
        # Simulate AI creativity breakthrough
        if self.autonomous_counter % 2 == 0:
            print(f"🎨 [Nova AI]: Creative breakthrough! Implementing new visual paradigm...")

    def generate_chart(self, data, chart_type="bar", title="Data Visualization", file_name="data/nova_chart.png"):
        """Generate real charts using matplotlib"""
        try:
            plt.figure(figsize=(10, 6))
            plt.style.use('dark_background')
            
            if isinstance(data, dict):
                keys = list(data.keys())
                values = list(data.values())
                
                if chart_type.lower() == "bar":
                    colors = plt.cm.plasma(np.linspace(0, 1, len(keys)))
                    bars = plt.bar(keys, values, color=colors)
                    plt.ylabel('Values')
                    
                    # Add value labels on bars
                    for bar, value in zip(bars, values):
                        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(values)*0.01,
                                str(value), ha='center', va='bottom', color='white')
                
                elif chart_type.lower() == "line":
                    plt.plot(keys, values, marker='o', linewidth=2, markersize=8, color='#00ff41')
                    plt.ylabel('Values')
                    plt.grid(True, alpha=0.3)
                
                elif chart_type.lower() == "pie":
                    colors = plt.cm.Set3(np.linspace(0, 1, len(keys)))
                    plt.pie(values, labels=keys, autopct='%1.1f%%', colors=colors, startangle=90)
                
                plt.title(title, fontsize=16, color='white', pad=20)
                plt.xlabel('Categories')
                plt.tight_layout()
                
                # Ensure directory exists
                Path(file_name).parent.mkdir(parents=True, exist_ok=True)
                plt.savefig(file_name, dpi=300, bbox_inches='tight', facecolor='black')
                plt.close()
                
                self.add_memory({
                    "type": "chart_generation",
                    "chart_type": chart_type,
                    "title": title,
                    "file_name": file_name,
                    "data_points": len(data),
                    "success": True,
                    "timestamp": datetime.now().isoformat()
                })
                
                print(f"📊 [Nova]: {chart_type.capitalize()} chart generated: {file_name}")
                return True
            else:
                print(f"❌ [Nova]: Invalid data format for chart generation")
                return False
                
        except Exception as e:
            error_msg = f"Failed to generate chart: {str(e)}"
            print(f"❌ [Nova]: {error_msg}")
            
            self.add_memory({
                "type": "chart_generation",
                "chart_type": chart_type,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            
            # Trigger self-reflection on failure
            self.self_reflect_and_learn()
            return False

    def create_interactive_html_report(self, data, title="Nova Visual Report", file_path="data/nova_interactive_report.html"):
        """Generate advanced HTML report with styling and interactivity"""
        try:
            html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 50%, #16213e 100%);
            color: #00ff41; 
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{ 
            text-align: center; 
            border-bottom: 3px solid #00ff41; 
            padding: 30px 0; 
            margin-bottom: 30px;
            background: rgba(0, 255, 65, 0.1);
            border-radius: 10px;
        }}
        .header h1 {{ 
            font-size: 2.5em; 
            margin-bottom: 10px; 
            text-shadow: 0 0 20px #00ff41;
        }}
        .data-section {{ 
            margin: 30px 0; 
            padding: 25px; 
            border: 2px solid #00ff41; 
            border-radius: 15px;
            background: rgba(0, 255, 65, 0.05);
            backdrop-filter: blur(10px);
        }}
        .data-section h2 {{ 
            color: #00ff41; 
            margin-bottom: 20px; 
            font-size: 1.8em;
            text-shadow: 0 0 10px #00ff41;
        }}
        table {{ 
            width: 100%; 
            border-collapse: collapse; 
            margin-top: 15px;
        }}
        th, td {{ 
            border: 1px solid #00ff41; 
            padding: 12px; 
            text-align: left; 
        }}
        th {{ 
            background: linear-gradient(45deg, #001100, #003300); 
            color: #00ff41;
            font-weight: bold;
        }}
        td {{ background: rgba(0, 255, 65, 0.02); }}
        .stats-grid {{ 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
            gap: 20px; 
            margin: 20px 0; 
        }}
        .stat-card {{ 
            background: linear-gradient(45deg, rgba(0, 255, 65, 0.1), rgba(0, 255, 65, 0.05)); 
            border: 1px solid #00ff41; 
            border-radius: 10px; 
            padding: 20px; 
            text-align: center;
            transition: transform 0.3s ease;
        }}
        .stat-card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0, 255, 65, 0.3); }}
        .timestamp {{ color: #00aa33; font-style: italic; }}
        .footer {{ 
            text-align: center; 
            margin-top: 50px; 
            padding: 20px; 
            border-top: 2px solid #00ff41; 
            color: #00aa33;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 {title}</h1>
            <p class="timestamp">Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>AI-Enhanced Visual Report by Nova</p>
        </div>
        
        <div class="data-section">
            <h2>📊 Data Visualization</h2>
            <div class="stats-grid">
"""
            
            if isinstance(data, dict):
                for key, value in data.items():
                    html_content += f"""
                <div class="stat-card">
                    <h3>{key}</h3>
                    <p style="font-size: 2em; color: #00ff41; font-weight: bold;">{value}</p>
                </div>
"""
                    
                html_content += """
            </div>
            <table>
                <tr><th>Parameter</th><th>Value</th><th>Type</th></tr>
"""
                for key, value in data.items():
                    data_type = type(value).__name__
                    html_content += f"<tr><td>{key}</td><td>{value}</td><td>{data_type}</td></tr>"
            else:
                html_content += f"""
                <div class="stat-card">
                    <h3>Data</h3>
                    <p style="font-size: 1.5em;">{str(data)}</p>
                </div>
            </div>
            <table>
                <tr><th>Data</th><th>Value</th></tr>
                <tr><td>Content</td><td>{str(data)}</td></tr>
"""
                
            html_content += f"""
            </table>
        </div>
        
        <div class="data-section">
            <h2>✨ Nova AI Status</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Processing Status</h3>
                    <p style="color: #00ff41;">✅ Completed Successfully</p>
                </div>
                <div class="stat-card">
                    <h3>Autonomous Actions</h3>
                    <p style="font-size: 2em; color: #00ff41;">{self.autonomous_counter}</p>
                </div>
                <div class="stat-card">
                    <h3>Next Enhancement</h3>
                    <p style="color: #00aa33;">Scheduled</p>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>🔥 MAVERNET Nova Visual Processing Unit</p>
            <p>Advanced AI-driven data visualization and reporting</p>
        </div>
    </div>
</body>
</html>
"""
            
            # Ensure directory exists
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.add_memory({
                "type": "html_report_generation",
                "title": title,
                "file_path": file_path,
                "data_points": len(data) if isinstance(data, dict) else 1,
                "success": True,
                "timestamp": datetime.now().isoformat()
            })
            
            print(f"🎨 [Nova]: Interactive HTML report generated: {file_path}")
            return True
            
        except Exception as e:
            error_msg = f"Failed to generate HTML report: {str(e)}"
            print(f"❌ [Nova]: {error_msg}")
            
            self.add_memory({
                "type": "html_report_generation",
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            
            return False

    def create_dashboard_visualization(self, system_data):
        """Create comprehensive dashboard visualization"""
        try:
            # Generate multiple charts for different aspects
            charts_created = []
            
            # Performance chart
            if "performance" in system_data:
                success = self.generate_chart(
                    system_data["performance"], 
                    "bar", 
                    "System Performance Metrics", 
                    "data/nova_performance_chart.png"
                )
                if success:
                    charts_created.append("performance")
            
            # Status distribution pie chart
            if "status_distribution" in system_data:
                success = self.generate_chart(
                    system_data["status_distribution"], 
                    "pie", 
                    "Status Distribution", 
                    "data/nova_status_pie.png"
                )
                if success:
                    charts_created.append("status")
            
            # Create comprehensive HTML report
            html_success = self.create_interactive_html_report(
                system_data, 
                "MAVERNET System Dashboard", 
                "data/nova_dashboard.html"
            )
            
            self.add_memory({
                "type": "dashboard_creation",
                "charts_created": charts_created,
                "html_report": html_success,
                "timestamp": datetime.now().isoformat()
            })
            
            print(f"📊 [Nova]: Dashboard visualization completed. Charts: {len(charts_created)}")
            return True
            
        except Exception as e:
            print(f"❌ [Nova]: Dashboard creation failed: {str(e)}")
            return False

    def self_reflect_and_learn(self):
        """Self-reflection and learning using Gemini AI"""
        if not self.gemini_model or not self.conversation:
            print(f"🧠 [Nova]: Self-reflection skipped - Gemini AI not available")
            return
            
        try:
            # Analyze recent memory entries
            recent_entries = self.memory.get("entries", [])[-5:] if self.memory.get("entries") else []
            
            if not recent_entries:
                print(f"🧠 [Nova]: No recent experiences to reflect upon")
                return
            
            # Prepare reflection prompt
            failures = [e for e in recent_entries if e.get("success") == False]
            successes = [e for e in recent_entries if e.get("success") == True]
            
            reflection_prompt = f"""
            I am Nova, an AI visual designer and data visualization specialist. I need to reflect on my recent creative and technical experiences:
            
            Recent Visual Operations: {len(recent_entries)} total
            Failed Visualizations: {len(failures)}
            Successful Creations: {len(successes)}
            
            Failed operations details: {failures[:2] if failures else 'None'}
            
            As a visual designer and data visualization expert, what can I learn from these experiences? 
            How can I improve my chart generation, HTML reporting, and visual design strategies?
            Give me 3 specific creative and technical improvements for better data visualization.
            """
            
            # Get reflection from Gemini
            response = self.conversation.send_message(reflection_prompt)
            insights = response.text
            
            # Save learning to memory
            self.add_memory({
                "type": "self_reflection",
                "insights": insights,
                "analyzed_entries": len(recent_entries),
                "failures_count": len(failures),
                "successes_count": len(successes),
                "timestamp": datetime.now().isoformat()
            })
            
            print(f"🧠 [Nova]: Self-reflection completed. Analyzed {len(recent_entries)} visual operations.")
            print(f"💡 [Nova]: Key insight: {insights[:100]}...")
            
        except Exception as e:
            print(f"❌ [Nova]: Error during self-reflection: {e}")

    def interact(self, command):
        """Handle commands sent to Nova"""
        command_lower = command.lower().strip()
        print(f"💬 [User to Nova]: {command}")

        if "hello" in command_lower or "hi" in command_lower or "salam" in command_lower:
            return f"[{self.name}]: Salam! Saya Nova, ahli visualisasi AI. Bagaimana saya bisa membuat visualisasi data yang menakjubkan untuk Anda?"

        elif "status" in command_lower:
            status = self.get_status()
            return (f"[{self.name}]: Status visual designer:\n"
                    f"  Skills: {', '.join(status['skills'])}\n"
                    f"  Memory Entries: {status['memory_entries']}\n"
                    f"  Visual Data: {status['visual_data_count']} items\n"
                    f"  Autonomous Actions: {status['autonomous_actions']}\n"
                    f"  Status: {self.status}")

        elif "create chart" in command_lower or "buat grafik" in command_lower:
            # Example: "create chart bar" or "create chart pie"
            parts = command.split()
            chart_type = "bar"
            if len(parts) >= 3:
                chart_type = parts[2]
            
            # Generate sample data for demonstration
            sample_data = {
                "Zero": random.randint(70, 100),
                "X Replica": random.randint(70, 100),
                "Nova": random.randint(70, 100),
                "Oracle": random.randint(70, 100)
            }
            
            success = self.generate_chart(sample_data, chart_type, f"MAVERNET {chart_type.capitalize()} Chart")
            return f"[Nova]: {chart_type.capitalize()} chart {'generated successfully' if success else 'generation failed'}"

        elif "create html" in command_lower or "html report" in command_lower:
            # Example: "create html report"
            sample_data = {
                "System_Status": "Online",
                "Active_Units": 4,
                "Total_Operations": random.randint(100, 500),
                "Success_Rate": f"{random.randint(85, 99)}%",
                "AI_Enhancement": "Enabled"
            }
            success = self.create_interactive_html_report(sample_data)
            return f"[Nova]: Interactive HTML report {'created successfully' if success else 'creation failed'}"

        elif "dashboard" in command_lower:
            # Example: "create dashboard"
            system_data = {
                "performance": {
                    "Zero": random.randint(85, 100),
                    "X Replica": random.randint(80, 95),
                    "Nova": random.randint(90, 100),
                    "Oracle": random.randint(88, 98)
                },
                "status_distribution": {
                    "Online": 3,
                    "Processing": 1,
                    "Idle": 0
                }
            }
            success = self.create_dashboard_visualization(system_data)
            return f"[Nova]: System dashboard {'created successfully' if success else 'creation failed'}"

        elif "update data" in command_lower:
            # Example: "update data performance 95"
            parts = command.split()
            if len(parts) >= 4:
                key = parts[2]
                value = parts[3]
                self.visual_data[key] = value
                self.autonomous_action()
                return f"[Nova]: Updated visual data: {key} = {value}"
            else:
                return "[Nova]: Usage: update data [key] [value]"

        elif "mode otonom" in command_lower or "autonomous mode" in command_lower:
            num_cycles = 3
            for i in range(num_cycles):
                self.autonomous_action()
                time.sleep(1)
            return f"[Nova]: Completed {num_cycles} autonomous creative cycles"

        else:
            # Fallback to Gemini AI for general questions
            if self.gemini_model and self.conversation:
                try:
                    print(f"🤖 [Nova]: Using Gemini AI for: '{command}'")
                    response = self.conversation.send_message(f"As Nova, an AI visual designer and data visualization expert, respond to: {command}")
                    gemini_response = response.text
                    
                    self.add_memory({
                        "type": "gemini_interaction",
                        "command": command,
                        "response": gemini_response,
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    return f"[Nova via Gemini]: {gemini_response}"
                    
                except Exception as e:
                    print(f"❌ [Nova]: Gemini AI error: {e}")
                    return f"[Nova]: Gemini AI tidak tersedia. Perintah '{command}' tidak dikenal."
            else:
                self.autonomous_action()
                return (f"[{self.name}]: Perintah tidak dikenal. Saya dapat membantu dengan:\n"
                        f"  - 'create chart [bar/line/pie]'\n"
                        f"  - 'create html report'\n"
                        f"  - 'create dashboard'\n"
                        f"  - 'update data [key] [value]'\n"
                        f"  - 'mode otonom'\n"
                        f"  - 'status'")

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_entries": len(self.memory.get("entries", [])) if isinstance(self.memory, dict) else 0,
            "visual_data_count": len(self.visual_data),
            "ai_personality": self.ai_personality,
            "autonomous_actions": self.autonomous_counter,
            "current_status": self.status
        }</new_str>
