# 🔗 Attack Chain Framework

> CLI-based penetration testing framework for modeling, visualizing, and reporting OWASP Top 10 attack chains.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## Overview

The **Attack Chain Framework** is a CLI tool built for web application penetration testers and security researchers. It models real-world attack scenarios by chaining OWASP Top 10 vulnerabilities together, maps them to the cyber kill chain, and generates automated Markdown reports with Graphviz visualizations.

Built as a team project by cybersecurity students, this tool bridges the gap between vulnerability discovery and structured reporting.

## Features

- 🧠 **Attack Chain Modeling** — Graph-theory-based vulnerability chaining using NetworkX
- ⚔️ **Kill Chain Mapping** — Maps attack steps to Lockheed Martin Cyber Kill Chain phases
- 📊 **Graphviz Visualization** — Auto-generates visual attack path diagrams
- 📝 **Markdown Report Generation** — One-click professional pentest reports
- 🖥️ **Interactive CLI** — Menu-driven interface with ASCII banner

## Installation

```bash
git clone https://github.com/mdAqibb/attach-chain-framework.git
cd attach-chain-framework
pip install networkx graphviz
```

> Make sure [Graphviz](https://graphviz.org/download/) is also installed on your system.

## Usage

```bash
python main.py

# or load a vulnerability file directly:
python main.py --input vulnerabilities.json
```

**Menu Options:**
1. Load vulnerability JSON file
2. Build attack chain
3. Visualize attack chain
4. Generate report
5. Exit

## Vulnerability File Format

```json
[
  {"name": "SQL Injection", "severity": "Critical", "cvss": 9.8},
  {"name": "Broken Authentication", "severity": "High", "cvss": 7.5},
  {"name": "XSS", "severity": "Medium", "cvss": 6.1}
]
```

## Output

| File | Description |
|---|---|
| `output/attack_chain.png` | Visual attack chain graph |
| `output/report.md` | Full penetration testing report |

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.8+ |
| Graph Engine | NetworkX |
| Visualization | Graphviz |
| Report Format | Markdown |

## Author

**Mohammed Aqib** & Team  
[LinkedIn](https://www.linkedin.com/in/88maqib/) • [GitHub](https://github.com/mdAqibb)

---

> ⚠️ Built for educational purposes and **authorized** penetration testing only. Always obtain written permission before testing any system.
