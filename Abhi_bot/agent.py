from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

root_agent = Agent(
    model='gemini-3.5-flash',  # This is the by default model for google
    #model = LiteLlm(model = "openai/gpt-4o"),  # This is a idea to use your own LLM model via LiteLLM.
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    generate_content_config=types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=800
    )
)
