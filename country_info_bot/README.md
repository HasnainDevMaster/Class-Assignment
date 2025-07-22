# 🌍 Country Info Bot

**Country Info Bot** is a CLI tool built with the OpenAI Agents SDK and Gemini (via OpenAI‑compatible API) that answers country‑specific queries in three areas:

1. **Capital Finder** – returns the capital city  
2. **Language Finder** – returns the official or most common language(s)  
3. **Population Finder** – returns the approximate population  

An **Orchestrator Agent** ties these three “tool” agents together, invokes them in sequence, and summarizes the results in a friendly paragraph.

---

## 📁 File: `country_info_toolkit.py`

Contains:

- Loading `GEMINI_API_KEY` from a `.env` file  
- Configuring the `AsyncOpenAI` client for Gemini  
- Defining three agents (`Capital Finder`, `Language Finder`, `Population Finder`) and converting them to tools via `.as_tool()`  
- Defining an Orchestrator Agent that calls the three tools in order and aggregates results  
- A simple async `main()` that prompts the user and prints the summary  

---

## 🚀 Features

- 🏷️ **Modular**: Each piece of information (capital, language, population) is its own agent‑tool.  
- 🤖 **Orchestration**: A single “triage” agent runs the three tools and produces a cohesive summary.  
- 🔐 **Secure**: API key stored in `.env` and loaded via `python‑dotenv`.  
- ⚡ **Fast setup** using the ultra‑light **uv** environment manager.  

---

## ⚙️ Setup & Installation

### 1. Initialize project & virtual environment

```bash
uv init
````

This creates a `.venv` directory and activates a lightweight Python environment.

---

### 2. Install dependencies

```bash
uv add openai-agents python-dotenv openai
```

---

### 3. Activate the virtual environment

```bash
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

---

### 4. Configure your API key

Create a file named `.env` in the project root:

```text
GEMINI_API_KEY=your-gemini-api-key-here
```

---

## 🧪 Usage

Run the script with:

```bash
uv run country_info_toolkit.py
```

You will be prompted:

```text
🌍 Enter a country name:
```

Type a country (e.g. `Japan`) and press **Enter**. You’ll see:

```text
🔎 Gathering data...

📘 Country Summary:

Capital Finder says the capital of Japan is Tokyo.
Language Finder says the official language is Japanese.
Population Finder says the population is around 125 million people.

Japan is a beautiful island nation in East Asia. Its dynamic capital, Tokyo, is known for blending cutting‑edge technology with traditional culture. The primary language spoken is Japanese, and it is home to approximately 125 million people.
```

---

## 🙋‍♂️ Author

**Syed Hasnain Ali Shah**
[GitHub](https://github.com/HasnainDevMaster) | [LinkedIn](https://linkedin.com/in/syed-hasnain-ali-shah-a80428252)

---