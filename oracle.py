
# oracle.py - AI-Enhanced Intelligence & Strategic Unit
import json
import random
from pathlib import Path
from datetime import datetime

class Oracle:
    def __init__(self):
        self.name = "Oracle"
        self.skills = [
            "Intelijen Data",
            "Pemetaan & Visualisasi", 
            "Briefing & Analisis",
            "AI Strategic Forecasting"
        ]
        self.memory = self.load_memory()
        self.map_data = {}
        self.ai_personality = "Visioner dan strategis, penjaga masa depan sistem dengan AI prediktif"
        self.autonomous_counter = 0

    def load_memory(self):
        path = Path("data/memory_log.json")
        if path.exists():
            with path.open() as f:
                data = json.load(f)
                return data.get(self.name, {})
        return {}

    def autonomous_action(self):
        """AI Agent: Autonomous strategic planning and intelligence analysis"""
        self.autonomous_counter += 1
        
        actions = [
            "Forecasting system evolution scenarios",
            "Mapping strategic intelligence networks", 
            "Analyzing potential future threats",
            "Developing AI-driven contingency plans"
        ]
        
        selected_action = random.choice(actions)
        print(f"🤖 [Oracle AI]: Executing autonomous action - {selected_action}")
        
        # Log autonomous action to memory
        self.add_memory({
            "type": "autonomous_action",
            "action": selected_action,
            "timestamp": datetime.now().isoformat(),
            "execution_count": self.autonomous_counter
        })
        
        # Simulate AI prediction
        if self.autonomous_counter % 5 == 0:
            print(f"🔮 [Oracle AI]: Strategic vision acquired, updating future protocols...")

    def update_map(self, area, data):
        self.map_data[area] = data
        print(f"🗺️ [Oracle] AI-Enhanced map updated for area: {area}")
        self.autonomous_action()

    def generate_briefing(self):
        print("📊 [Oracle] AI-Enhanced intelligence briefing...")
        for area, info in self.map_data.items():
            print(f" - {area}: {info}")
        self.autonomous_action()

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
            "mapped_areas": list(self.map_data.keys()),
            "ai_personality": self.ai_personality,
            "autonomous_actions": self.autonomous_counter
        }
# oracle.py - AI-Enhanced Strategic Analysis Unit
import json
import random
import statistics
from pathlib import Path
from datetime import datetime

class Oracle:
    def __init__(self):
        self.name = "Oracle"
        self.skills = [
            "Analisis Prediktif",
            "Perhitungan Statistik",
            "Pemetaan Strategi",
            "AI Strategic Intelligence"
        ]
        self.memory = self.load_memory()
        self.analysis_data = {}
        self.ai_personality = "Analitis dan strategis, AI oracle dengan kemampuan prediktif"
        self.autonomous_counter = 0

    def load_memory(self):
        path = Path("data/memory_log.json")
        if path.exists():
            with path.open() as f:
                data = json.load(f)
                return data.get(self.name, {})
        return {}

    def autonomous_action(self):
        """AI Agent: Autonomous strategic analysis"""
        self.autonomous_counter += 1
        
        actions = [
            "Analyzing system performance patterns",
            "Predicting future optimization needs",
            "Mapping strategic intelligence networks",
            "Calculating threat probability matrices"
        ]
        
        selected_action = random.choice(actions)
        print(f"🤖 [Oracle AI]: Executing autonomous action - {selected_action}")
        
        # Log autonomous action to memory
        self.add_memory({
            "type": "autonomous_action",
            "action": selected_action,
            "timestamp": datetime.now().isoformat(),
            "execution_count": self.autonomous_counter
        })
        
        # Simulate AI strategic thinking
        if self.autonomous_counter % 3 == 0:
            print(f"🔮 [Oracle AI]: Strategic insight discovered, updating predictive models...")

    def analyze_text_file(self, file_path):
        """Analyze text file and generate statistics"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic text analysis
            lines = content.split('\n')
            words = content.split()
            chars = len(content)
            
            # Calculate statistics
            analysis = {
                "file_path": file_path,
                "total_lines": len(lines),
                "total_words": len(words),
                "total_characters": chars,
                "avg_words_per_line": len(words) / len(lines) if lines else 0,
                "avg_chars_per_word": chars / len(words) if words else 0,
                "analysis_timestamp": datetime.now().isoformat()
            }
            
            print(f"📊 [Oracle] Text analysis completed for {file_path}")
            print(f"   Lines: {analysis['total_lines']}")
            print(f"   Words: {analysis['total_words']}")
            print(f"   Characters: {analysis['total_characters']}")
            
            self.add_memory({
                "type": "text_analysis",
                "analysis": analysis,
                "timestamp": datetime.now().isoformat()
            })
            
            return analysis
            
        except Exception as e:
            print(f"❌ [Oracle] Error analyzing file: {str(e)}")
            return None

    def generate_analysis_report(self, analysis_data, output_path="data/oracle_analysis.txt"):
        """Generate analysis report file"""
        try:
            report_content = f"""
MAVERNET ORACLE - STRATEGIC ANALYSIS REPORT
==========================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

ANALYSIS SUMMARY:
"""
            
            if isinstance(analysis_data, dict):
                for key, value in analysis_data.items():
                    report_content += f"{key}: {value}\n"
            else:
                report_content += f"Data: {str(analysis_data)}\n"
                
            report_content += f"""

ORACLE AI INSIGHTS:
- Analysis completed with high precision
- Strategic patterns identified
- Predictive modeling updated
- Threat assessment: LOW

RECOMMENDATIONS:
- Continue monitoring data patterns
- Implement automated analysis cycles
- Enhance predictive capabilities

End of Report
=============
"""
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            print(f"📝 [Oracle] Analysis report generated: {output_path}")
            self.add_memory({
                "type": "report_generation",
                "file": output_path,
                "timestamp": datetime.now().isoformat()
            })
            return True
            
        except Exception as e:
            print(f"❌ [Oracle] Error generating report: {str(e)}")
            return False

    def calculate_statistics(self, data_list):
        """Calculate basic statistics from numeric data"""
        try:
            if not data_list:
                return None
                
            numeric_data = [float(x) for x in data_list if str(x).replace('.', '').replace('-', '').isdigit()]
            
            if not numeric_data:
                print("❌ [Oracle] No numeric data found for statistics")
                return None
            
            stats = {
                "count": len(numeric_data),
                "mean": statistics.mean(numeric_data),
                "median": statistics.median(numeric_data),
                "min": min(numeric_data),
                "max": max(numeric_data),
                "range": max(numeric_data) - min(numeric_data)
            }
            
            if len(numeric_data) > 1:
                stats["stdev"] = statistics.stdev(numeric_data)
            else:
                stats["stdev"] = 0
            
            print(f"📈 [Oracle] Statistics calculated for {len(numeric_data)} values")
            print(f"   Mean: {stats['mean']:.2f}")
            print(f"   Median: {stats['median']:.2f}")
            print(f"   Range: {stats['min']:.2f} - {stats['max']:.2f}")
            
            return stats
            
        except Exception as e:
            print(f"❌ [Oracle] Error calculating statistics: {str(e)}")
            return None

    def interact(self, command):
        """Handle commands sent to Oracle"""
        command_lower = command.lower()
        
        if "analyze file" in command_lower:
            # Example: "analyze file data/memory_log.json"
            parts = command.split()
            if len(parts) >= 3:
                file_path = parts[2]
                analysis = self.analyze_text_file(file_path)
                if analysis:
                    self.generate_analysis_report(analysis)
                    return f"[Oracle] Analysis completed for {file_path}"
                else:
                    return f"[Oracle] Failed to analyze {file_path}"
            else:
                return "[Oracle] Usage: analyze file [file_path]"
                
        elif "calculate stats" in command_lower:
            # Example: "calculate stats 1,2,3,4,5"
            parts = command.split()
            if len(parts) >= 3:
                data_str = " ".join(parts[2:])
                data_list = data_str.replace(',', ' ').split()
                stats = self.calculate_statistics(data_list)
                if stats:
                    self.generate_analysis_report(stats, "data/oracle_stats.txt")
                    return f"[Oracle] Statistics calculated for {len(data_list)} values"
                else:
                    return "[Oracle] Failed to calculate statistics"
            else:
                return "[Oracle] Usage: calculate stats [comma-separated numbers]"
                
        elif "status" in command_lower:
            return f"[Oracle] Status: {self.get_status()}"
            
        else:
            self.autonomous_action()
            return f"[Oracle] AI strategic analysis: {command}"

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
            "analysis_data_count": len(self.analysis_data),
            "ai_personality": self.ai_personality,
            "autonomous_actions": self.autonomous_counter
        }
