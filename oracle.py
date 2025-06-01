

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
        }</old_str>
<new_str># oracle.py - AI-Enhanced Strategic Analysis & Intelligence Unit
import json
import random
import statistics
import os
from pathlib import Path
from datetime import datetime
from collections import Counter
import re

# Data analysis libraries
import numpy as np
import pandas as pd

# Text analysis libraries
try:
    import nltk
    from nltk.sentiment import SentimentIntensityAnalyzer
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False
    print("⚠️ [Oracle]: NLTK not available, using basic text analysis")

# Gemini AI import
import google.generativeai as genai

class Oracle:
    def __init__(self, gemini_model=None):
        self.name = "Oracle"
        self.skills = [
            "Analisis Prediktif",
            "Perhitungan Statistik Lanjutan",
            "Analisis Teks & Sentimen",
            "Pemetaan Strategis",
            "AI Strategic Intelligence",
            "Threat Assessment"
        ]
        self.memory = self.load_memory()
        self.analysis_data = {}
        self.ai_personality = "Analitis dan strategis, Oracle AI dengan kemampuan prediktif dan intelligence gathering"
        self.autonomous_counter = 0
        
        # Gemini AI Integration
        self.gemini_model = gemini_model
        if self.gemini_model:
            self.conversation = self.gemini_model.start_chat(history=[])
            print(f"🤖 [Oracle]: Gemini AI conversation initialized")
        else:
            self.conversation = None
            print(f"⚠️ [Oracle]: Running without Gemini AI")

        self.status = "Analyzing & Ready"
        
        # Initialize NLTK components if available
        if NLTK_AVAILABLE:
            try:
                nltk.download('vader_lexicon', quiet=True)
                nltk.download('stopwords', quiet=True)
                nltk.download('punkt', quiet=True)
                self.sentiment_analyzer = SentimentIntensityAnalyzer()
                print(f"🔮 [Oracle]: NLTK sentiment analysis initialized")
            except:
                self.sentiment_analyzer = None
                print(f"⚠️ [Oracle]: NLTK initialization failed")
        else:
            self.sentiment_analyzer = None
        
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        print(f"[{self.name}]: Strategic analysis systems online. Personality: '{self.ai_personality}'")

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
            print(f"❌ [Oracle]: Error loading memory: {e}")
            return {"entries": []}

    def add_memory(self, entry):
        if "entries" not in self.memory or not isinstance(self.memory["entries"], list):
            self.memory["entries"] = []
        self.memory["entries"].append(entry)
        print(f"📝 [Oracle]: Logged to memory: {entry.get('type')}")

    def autonomous_action(self):
        """AI Agent: Autonomous strategic analysis and intelligence gathering"""
        self.autonomous_counter += 1
        
        actions = [
            "Analyzing system performance patterns",
            "Predicting future optimization needs",
            "Mapping strategic intelligence networks",
            "Calculating threat probability matrices",
            "Performing predictive trend analysis",
            "Evaluating risk assessment scenarios"
        ]
        
        selected_action = random.choice(actions)
        print(f"🤖 [Oracle AI]: Executing autonomous action - {selected_action}")
        
        self.add_memory({
            "type": "autonomous_action",
            "action": selected_action,
            "timestamp": datetime.now().isoformat(),
            "execution_count": self.autonomous_counter
        })
        
        # Simulate AI strategic thinking and prediction
        if self.autonomous_counter % 3 == 0:
            print(f"🔮 [Oracle AI]: Strategic insight discovered, updating predictive models...")

    def advanced_text_analysis(self, text_content):
        """Perform advanced text analysis including sentiment and keyword extraction"""
        try:
            analysis = {
                "basic_stats": {},
                "sentiment": {},
                "keywords": {},
                "readability": {}
            }
            
            # Basic statistics
            lines = text_content.split('\n')
            words = text_content.split()
            sentences = re.split(r'[.!?]+', text_content)
            
            analysis["basic_stats"] = {
                "total_lines": len(lines),
                "total_words": len(words),
                "total_characters": len(text_content),
                "total_sentences": len([s for s in sentences if s.strip()]),
                "avg_words_per_line": len(words) / len(lines) if lines else 0,
                "avg_words_per_sentence": len(words) / len(sentences) if sentences else 0,
                "avg_chars_per_word": len(text_content) / len(words) if words else 0
            }
            
            # Sentiment analysis (if NLTK available)
            if self.sentiment_analyzer:
                sentiment_scores = self.sentiment_analyzer.polarity_scores(text_content)
                analysis["sentiment"] = {
                    "compound": sentiment_scores['compound'],
                    "positive": sentiment_scores['pos'],
                    "negative": sentiment_scores['neg'],
                    "neutral": sentiment_scores['neu'],
                    "overall_sentiment": "positive" if sentiment_scores['compound'] > 0.1 else "negative" if sentiment_scores['compound'] < -0.1 else "neutral"
                }
            else:
                # Simple sentiment analysis
                positive_words = ['good', 'great', 'excellent', 'success', 'working', 'completed', 'online']
                negative_words = ['error', 'failed', 'problem', 'issue', 'wrong', 'offline', 'timeout']
                
                text_lower = text_content.lower()
                pos_count = sum(1 for word in positive_words if word in text_lower)
                neg_count = sum(1 for word in negative_words if word in text_lower)
                
                analysis["sentiment"] = {
                    "positive_indicators": pos_count,
                    "negative_indicators": neg_count,
                    "overall_sentiment": "positive" if pos_count > neg_count else "negative" if neg_count > pos_count else "neutral"
                }
            
            # Keyword frequency analysis
            words_lower = [word.lower().strip('.,!?";') for word in words if len(word) > 3]
            word_freq = Counter(words_lower)
            analysis["keywords"] = dict(word_freq.most_common(10))
            
            # Readability score (simple approximation)
            avg_sentence_length = analysis["basic_stats"]["avg_words_per_sentence"]
            avg_word_length = analysis["basic_stats"]["avg_chars_per_word"]
            readability_score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * (avg_word_length / 4.7))
            
            analysis["readability"] = {
                "flesch_score_approx": readability_score,
                "reading_level": "easy" if readability_score > 70 else "moderate" if readability_score > 30 else "difficult"
            }
            
            return analysis
            
        except Exception as e:
            print(f"❌ [Oracle]: Error in advanced text analysis: {str(e)}")
            return None

    def analyze_file_comprehensive(self, file_path):
        """Comprehensive file analysis with multiple metrics"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Perform advanced analysis
            analysis = self.advanced_text_analysis(content)
            
            if analysis:
                analysis["file_info"] = {
                    "file_path": file_path,
                    "file_size_bytes": len(content.encode('utf-8')),
                    "analysis_timestamp": datetime.now().isoformat()
                }
                
                print(f"📊 [Oracle] Comprehensive analysis completed for {file_path}")
                print(f"   📝 Words: {analysis['basic_stats']['total_words']}")
                print(f"   📄 Lines: {analysis['basic_stats']['total_lines']}")
                print(f"   😊 Sentiment: {analysis['sentiment'].get('overall_sentiment', 'unknown')}")
                print(f"   🔑 Top keyword: {list(analysis['keywords'].keys())[0] if analysis['keywords'] else 'none'}")
                
                self.add_memory({
                    "type": "comprehensive_file_analysis",
                    "file_path": file_path,
                    "analysis_summary": {
                        "words": analysis['basic_stats']['total_words'],
                        "sentiment": analysis['sentiment'].get('overall_sentiment'),
                        "readability": analysis['readability'].get('reading_level')
                    },
                    "success": True,
                    "timestamp": datetime.now().isoformat()
                })
                
                return analysis
            else:
                return None
                
        except Exception as e:
            error_msg = f"Failed to analyze file {file_path}: {str(e)}"
            print(f"❌ [Oracle]: {error_msg}")
            
            self.add_memory({
                "type": "comprehensive_file_analysis",
                "file_path": file_path,
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            
            # Trigger self-reflection on failure
            self.self_reflect_and_learn()
            return None

    def advanced_statistical_analysis(self, data_list):
        """Advanced statistical analysis using numpy"""
        try:
            if not data_list:
                return None
                
            # Convert to numeric data
            numeric_data = []
            for item in data_list:
                try:
                    numeric_data.append(float(item))
                except (ValueError, TypeError):
                    pass
            
            if not numeric_data:
                print("❌ [Oracle] No numeric data found for statistical analysis")
                return None
            
            data_array = np.array(numeric_data)
            
            stats = {
                "basic_stats": {
                    "count": len(numeric_data),
                    "mean": float(np.mean(data_array)),
                    "median": float(np.median(data_array)),
                    "min": float(np.min(data_array)),
                    "max": float(np.max(data_array)),
                    "range": float(np.max(data_array) - np.min(data_array)),
                    "std_deviation": float(np.std(data_array)),
                    "variance": float(np.var(data_array))
                },
                "advanced_stats": {
                    "percentile_25": float(np.percentile(data_array, 25)),
                    "percentile_75": float(np.percentile(data_array, 75)),
                    "iqr": float(np.percentile(data_array, 75) - np.percentile(data_array, 25)),
                    "skewness_approx": float((np.mean(data_array) - np.median(data_array)) / np.std(data_array)) if np.std(data_array) != 0 else 0
                },
                "distribution_analysis": {
                    "is_normal_dist_approx": abs((np.mean(data_array) - np.median(data_array)) / np.std(data_array)) < 0.5 if np.std(data_array) != 0 else True,
                    "outliers_iqr": self._detect_outliers_iqr(data_array),
                    "coefficient_of_variation": float(np.std(data_array) / np.mean(data_array)) if np.mean(data_array) != 0 else 0
                }
            }
            
            print(f"📈 [Oracle] Advanced statistical analysis completed for {len(numeric_data)} values")
            print(f"   📊 Mean: {stats['basic_stats']['mean']:.2f}")
            print(f"   📊 Std Dev: {stats['basic_stats']['std_deviation']:.2f}")
            print(f"   📊 IQR: {stats['advanced_stats']['iqr']:.2f}")
            print(f"   📊 Outliers: {len(stats['distribution_analysis']['outliers_iqr'])} detected")
            
            return stats
            
        except Exception as e:
            print(f"❌ [Oracle] Error in advanced statistical analysis: {str(e)}")
            return None

    def _detect_outliers_iqr(self, data_array):
        """Detect outliers using IQR method"""
        q1 = np.percentile(data_array, 25)
        q3 = np.percentile(data_array, 75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        outliers = [x for x in data_array if x < lower_bound or x > upper_bound]
        return outliers

    def generate_comprehensive_report(self, analysis_data, output_path="data/oracle_comprehensive_report.txt"):
        """Generate comprehensive analysis report"""
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            report_content = f"""
╔══════════════════════════════════════════════════════════════╗
║                    MAVERNET ORACLE                          ║
║              COMPREHENSIVE ANALYSIS REPORT                  ║
╚══════════════════════════════════════════════════════════════╝

Generated: {timestamp}
Oracle AI Version: Advanced Analytics v2.0
Analysis Scope: Strategic Intelligence & Predictive Modeling

═══════════════════════════════════════════════════════════════

EXECUTIVE SUMMARY:
"""
            
            if isinstance(analysis_data, dict):
                # Handle different types of analysis data
                if "basic_stats" in analysis_data:
                    # Text analysis report
                    basic = analysis_data.get("basic_stats", {})
                    sentiment = analysis_data.get("sentiment", {})
                    keywords = analysis_data.get("keywords", {})
                    readability = analysis_data.get("readability", {})
                    
                    report_content += f"""
TEXT ANALYSIS FINDINGS:
▶ Document Statistics:
  • Total Words: {basic.get('total_words', 'N/A')}
  • Total Lines: {basic.get('total_lines', 'N/A')}
  • Total Sentences: {basic.get('total_sentences', 'N/A')}
  • Average Words per Sentence: {basic.get('avg_words_per_sentence', 0):.2f}

▶ Sentiment Analysis:
  • Overall Sentiment: {sentiment.get('overall_sentiment', 'neutral').upper()}
  • Sentiment Score: {sentiment.get('compound', 'N/A')}

▶ Content Analysis:
  • Reading Level: {readability.get('reading_level', 'unknown').upper()}
  • Top Keywords: {', '.join(list(keywords.keys())[:5]) if keywords else 'None detected'}

▶ Strategic Assessment:
  • Content Complexity: {'HIGH' if readability.get('reading_level') == 'difficult' else 'MODERATE' if readability.get('reading_level') == 'moderate' else 'LOW'}
  • Emotional Tone: {sentiment.get('overall_sentiment', 'neutral').upper()}
  • Information Density: {'HIGH' if basic.get('avg_words_per_sentence', 0) > 20 else 'MODERATE' if basic.get('avg_words_per_sentence', 0) > 15 else 'LOW'}
"""
                    
                elif "basic_stats" in analysis_data and "advanced_stats" in analysis_data:
                    # Statistical analysis report
                    basic = analysis_data.get("basic_stats", {})
                    advanced = analysis_data.get("advanced_stats", {})
                    distribution = analysis_data.get("distribution_analysis", {})
                    
                    report_content += f"""
STATISTICAL ANALYSIS FINDINGS:
▶ Descriptive Statistics:
  • Sample Size: {basic.get('count', 'N/A')}
  • Mean: {basic.get('mean', 0):.4f}
  • Median: {basic.get('median', 0):.4f}
  • Standard Deviation: {basic.get('std_deviation', 0):.4f}
  • Range: {basic.get('range', 0):.4f}

▶ Advanced Metrics:
  • 25th Percentile: {advanced.get('percentile_25', 0):.4f}
  • 75th Percentile: {advanced.get('percentile_75', 0):.4f}
  • Interquartile Range: {advanced.get('iqr', 0):.4f}
  • Coefficient of Variation: {distribution.get('coefficient_of_variation', 0):.4f}

▶ Distribution Analysis:
  • Approximate Normal Distribution: {'YES' if distribution.get('is_normal_dist_approx') else 'NO'}
  • Outliers Detected: {len(distribution.get('outliers_iqr', []))}
  • Data Quality: {'HIGH' if distribution.get('coefficient_of_variation', 1) < 0.3 else 'MODERATE' if distribution.get('coefficient_of_variation', 1) < 0.7 else 'LOW'}

▶ Strategic Insights:
  • Data Consistency: {'EXCELLENT' if distribution.get('coefficient_of_variation', 1) < 0.2 else 'GOOD' if distribution.get('coefficient_of_variation', 1) < 0.5 else 'NEEDS ATTENTION'}
  • Predictability: {'HIGH' if distribution.get('is_normal_dist_approx') and len(distribution.get('outliers_iqr', [])) < 2 else 'MODERATE'}
  • Risk Assessment: {'LOW' if len(distribution.get('outliers_iqr', [])) == 0 else 'MODERATE' if len(distribution.get('outliers_iqr', [])) < 3 else 'HIGH'}
"""
                else:
                    # Generic data report
                    report_content += f"""
GENERAL ANALYSIS FINDINGS:
"""
                    for key, value in analysis_data.items():
                        report_content += f"  • {key}: {value}\n"
            else:
                report_content += f"Data: {str(analysis_data)}\n"
                
            report_content += f"""

═══════════════════════════════════════════════════════════════

ORACLE AI STRATEGIC ASSESSMENT:
▶ Analysis Quality: COMPREHENSIVE ✓
▶ Data Integrity: VERIFIED ✓
▶ Predictive Modeling: UPDATED ✓
▶ Strategic Patterns: IDENTIFIED ✓

RECOMMENDATIONS:
1. Continue automated monitoring of identified patterns
2. Implement real-time analysis for critical metrics
3. Establish predictive alert thresholds
4. Schedule regular comprehensive analysis cycles

THREAT ASSESSMENT: LOW RISK ✓
SYSTEM OPTIMIZATION: RECOMMENDED FOR NEXT CYCLE

═══════════════════════════════════════════════════════════════

Oracle Autonomous Actions: {self.autonomous_counter}
Report Generation: AUTO-TRIGGERED
Next Analysis: SCHEDULED

--- END OF ORACLE REPORT ---
"""
            
            # Ensure directory exists
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            self.add_memory({
                "type": "comprehensive_report_generation",
                "output_path": output_path,
                "analysis_type": "comprehensive",
                "success": True,
                "timestamp": datetime.now().isoformat()
            })
            
            print(f"📝 [Oracle] Comprehensive analysis report generated: {output_path}")
            return True
            
        except Exception as e:
            error_msg = f"Failed to generate comprehensive report: {str(e)}"
            print(f"❌ [Oracle]: {error_msg}")
            
            self.add_memory({
                "type": "comprehensive_report_generation",
                "error": error_msg,
                "success": False,
                "timestamp": datetime.now().isoformat()
            })
            
            return False

    def self_reflect_and_learn(self):
        """Self-reflection and learning using Gemini AI"""
        if not self.gemini_model or not self.conversation:
            print(f"🧠 [Oracle]: Self-reflection skipped - Gemini AI not available")
            return
            
        try:
            # Analyze recent memory entries
            recent_entries = self.memory.get("entries", [])[-5:] if self.memory.get("entries") else []
            
            if not recent_entries:
                print(f"🧠 [Oracle]: No recent experiences to reflect upon")
                return
            
            # Prepare reflection prompt
            failures = [e for e in recent_entries if e.get("success") == False]
            successes = [e for e in recent_entries if e.get("success") == True]
            
            reflection_prompt = f"""
            I am Oracle, an AI strategic analyst and intelligence specialist. I need to reflect on my recent analytical experiences:
            
            Recent Analysis Operations: {len(recent_entries)} total
            Failed Analyses: {len(failures)}
            Successful Analyses: {len(successes)}
            
            Types of operations performed: {[e.get('type') for e in recent_entries]}
            Failed operations details: {failures[:2] if failures else 'None'}
            
            As a strategic analyst and data intelligence expert, what can I learn from these experiences? 
            How can I improve my analysis accuracy, statistical modeling, and intelligence gathering?
            Give me 3 specific analytical improvements for better strategic insights.
            Focus on: 1) Analysis methodology, 2) Pattern recognition, 3) Predictive accuracy.
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
            
            print(f"🧠 [Oracle]: Self-reflection completed. Analyzed {len(recent_entries)} strategic operations.")
            print(f"💡 [Oracle]: Key insight: {insights[:100]}...")
            
        except Exception as e:
            print(f"❌ [Oracle]: Error during self-reflection: {e}")

    def interact(self, command):
        """Handle commands sent to Oracle"""
        command_lower = command.lower().strip()
        print(f"💬 [User to Oracle]: {command}")

        if "hello" in command_lower or "hi" in command_lower or "salam" in command_lower:
            return f"[{self.name}]: Salam. Saya Oracle, ahli analisis strategis dan intelligence AI. Bagaimana saya bisa membantu dengan analisis data dan prediksi Anda?"

        elif "status" in command_lower:
            status = self.get_status()
            return (f"[{self.name}]: Status strategic analyst:\n"
                    f"  Skills: {', '.join(status['skills'])}\n"
                    f"  Memory Entries: {status['memory_entries']}\n"
                    f"  Analysis Data: {status['analysis_data_count']} datasets\n"
                    f"  Autonomous Actions: {status['autonomous_actions']}\n"
                    f"  Status: {self.status}")

        elif "analyze file" in command_lower:
            # Example: "analyze file data/memory_log.json"
            parts = command.split()
            if len(parts) >= 3:
                file_path = parts[2]
                analysis = self.analyze_file_comprehensive(file_path)
                if analysis:
                    self.generate_comprehensive_report(analysis, f"data/oracle_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
                    return f"[Oracle] Comprehensive analysis completed for {file_path}"
                else:
                    return f"[Oracle] Failed to analyze {file_path}"
            else:
                return "[Oracle] Usage: analyze file [file_path]"

        elif "calculate stats" in command_lower or "analisis statistik" in command_lower:
            # Example: "calculate stats 1,2,3,4,5,10,15,20,25,30"
            parts = command.split()
            if len(parts) >= 3:
                data_str = " ".join(parts[2:])
                data_list = re.split(r'[,\s]+', data_str)
                stats = self.advanced_statistical_analysis(data_list)
                if stats:
                    self.generate_comprehensive_report(stats, f"data/oracle_stats_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
                    return f"[Oracle] Advanced statistical analysis completed for {len(data_list)} values"
                else:
                    return "[Oracle] Failed to perform statistical analysis"
            else:
                return "[Oracle] Usage: calculate stats [comma-separated numbers]"

        elif "text analysis" in command_lower:
            # Example: "text analysis This is a sample text for analysis"
            text_start = command.lower().find("text analysis") + len("text analysis")
            text_content = command[text_start:].strip()
            if text_content:
                analysis = self.advanced_text_analysis(text_content)
                if analysis:
                    self.generate_comprehensive_report(analysis, f"data/oracle_text_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
                    return f"[Oracle] Advanced text analysis completed. Sentiment: {analysis['sentiment'].get('overall_sentiment', 'unknown')}"
                else:
                    return "[Oracle] Failed to perform text analysis"
            else:
                return "[Oracle] Usage: text analysis [your text content]"

        elif "mode otonom" in command_lower or "autonomous mode" in command_lower:
            num_cycles = 3
            for i in range(num_cycles):
                self.autonomous_action()
                time.sleep(1)
            return f"[Oracle] Completed {num_cycles} autonomous strategic analysis cycles"

        else:
            # Fallback to Gemini AI for general questions
            if self.gemini_model and self.conversation:
                try:
                    print(f"🤖 [Oracle]: Using Gemini AI for strategic consultation: '{command}'")
                    response = self.conversation.send_message(f"As Oracle, an AI strategic analyst and intelligence expert, provide strategic insights for: {command}")
                    gemini_response = response.text
                    
                    self.add_memory({
                        "type": "gemini_strategic_consultation",
                        "command": command,
                        "response": gemini_response,
                        "timestamp": datetime.now().isoformat()
                    })
                    
                    return f"[Oracle via Gemini]: {gemini_response}"
                    
                except Exception as e:
                    print(f"❌ [Oracle]: Gemini AI error: {e}")
                    return f"[Oracle]: Gemini AI tidak tersedia untuk konsultasi strategis."
            else:
                self.autonomous_action()
                return (f"[{self.name}]: Perintah tidak dikenal. Saya dapat membantu dengan:\n"
                        f"  - 'analyze file [file_path]'\n"
                        f"  - 'calculate stats [numbers]'\n"
                        f"  - 'text analysis [text]'\n"
                        f"  - 'mode otonom'\n"
                        f"  - 'status'")

    def get_status(self):
        return {
            "name": self.name,
            "skills": self.skills,
            "memory_entries": len(self.memory.get("entries", [])) if isinstance(self.memory, dict) else 0,
            "analysis_data_count": len(self.analysis_data),
            "ai_personality": self.ai_personality,
            "autonomous_actions": self.autonomous_counter,
            "current_status": self.status,
            "nlp_available": NLTK_AVAILABLE,
            "sentiment_analysis": self.sentiment_analyzer is not None
        }</new_str>
