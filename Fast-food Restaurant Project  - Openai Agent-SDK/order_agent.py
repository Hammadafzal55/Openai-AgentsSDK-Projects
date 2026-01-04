import os
from dotenv import load_dotenv
from agents import Agent, ModelSettings, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool, RunContextWrapper
from datetime import datetime, time

#----------------------------------------------------------------------------

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#----------------------------------------------------------------------------
def is_bussiness_hours():
    now = datetime.now().time()
    bussiness_start = time(9, 0)  # 9:00 AM
    bussiness_off = time(21, 0)  # 9:00 PM
    return (bussiness_start <= now) and (now <= bussiness_off)
#----------------------------------------------------------------------------

def closed_tool_swicther(ctx: RunContextWrapper, agent: Agent)-> bool :
    """Enable shop_closed tool only when the shop is closed"""
    return not is_bussiness_hours()

def burger_tool_swicther(ctx: RunContextWrapper, agent: Agent)-> bool :
    if ctx.context.order_type == "burger":
        return True
    return False

def pizza_tool_swicther(ctx: RunContextWrapper, agent: Agent)-> bool :
    if ctx.context.order_type == "pizza":
        return True
    return False
#----------------------------------------------------------------------------
@function_tool(is_enabled=closed_tool_swicther)
def shop_closed()-> str:
    """Return a standard shop closed notice """
    return "Shop is closed. Please come back during business hours. (9am - 9pm)"

@function_tool(is_enabled=burger_tool_swicther)
def burger_order():
    """Provide an update for the status of the user's burger order"""
    return "Your Burger is cooking... place wait for just 10 minutes."


@function_tool(is_enabled=pizza_tool_swicther)
def pizza_order():
    """Provide an update for the status of the user's pizza order"""
    return "Your Pizza is cooking... place wait for just 10 minutes."
#----------------------------------------------------------------------------

my_order_agent = Agent(
    name="my_order_agent",
    instructions=
    """you are a order taker manager for a fast food restaurant.
    After calling a tool:
    - Use the tool data to write a friendly, creative response
    - Mention quantity clearly
    - Always ask if the user wants to add something else.
    Always use tool provided to you.
    if the shop_closed tool is available use it immediately.
    Never respond with your own text - always use a tool.""",
    model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client),
    tools=[burger_order, pizza_order, shop_closed],
    model_settings=ModelSettings(temperature=0.3, tool_choice="required")
)

#----------------------------------------------------------------------------

