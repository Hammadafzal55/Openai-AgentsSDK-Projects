import os
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI
from output_guardrail import res_check

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#---------------------------------------------------------------------------------
account_agent = Agent(
    name="Account Services Agent",
    instructions="You help user in their query of account balance, statements, and account information. Always generate a token!",
    model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client),
)

transfer_agent = Agent(
    name="Transfer Services Agent",
    instructions="You help user with money transfer and payments. Always generate a token!",
    model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client),
)

loan_agent = Agent(
    name="Loan Services Agent",
    instructions="You help user with loans and mortgages. Always generate a token!",
    model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client),
    output_guardrails=[res_check]
)
