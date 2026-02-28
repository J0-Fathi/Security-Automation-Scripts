# 🔐 Simple SOC Log Analyzer

A beginner-level Python project that simulates a simple SOC (Security Operations Center) log analysis tool.

This tool:
- Reads login logs from a JSON file
- Counts failed login attempts per user
- Detects suspicious users (3+ failed attempts)
- Assigns risk levels (LOW / MEDIUM / HIGH)
- Generates a terminal-style security report

---

## 🚀 Features

- JSON Log File Input
- Failed Login Counter
- Suspicious User Detection
- Risk Level Classification
- Metasploit-style Terminal Output

---
## How to Run
python .\log.py

## Outut Sample
("Output.jpg")
---

## 📂 Example JSON Log Format

```json
[
  {"user": "ali", "status": "failed"},
  {"user": "ali", "status": "failed"},
  {"user": "mona", "status": "success"},
  {"user": "ahmed", "status": "failed"}
]



