# 🤖 Agentic SDK Class Assignments

This repository contains three AI agent-based assignments built using the Agentic SDK. These assignments demonstrate how to create intelligent agents, perform agent handoffs, and integrate tool-based functionality.

## 📂 Assignments Overview

### 1️⃣ Smart Store Agent - `product_suggester.py`
An intelligent agent that suggests a relevant product (e.g., medicine) based on the user's described need.  
**Example:** User says, *“I have a headache”* → agent suggests a suitable remedy and explains the reasoning.

### 2️⃣ Mood Analyzer with Handoff - `mood_handoff.py`
A two-agent system:
- **Agent 1:** Detects user's mood from a message (happy, sad, stressed, etc.)
- **Agent 2:** If mood is sad or stressed, recommends an uplifting activity.
Uses `Runner.run()` for executing both agents with output logging.

### 3️⃣ Country Info Bot (with Tools) - `country_info_toolkit.py`
A multi-tool agent system:
- Tools: Capital finder, language identifier, population retriever.
- An orchestrator agent takes a country name and provides all three details by utilizing individual tools.
