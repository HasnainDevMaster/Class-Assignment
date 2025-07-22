import asyncio
import os
from dotenv import load_dotenv 
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# Load environment variables from .env file
load_dotenv()

# 1. Configure your custom LLM client (e.g. Gemini)
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# (Optional) disable low‑level tracing for cleaner logs/output
set_tracing_disabled(True)

# 2. Define your Smart Store agent with detailed instructions for product recommendations
agent = Agent(
    name="Smart Store",
    instructions=(
        "You are a virtual store assistant specializing in a wide range of products—from "
        "home office furniture and kitchen gadgets to fitness equipment and travel accessories. "
        "When the user describes their needs or asks for multiple items in one request, you should:\n"
        "  1. Identify each product category or need the user mentions.\n"
        "  2. For each item, recommend a specific product (include brand/model if applicable).\n"
        "  3. Explain in a few sentences why each product fits their requirement.\n"
        "  4. If the user asks for multiple items at once, present your recommendations as a "
        "numbered list with clear headings per item.\n"
        "  5. Keep your tone friendly and concise."
    ),
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",  # Specify the Gemini model to use
        openai_client=client       # Pass the configured OpenAI-compatible client
    ),
)

# 3. Run your agent in an async main function
async def main():
    # Prompt the user for their product needs
    user_input = input("How can I help you today? ")
    # Get product suggestions from the agent
    result = await Runner.run(agent, user_input)
    # Display the agent's suggestions
    print("\n🤖 Product Suggestions:\n", result.final_output)

# Entry point: run the async main function
if __name__ == "__main__":
    asyncio.run(main())
