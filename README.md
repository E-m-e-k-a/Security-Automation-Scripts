# SOC Python Tools

## 📊 Project Overview

Collection of Python automation scripts designed to streamline Security Operations Center (SOC) workflows and improve analyst efficiency. These tools automate routine security tasks, enhance decision-making processes, and demonstrate practical application of programming in cybersecurity operations.

---

## 🎯 Purpose

Built to address common SOC analyst challenges:
- Alert fatigue from high-volume monitoring
- Inconsistent severity prioritization
- Manual triage processes
- Time-consuming routine tasks

These tools provide automated, consistent, and scalable solutions for security operations.

---

## 🛠️ Tools Included

### 1. Alert Severity Calculator

**Purpose:** Automates alert severity scoring and prioritization for SOC Level 1 analysts

**Functionality:**
- Calculates severity scores based on multiple factors
- Provides consistent prioritization methodology
- Reduces human error in alert triage
- Speeds up incident response decision-making

**Scoring Algorithm:**

**Alert Type Scoring:**
- Malware: +30 points (highest threat)
- Phishing: +25 points
- Unauthorized Access: +25 points
- Brute Force: +20 points
- Unknown/Other: +10 points

**Failed Attempts Scoring:**
- 500+ attempts: +20 points (active attack)
- 100-499 attempts: +15 points
- 10-99 attempts: +10 points
- 1-9 attempts: +5 points

**Affected Systems Scoring:**
- 5+ systems: +20 points (widespread)
- 2-4 systems: +10 points
- 1 system: +5 points

**Priority Classification:**
- **HIGH:** Score 61+ (immediate action required)
- **MEDIUM:** Score 31-60 (timely investigation needed)
- **LOW:** Score 0-30 (routine monitoring)

**Usage:**
```bash
python alert_severity_calculator.py
```

**Input Required:**
- Alert type (malware/phishing/brute_force/unauthorized_access)
- Source IP address
- Number of failed attempts
- Number of affected systems

**Output:**
- Calculated severity score
- Priority level classification
- Complete alert summary

---

## 💡 Technical Concepts Demonstrated

**Python Fundamentals:**
- User input handling with validation
- Conditional logic (if/elif/else statements)
- Variable operations and scoring algorithms
- String formatting (f-strings)
- Output formatting for readability

**Security Operations Concepts:**
- Alert triage methodology
- Severity scoring frameworks
- Incident prioritization
- SOC workflow automation

---

## 🎓 Skills Development

**Programming Skills:**
- Python scripting for automation
- Algorithm design and implementation
- User interface design (CLI)
- Code organization and readability

**Cybersecurity Skills:**
- Understanding SOC analyst workflows
- Alert classification methodologies
- Incident response prioritization
- Security operations automation

---

## 📈 Future Enhancements

**Planned Features:**
- Machine learning for adaptive scoring
- Integration with SIEM platforms (Splunk, ELK)
- Threat intelligence feed correlation
- Historical alert database
- Automated alert escalation
- Email/Slack notifications
- CSV export for reporting
- Multi-user support with role-based access

---

## 🔧 Requirements

**Python Version:** 3.6+

**Dependencies:** None (uses only standard library)

**Installation:**
```bash
git clone https://github.com/E-m-e-k-a/SOC-Python-Tools.git
cd SOC-Python-Tools
python alert_severity_calculator.py
```

---

## 📝 Usage Examples

**Example 1: High Severity Alert**
Alert type: malware
Source IP: 192.168.1.100
Failed attempts: 600
Affected systems: 10
Result: HIGH severity (Score: 75)

**Example 2: Medium Severity Alert**
Alert type: phishing
Source IP: 10.0.0.50
Failed attempts: 150
Affected systems: 2
Result: MEDIUM severity (Score: 50)

**Example 3: Low Severity Alert**
Alert type: brute_force
Source IP: 172.16.0.10
Failed attempts: 5
Affected systems: 1
Result: LOW severity (Score: 30)

---

## 🎯 Learning Outcomes

**From Building These Tools:**
- Practical application of Python in cybersecurity
- Understanding SOC operational workflows
- Automation mindset for repetitive tasks
- Problem-solving through code
- Security operations optimization

---
---

### 2. Log Parser

**Purpose:** Automatically scans log files for suspicious activity patterns

**Functionality:**
- Reads any log file from system
- Scans against predefined suspicious patterns
- Displays numbered list of findings
- Handles errors gracefully
- Case-insensitive pattern matching

**Suspicious Patterns Detected:**
- Failed authentication attempts
- Invalid user access
- Denied/blocked connections
- System errors and warnings
- Web attack signatures (SQL injection, directory traversal)
- Network scanning activity

**Usage:**
```bash
python log_parser.py
```

**Input Required:**
- Path to log file

**Output:**
- Total entries scanned
- Number of suspicious entries found
- Numbered list of suspicious log lines

**Example:**
```
==================================================
SOC Log Parser
==================================================

Enter log file path: /var/log/auth.log

✅ Successfully loaded 150 log entries
🔍 Scanning for 20 suspicious patterns...

==================================================
SCAN RESULTS
==================================================
Total log entries scanned: 150
Suspicious entries found: 3
==================================================

🚨 SUSPICIOUS ENTRIES:
--------------------------------------------------
1. Jun 8 13:15:23 kali sshd: Failed password for root from 192.168.1.100
2. Jun 8 13:15:24 kali sshd: Invalid user admin from 192.168.1.100
3. Jun 8 13:15:25 kali kernel: iptables DENIED IN=eth0 SRC=45.33.32.156

==================================================
Scan Complete!
==================================================
```

## 📞 Contact

**GitHub:** [@E-m-e-k-a](https://github.com/E-m-e-k-a)

**Portfolio:** Building practical cybersecurity tools and automation solutions

**Date:** May 2026

---

## 📄 License

Educational project - Free to use and modify for learning purposes

---

**⭐ Building automation tools for modern SOC operations**
