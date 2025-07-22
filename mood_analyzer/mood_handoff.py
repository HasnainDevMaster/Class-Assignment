import asyncio
import os
from dotenv import load_dotenv 
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# Load environment variables from .env file
load_dotenv()

# Configure custom LLM provider
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(True)

# Agent 1: Detect user's mood
mood_analyzer = Agent(
    name="Mood Analyzer",
    instructions=(
        "You are an advanced emotion detection expert. Given a short user message, analyze the text and respond with the single word that best describes the user's mood. "
        "Possible moods include: happy, sad, stressed, excited, calm, angry, anxious, bored, tired, hopeful, frustrated, grateful, lonely, or any other relevant emotion. "
        "If the mood is positive (happy, excited, calm, hopeful, grateful), respond with the exact word. "
        "If the mood is negative (sad, stressed, angry, anxious, bored, tired, frustrated, lonely), respond with the most accurate word. "
        "Do not provide any explanation, context, or additional words—just the mood word. "
        "Be precise and avoid synonyms unless the user's message is ambiguous."
    ),
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client,
    )
)

# Agent 2: Suggest activity if mood is negative
activity_suggester = Agent(
    name="Activity Suggester",
    instructions=(
        "You are a compassionate assistant who suggests one positive, practical activity to help someone improve their mood when they are feeling negative emotions. "
        "If the mood is sad, suggest an activity that brings comfort or joy, such as listening to uplifting music, talking to a friend, or spending time in nature. "
        "If the mood is stressed or anxious, recommend a calming activity like deep breathing exercises, meditation, a short walk, or journaling. "
        "If the mood is angry or frustrated, suggest a healthy outlet such as physical exercise, creative expression, or taking a break to cool down. "
        "If the mood is lonely, recommend connecting with others, joining a group activity, or reaching out to loved ones. "
        "If the mood is tired or bored, suggest something energizing or engaging, like a quick stretch, a fun hobby, or a change of scenery. "
        "Always explain briefly why the activity is helpful for that specific mood. "
        "Keep your response short, supportive, and tailored to the detected mood."
    ),
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client,
    )
)

# Run both agents with handoff logic
async def main():
    user_input = input("🗣️  How are you feeling today?\n> ")

    # Step 1: Detect mood
    print("\n🔎 Running agent: Mood Analyzer")
    try:
        mood_result = await Runner.run(mood_analyzer, user_input)
        mood = mood_result.final_output.strip().lower()
        print(f"\n🧠 Detected Mood: {mood.capitalize()}")
    except Exception as e:
        print(f"Error running Mood Analyzer agent: {e}")
        return

    # Step 2: If mood is negative, suggest activity
    if mood in ["sad", "stressed", "angry", "anxious", "bored", "tired", "frustrated", "lonely"]:
        print(f"\n🔎 Running agent: Activity Suggester for mood '{mood}'")
        try:
            activity_result = await Runner.run(activity_suggester, f"The user is feeling {mood}.")
            print("\n🎯 Suggested Activity:")
            print(activity_result.final_output)
        except Exception as e:
            print(f"Error running Activity Suggester agent: {e}")
    else:
        print("\n😊 You seem to be doing fine. Keep it up!")

if __name__ == "__main__":
    asyncio.run(main())
