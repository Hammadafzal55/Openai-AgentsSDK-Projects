import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
import rich
from input_guardrail import check_slangs
from tools import identify_banking_purpose, generate_customer_token
from handoff_agents import account_agent, transfer_agent, loan_agent

#---------------------------------------------------------------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#---------------------------------------------------------------------------------
agent = Agent(
    name="Bank greeting Agent",
    instructions=
    """
    You are a friendly Bank grating agent.

    1. Welcome customer nicely.

    2. Use identify_banking_purpose to understand user need.

    3. If confidence > 0.8 send user to the side specialist

    4.  Always use generate_customer_token tool to generate token for the customer.

        #Example: Argument for the generate_customer_token can only be (Args: service_type = general or service_type = account_service or service_type = transfer_service or service_type = loan_service)

    Always be helpful
    """,
    model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client),
    handoffs=[account_agent, transfer_agent, loan_agent],
    tools=[generate_customer_token, identify_banking_purpose],
    input_guardrails=[check_slangs],
)

#---------------------------------------------------------------------------------
while True:
    try:
        user_input = input("\n🤖Enter your banking query (or type 'exit' to quit): ")
        if user_input.lower() in  ['exit', 'quit']:
            print("Exiting the banking agent. Goodbye!")
            break

        result = Runner.run_sync(agent, input=user_input)
        rich.print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        rich.print(f"[bold red]❌Input Guardrail Triggered: {e}[/bold red]")
    except OutputGuardrailTripwireTriggered as e:
        rich.print(f"[bold red]❌Output Guardrail Triggered: {e}[/bold red]")
