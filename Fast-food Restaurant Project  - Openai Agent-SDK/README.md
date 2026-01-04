# 🍔 Fast-food Restaurant AI Agent System

Welcome to the **Fast-food Restaurant AI Agent System**! This repository demonstrates a high-performance, multi-agent workflow built with the **OpenAI Agents SDK**. Designed as a modern solution for automated order management, the system intelligently handles customer requests, validates orders, and manages kitchen status updates.

---

## 🌟 Why This project?

This isn't just a simple chatbot. It's a structured **Agentic Workflow** that uses:
- **Intelligent Routing**: A gatekeeper agent deciphers customer intent before passing it to specialized agents.
- **Context-Aware Tools**: Tools that automatically "turn off" when the shop is closed or if they aren't relevant to the current order.
- **Type Safety**: Full Pydantic integration for reliable, structured data extraction.

---

## 🛠️ Technical Powerhouse

- **Framework**: [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) (v0.6.4+)
- **Package Management**: [uv](https://github.com/astral-sh/uv) (for lightning-fast dependency handling)
- **Runtime**: Python 3.13+
- **Styling**: `rich` for a beautiful, color-coded terminal experience.

---

## 🚀 Getting Started (Using `uv`)

This project is optimized for **uv**. If you don't have it yet, get it with: `pip install uv`.

1. **Clone & Enter**:
   ```bash
   git clone <repo-url>
   cd "Fast-food Restaurant Project"
   ```

2. **Sync Dependencies**:
   ```bash
   uv sync
   ```

3. **Configure Secrets**:
   Create a `.env` file:
   ```env
   GEMINI_API_KEY=your_gemini_key
   # OR
   OPENAI_API_KEY=your_openai_key
   ```

4. **Launch the Agent**:
   ```bash
   uv run main.py
   ```

---

## 🔄 Dual-Model Flexibility (Gemini & OpenAI)

The system is configured to use **Gemini 2.5 Flash** by default because of its speed and efficiency, but switching to native **OpenAI** is now simpler than ever thanks to the Agents SDK.

### Option 1: Gemini (Current Setup)
We use a specialized client to bridge Gemini into the OpenAI SDK:
```python
# Uses AsyncOpenAI with custom base_url
model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client)
```

### Option 2: OpenAI (The "Simple" Way) 🚀
If you want to use OpenAI, you can strip away the extra configuration. The Agents SDK will automatically find your `OPENAI_API_KEY` from the environment.

**Just update your model assignment:**
```python
# Simple and Clean
main_agent = Agent(
    ...,
    model="gpt-4o", # Simply provide the model name string
)
```
*No need for `AsyncOpenAI` or `OpenAIChatCompletionsModel` wrappers—the SDK handles it!*

---

## 🧠 System Architecture

### 1. The Gatekeeper (Main Agent)
Uses an `Order_Checker` schema to analyze every word the customer says.
- **Is it an order?** If yes, it extracts the `order_type` and `quantity`.
- **Is it a greeting or a complaint?** It captures the `reason` and responds appropriately.

### 2. The Specialist (Order Agent)
Only comes into play once an order is validated.
- **Dynamic Tools**: Only shows `pizza_order` if the user wants pizza.
- **Business Logic**: Automatically checks if `is_bussiness_hours()` (9 AM - 9 PM) is true. If not, the `shop_closed` tool takes over!

---

## 📂 Project Structure
```text
.
├── main.py              # The Brain: Main Agent & Classification
├── order_agent.py       # The Muscle: Order Agent & Order Tools
├── pyproject.toml       # UV Project Configuration
├── .env                 # Your Secrets (Keys)
└── uv.lock              # Deterministic Dependency Map
```

---

## 🍔 Try an Order!
> "I want to buy 3 delicious burgers"

**Result:**
1. **Main Agent** confirms it's a burger order with quantity 3.
2. **Order Agent** triggers `burger_order` tool.
3. **Response**: *"Your Burger is cooking... please wait for just 10 minutes. Would you like to add some fries or a drink?"*

---
*Built with ❤️ using OpenAI Agents SDK and Python 3.13*
