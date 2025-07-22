# 🛍️ Smart Store Agent

**Smart Store Agent** is an AI-powered virtual assistant built using the [OpenAI Agents SDK](https://github.com/openai/agents). It recommends products based on natural language input — whether you’re looking for office furniture, kitchen gadgets, travel accessories, or fitness equipment.

This implementation uses **Gemini via OpenAI-compatible API** and is powered by the `uv` package manager for fast virtual environments and dependency installation.

---

## 📂 File: `product_suggester.py`

This file defines a single intelligent agent configured at the **agent level**, leveraging Gemini's OpenAI-compatible endpoint to interpret user needs and suggest relevant products with short explanations.

---

## 🚀 Features

* 💬 Understands natural product queries (e.g., "I need a desk lamp and a comfy chair").
* 📦 Suggests specific items with brand/model when appropriate.
* 🧠 Explains product relevance in 1–2 sentences.
* 🔄 Handles multi-item queries gracefully with clean formatting.
* ⚡ Uses `uv` for modern, fast Python environment management.

---

## 🧪 Example Usage

```bash
$ python product_suggester.py
How can I help you today? I’m looking for a keyboard, a good webcam, and a desk lamp.

🤖 Product Suggestions:
1. **Keychron K2 Wireless Keyboard** – Offers tactile feedback with Bluetooth support, ideal for both Mac and Windows users.
2. **Logitech C920 HD Pro Webcam** – Full HD video and excellent low-light performance, great for meetings and content creation.
3. **BenQ ScreenBar LED Lamp** – Reduces eye strain with auto-dimming and saves desk space with a monitor-mounted design.
```

---

## 🛠️ Setup & Installation

### ✅ 1. Initialize your project using `uv`

```bash
uv init
```

This creates a `.venv` folder with a virtual environment.

---

### ✅ 2. Install dependencies

```bash
uv add openai-agents python-dotenv
```

---

### ✅ 3. Activate the virtual environment

```bash
.venv\Scripts\activate  # For Windows
# OR
source .venv/bin/activate  # For macOS/Linux
```

---

### ✅ 4. Set your Gemini API Key

Create a `.env` file in the root of your project:

```
GEMINI_API_KEY=your-gemini-api-key-here
```

And update `product_suggester.py` to load it:

```python
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
```

---

## ⚙️ Agent Configuration

The agent is defined with detailed instructions to:

* Understand the user’s needs.
* Suggest one or more relevant products.
* Justify each recommendation clearly.

---

## 🙋‍♂️ Author

**Syed Hasnain Ali Shah**
[GitHub](https://github.com/HasnainDevMaster) | [LinkedIn](https://linkedin.com/in/syed-hasnain-ali-shah-a80428252)

---
