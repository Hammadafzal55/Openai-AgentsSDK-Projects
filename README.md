# 🚀 OpenAI Agents SDK Projects

Welcome to the **OpenAI Agents SDK Projects** repository! This collection showcases practical implementations of agentic workflows using the **OpenAI Agents SDK**. Each project demonstrates different aspects of modern AI agent development—from simple multi-agent systems to enterprise-grade applications with guardrails.

---

## 📚 Project Collection

### 🍔 Fast-food Restaurant AI Agent System

A beginner-friendly introduction to multi-agent systems featuring:
- **Two-Agent Architecture**: Main Agent (classifier) + Order Agent (executor)
- **Dynamic Tool Switching**: Context-aware tools for pizza vs burger orders
- **Business Logic Integration**: Automatic shop hours enforcement (9 AM - 9 PM)
- **Structured Validation**: Pydantic models for reliable data extraction

**Perfect for learning**: Agent handoffs, conditional tool execution, and basic workflow orchestration.

**Navigate to**: [Fast-food Restaurant Project](./Fast-food%20Restaurant%20Project%20-%20Openai%20Agent-SDK/)

---

### 🏦 Bank Environment AI Agent System

An enterprise-grade customer service simulation featuring:
- **Modular Architecture**: Separated concerns (guardrails, tools, agents)
- **Multi-Agent Orchestration**: Greeting agent delegates to specialists (Account, Transfer, Loan)
- **Dual-Layer Guardrails**: Input guardrails (abuse detection) + Output guardrails (topic compliance)
- **Token Queue System**: Real-world service queue simulation with wait time management
- **Service Routing**: Intent-based routing with confidence thresholds

**Perfect for learning**: Modular code organization, guardrails, handoffs, and complex workflows.

**Navigate to**: [Bank Environment Project](./Bank%20Environment%20Project%20-%20Openai%20Agent-SDK/)

---

## 🛠️ Technical Stack (Common to All Projects)

| Technology | Purpose |
|------------|---------|
| **OpenAI Agents SDK** (v0.6.4+) | Core agentic framework for orchestrating agents and tools |
| **uv** | Lightning-fast Python package manager |
| **Python 3.13+** | Runtime environment |
| **Google Gemini 2.5 Flash** | Default LLM (via OpenAI-compatible endpoint) |
| **python-dotenv** | Environment variable management |
| **rich** | Beautiful terminal formatting and color-coded output |

---

## 🔑 LLM Provider Flexibility

Both projects are designed with **provider flexibility** in mind:

### Current Setup: Gemini
Uses Google Gemini 2.5 Flash through an OpenAI-compatible endpoint for speed and efficiency.

### Switch to OpenAI (Simple & Clean)
Just provide the model name as a string to any Agent definition:
```python
agent = Agent(
    name="My Agent",
    instructions="...",
    model="gpt-4o" # That's it! No extra configuration needed.
)
```

The SDK automatically detects your `OPENAI_API_KEY` from the environment and handles the rest. No need for `AsyncOpenAI` or `OpenAIChatCompletionsModel` wrappers.

---

## 🚀 Getting Started with Any Project

All projects use **uv** for dependency management.

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd Openai-AgentsSDK-Projects
   ```

2. **Choose a project**:
   ```bash
   cd "Fast-food Restaurant Project"
   # OR
   cd "Bank Environment Project"
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

4. **Configure API key**:
   Create a `.env` file in the project directory:
   ```env
   GEMINI_API_KEY=your_key_here
   # OR
   OPENAI_API_KEY=your_key_here
   ```

5. **Run**:
   ```bash
   uv run main.py
   ```

---

## 📊 Learning Path

| Project | Difficulty | Concepts Covered |
|---------|------------|-------------------|
| **Fast-food Restaurant** | Beginner | Multi-agent basics, handoffs, conditional tools, business logic |
| **Bank Environment** | Intermediate | Guardrails, modular architecture, complex routing, enterprise patterns |

---

## 🌟 Key Concepts Demonstrated

### Across Both Projects
- ✅ Multi-agent orchestration and handoffs
- ✅ Structured output with Pydantic models
- ✅ Function tools with conditional execution
- ✅ Async/await patterns for concurrent operations
- ✅ Context-aware agent behavior

### Bank Environment (Advanced)
- 🛡️ Input Guardrails (abuse/profanity detection)
- 🛡️ Output Guardrails (topic compliance enforcement)
- 🏗️ Modular code organization
- 🎯 Intent-based service routing
- 🔐 Enterprise-grade safety layers

---

## 📖 Resources

- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-agents-python)
- [uv Package Manager](https://github.com/astral-sh/uv)
- [Google Gemini API](https://ai.google.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

---

## 🤝 Contributing

This is an educational repository showcasing real-world agent implementations. Feel free to explore, modify, and learn from the code.

---

*Built with ❤️ using OpenAI Agents SDK, Python 3.13, and modern AI best practices*
