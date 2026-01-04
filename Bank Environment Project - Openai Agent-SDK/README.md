# 🏦 Bank Environment AI Agent System

Welcome to the **Bank Environment AI Agent System**! This is a sophisticated multi-agent banking assistant built with the **OpenAI Agents SDK**. The system simulates an intelligent customer service environment for banks, complete with specialized agents, input/output guardrails, and dynamic tool-based service routing.

---

## 🌟 Why This Project?

This project demonstrates a complete **Enterprise-Grade Agentic System** featuring:

- **Multi-Agent Orchestration**: A greeting agent that smartly delegates to specialized experts (Account, Transfer, Loan).
- **Guardrail Protection**: Dual-layer security with Input Guardrails (abuse detection) and Output Guardrails (topic compliance).
- **Tool-Based Routing**: Intelligent service identification that routes customers to the right specialist based on intent.
- **Token Queue Management**: Simulates real-world banking token systems for service queueing.

---

## 🛠️ Technical Stack

- **Framework**: [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) (v0.6.4+)
- **Package Management**: [uv](https://github.com/astral-sh/uv) (ultra-fast dependency management)
- **Runtime**: Python 3.13+
- **LLM Provider**: Google Gemini 2.5 Flash (via OpenAI-compatible endpoint)
- **UI/UX**: `rich` library for polished terminal output with colors and formatting

---

## 🏗️ Modular Architecture

The codebase is organized into **modular components** for maintainability and scalability:

```
.
├── main.py                  # Entry point & Greeting Agent
├── input_guardrail.py       # Abuse/Slang detection for user input
├── output_guardrail.py      # Banking-topic compliance for LLM output
├── tools.py                 # Service identification & token generation
├── handoff_agents.py        # Specialist agents (Account, Transfer, Loan)
├── pyproject.toml           # UV project configuration
├── .env                     # API keys
└── uv.lock                  # Dependency lock file
```

### Modules Overview

| Module | Responsibility |
|--------|----------------|
| `input_guardrail.py` | Validates user input, blocks abusive/slang language |
| `output_guardrail.py` | Ensures agent responses stay within banking domain |
| `tools.py` | Service intent analysis & token queue generation |
| `handoff_agents.py` | Specialized experts for specific banking domains |
| `main.py` | Orchestrator: Greeting agent with handoffs and guardrails |

---

## 🚀 Getting Started (Using `uv`)

This project is optimized for **uv**. If you don't have it yet: `pip install uv`.

1. **Clone & Enter**:

   ```bash
   git clone <repo-url>
   cd "Bank Environment Project"
   ```

2. **Sync Dependencies**:

   ```bash
   uv sync
   ```

3. **Configure Secrets**:
   Create a `.env` file:

   ```env
   GEMINI_API_KEY=your_gemini_key
   ```

4. **Run the System**:

   ```bash
   uv run main.py
   ```

---

## 🔄 LLM Provider Switching

### Gemini (Current Default)

Uses `AsyncOpenAI` with custom base_url for Gemini compatibility:

```python
client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client)
```

### OpenAI (The "Simple" Way) 🚀

To use OpenAI, simply provide the model name as a string:

```python
# Update each Agent definition in all modules
account_agent = Agent(
    name="Account Services Agent",
    instructions="...",
    model="gpt-4o", # Simply use the model string!
)
```

*No `AsyncOpenAI` or `OpenAIChatCompletionsModel` wrapper needed—the SDK handles it!*

---

## 🧠 System Architecture

### 1. The Greeting Agent (Orchestrator)

- **Role**: First point of contact, welcomes customers
- **Features**:
  - Uses `identify_banking_purpose` tool to understand customer intent
  - Routes to specialist agents when confidence > 0.8
  - Generates queue tokens for all customers
  - Protected by input guardrails (abuse detection)

### 2. Specialist Agents (Handoffs)

- **Account Agent**: Handles balance inquiries, statements, account info
- **Transfer Agent**: Manages money transfers and payments
- **Loan Agent**: Processes loan and mortgage queries (protected by output guardrails)

### 3. Guardrail System

- **Input Guardrail**: Blocks abusive/slang user input with `check_slangs`
- **Output Guardrail**: Ensures Loan Agent responses stay banking-focused with `res_check`

### 4. Tools

- `identify_banking_purpose`: Analyzes customer request and classifies service type
- `generate_customer_token`: Creates queue tokens with wait times based on service type

---

## 🛡️ Guardrail Behavior

### Input Guardrail (Abuse Detection)

If user input contains abusive or slang language:

```text
❌Input Guardrail Triggered: Detected abusive language
```

### Output Guardrail (Topic Compliance)

If the Loan Agent responds with non-banking content:

```text
❌Output Guardrail Triggered: Response not banking-related
```

---

## 🎯 Try It Out

**Example 1 - Balance Inquiry**:
> "I want to check my account balance"

**Response**:

1. Greeting agent identifies `account_service`
2. Handoffs to Account Agent
3. Generates token: `ACC123` (Wait: 5-10 minutes)

**Example 2 - Loan Query**:
> "I need help with a mortgage"

**Response**:

1. Greeting agent identifies `loan_service`
2. Handoffs to Loan Agent
3. Output guardrail validates response stays banking-focused
4. Generates token: `LOA456` (Wait: 15-20 minutes)

**Example 3 - Abuse Detection**:
> "What the [expletive] is wrong with this service?"

**Response**:

```text
❌Input Guardrail Triggered: Abusive language detected
```

---

## 📦 Service Type Codes

| Service Type | Prefix | Wait Time | Description |
|--------------|--------|-----------|-------------|
| General | GEN | 10-15 min | Default/general inquiries |
| Account Service | ACC | 5-10 min | Balance, statements, account info |
| Transfer Service | TRF | 2-5 min | Money transfers, payments |
| Loan Service | LOA | 15-20 min | Loans, mortgages, credit |

---

*Built with ❤️ using OpenAI Agents SDK, Python 3.13, and Enterprise Guardrails*
