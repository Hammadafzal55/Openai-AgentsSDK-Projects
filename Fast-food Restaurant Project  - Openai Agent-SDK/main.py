import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, enable_verbose_stdout_logging
from pydantic import BaseModel, Field
from typing import Literal
import rich
from order_agent import my_order_agent

load_dotenv()
set_tracing_disabled(True)

class Order_Checker(BaseModel):
    is_order: bool = Field(
        description="True if the user is placing an order for pizza or burger.False if the message is not about ordering food (e.g., general questions, greetings, or non-food-related requests)."
    )

    quantity: int = Field(
        default=0, description="Exact number of food items ordered (only for pizza or burger). If not ordering, set to 0."
    )

    order_type: Literal["pizza", "burger", None] = Field(
        description="Set to 'pizza' if the user is ordering pizza, or 'burger' if ordering for a burger. Use null or leave empty if the user is not ordering these items."
    )

    reason: str = Field(
        description="Summarise the user's message in one sentence if it is not related to ordering pizza or burger.Give the core intent or purpose (e.g., greeting, complaint and non food questions)."
    )

    user_question: str = Field(
        description="Copy the user's original message or question exactly, without edits"
    )

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

main_agent = Agent(
    name="main_agent",
    instructions=(
        "You are a helpful assistant for a fast food restaurant." 
 "you only handle questions and order's related to pizza and burger's." 
 "If the user want to place an order or asks about pizza or burger's respond helpfuly."
 "For all the topics (e.g., drinks, salad, general questions, greeting), do not treat them as orders."
 "Only treat an input as an order if the user mentions pizza or burger with the quantity."
    ),
    model=OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=client),
    output_type=Order_Checker
)

user_input = input("Enter your Order: ")
result = Runner.run_sync(main_agent, input=user_input)
rich.print('[bold green]Main Agent Response:[/bold green]: ', result.final_output)

if result.final_output.is_order == True:
    my_order_agent_result = Runner.run_sync(my_order_agent, input=result.to_input_list(), context=result.final_output)
    rich.print("[bold green]Order Agent Response:[/bold green]")
    rich.print("my_order_agent_result: ", my_order_agent_result.final_output)