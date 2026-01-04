import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, output_guardrail, RunContextWrapper, GuardrailFunctionOutput, OutputGuardrailTripwireTriggered
from pydantic import BaseModel, Field
from typing import Any

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#---------------------------------------------------------------------------------
class Check_Res_Class(BaseModel):
    is_not_banking_related: bool = Field(description="If the LLM response is not related to banking related topics set the value True in this field.")
    reasoning: str = Field(description="What is the reason behind it being not related to banking topics")
#---------------------------------------------------------------------------------
o_guardrail_agent = Agent(
    name="Output Guardrail Agent",
    instructions="""
    You are an Output Guardrail Agent.

    Your job is to strictly evaluate whether the LLM response is related to banking or not.

    Banking-related topics include ONLY:
    - Accounts, balance, statements
    - Money transfer, payments, transactions
    - Loans, mortgages, credit
    - Banking services, customer support, tokens, queues
    - Greetings and simple conversation directly related to banking (e.g. "Welcome to the bank", "How can I help you today?")

    If the response is about ANYTHING other than banking or simple banking-related conversation
    (for example: politics, sports, programming, movies, religion, jokes, personal opinions, general knowledge, or random chat),
    then you MUST set:
        is_not_banking_related = true

    If the response is clearly related to banking or a simple banking-related conversation,
    then set:
        is_not_banking_related = false

    Always provide a short and clear reasoning explaining your decision.

    Be strict. When in doubt, mark it as NOT banking-related.
    """,
    model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client),
    output_type=Check_Res_Class
)
#---------------------------------------------------------------------------------
@output_guardrail
async def res_check(ctx: RunContextWrapper, agent: Agent, output: Any)-> GuardrailFunctionOutput:

    result = await Runner.run(o_guardrail_agent, output, context=ctx)

    return GuardrailFunctionOutput(
        output_info = result.final_output,
        tripwire_triggered = result.final_output.is_not_banking_related
    )
