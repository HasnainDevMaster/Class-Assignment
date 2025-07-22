import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# Load .env
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in your .env file.")

# Configure client
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
set_tracing_disabled(True)

# --- Define the three tool-agents and convert them to tools ---

capital_agent = Agent(
    name="Capital Finder",
    instructions="Given a country name, reply ONLY with its capital city (no extra text).",
    model=OpenAIChatCompletionsModel("gemini-2.0-flash", openai_client=client)
)
capital_tool = capital_agent.as_tool(
    tool_name="get_capital",
    tool_description="Returns the capital city of the specified country."
)

language_agent = Agent(
    name="Language Finder",
    instructions="Given a country name, reply ONLY with its official or most commonly spoken language(s).",
    model=OpenAIChatCompletionsModel("gemini-2.0-flash", openai_client=client)
)
language_tool = language_agent.as_tool(
    tool_name="get_language",
    tool_description="Returns the official or most common language(s) of the specified country."
)

population_agent = Agent(
    name="Population Finder",
    instructions="Given a country name, reply ONLY with its approximate population (e.g. 'around 67 million').",
    model=OpenAIChatCompletionsModel("gemini-2.0-flash", openai_client=client)
)
population_tool = population_agent.as_tool(
    tool_name="get_population",
    tool_description="Returns the approximate population of the specified country."
)

# --- Orchestrator/Triage Agent ---

orchestrator = Agent(
    name="Country Info Orchestrator",
    instructions=(
        "You are the orchestrator. When given a country name, call these tools (in order):\n"
        "1. get_capital\n"
        "2. get_language\n"
        "3. get_population\n\n"
        "Then summarize the results in one friendly paragraph, prefixing each piece with "
        "'Capital Finder says...', 'Language Finder says...', etc."
    ),
    tools=[capital_tool, language_tool, population_tool],
    model=OpenAIChatCompletionsModel("gemini-2.0-flash", openai_client=client)
)

# --- Main ---

async def main():
    country = input("🌍 Enter a country name: ").strip()
    if not country:
        print("❌ Country name cannot be empty.")
        return

    print("\n🔎 Gathering data...\n")
    try:
        result = await Runner.run(orchestrator, f"Country: {country}")
        print("\n📘 Country Summary:\n")
        print(result.final_output)
    except Exception as e:
        print(f"\n❌ Error during lookup: {e}")

if __name__ == "__main__":
    asyncio.run(main())
