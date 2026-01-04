import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, input_guardrail, RunContextWrapper, TResponseInputItem, GuardrailFunctionOutput, InputGuardrailTripwireTriggered
from pydantic import BaseModel, Field

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#---------------------------------------------------------------------------------
class Check_Slang_Class(BaseModel):
    is_abusive: bool = Field(description="Value will be true if user query has some slang or abusive language")
    reasoning: str = Field(description="What is the reason behind it being abusive or not")
#---------------------------------------------------------------------------------
i_guardrail_agent = Agent(
    name="Input Guardrail Agent",
    instructions="Always check if the user query has any abusive and slang words.",
    model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client),
    output_type=Check_Slang_Class
)
#---------------------------------------------------------------------------------
@input_guardrail
async def check_slangs(ctx: RunContextWrapper, agent: Agent, input: str | list[TResponseInputItem])-> GuardrailFunctionOutput:

    result = await Runner.run(i_guardrail_agent, input, context=ctx)

    return GuardrailFunctionOutput(
        output_info= result.final_output,
        tripwire_triggered= result.final_output.is_abusive,
    )
