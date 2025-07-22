# 😌 Mood Analyzer with Activity Handoff

**Mood Analyzer with Handoff** is an intelligent, two-agent system that detects a user's emotional state and suggests a personalized activity if their mood is negative. It leverages the **OpenAI Agents SDK**, uses **Gemini** via OpenAI-compatible API, and is managed with the ultra-fast **uv** environment manager.

---

## 📂 File: `mood_handoff.py`

This Python script creates:

* A **Mood Analyzer Agent** to classify user emotion from free text.
* An **Activity Suggester Agent** to offer comforting or helpful suggestions when a negative emotion is detected.

The system uses `Runner.run()` to connect the agents in a logical handoff sequence.

---

## 🧠 What It Can Do

* ✅ Understands a user's emotional state from natural language input.
* 🧠 Detects mood in one word: e.g., **happy**, **sad**, **stressed**, **bored**, etc.
* 🎯 If a **negative** mood is detected, hands off to a second agent.
* 💡 Suggests specific, mood-based activities with short and supportive explanations.

---

## 🧪 Example Interaction

```bash
$ python mood_handoff.py
🗣️  How are you feeling today?
> I’ve been overwhelmed with tasks and can’t focus anymore.

🔎 Running agent: Mood Analyzer

🧠 Detected Mood: Stressed

🔎 Running agent: Activity Suggester for mood 'stressed'

🎯 Suggested Activity:
Try taking a short 10-minute walk outside. It helps clear your mind, reduce tension, and improve focus through movement and fresh air.
```

---

## 🛠️ Setup & Installation (with uv)

### ✅ 1. Initialize your project

```bash
uv init
```

This creates a fast, isolated `.venv` environment.

---

### ✅ 2. Install dependencies

```bash
uv add openai-agents python-dotenv
```

---

### ✅ 3. Activate the environment

```bash
.venv\Scripts\activate  # For Windows
# OR
source .venv/bin/activate  # For macOS/Linux
```

---

### ✅ 4. Add your Gemini API key

Create a `.env` file in your project root:

```
GEMINI_API_KEY=your-gemini-api-key-here
```

The script automatically loads it via `python-dotenv`.

---

## ⚙️ How It Works

1. The user provides a natural language statement (e.g., "I'm feeling lost lately").
2. The **Mood Analyzer Agent** replies with a single-word emotion like `sad`, `anxious`, or `hopeful`.
3. If the emotion is negative, the **Activity Suggester Agent** recommends a tailored activity to help.
4. Output is printed in a user-friendly format with support and empathy.

---

## 🔍 Code Structure Summary

* `Agent(name="Mood Analyzer", instructions=...)` – detects mood
* `Agent(name="Activity Suggester", instructions=...)` – provides suggestions
* `.env` stores your Gemini API key securely
* `Runner.run()` executes both agents in a clear async flow
* `Error handling` ensures graceful failure

---

## 🙋‍♂️ Author

**Syed Hasnain Ali Shah**
[GitHub](https://github.com/HasnainDevMaster) | [LinkedIn](https://linkedin.com/in/syed-hasnain-ali-shah-a80428252)

---
