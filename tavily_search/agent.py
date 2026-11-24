from google.adk.agents.llm_agent import Agent
from google.adk.tools.langchain_tool import LangchainTool
from langchain_tavily import TavilySearch


tavily_search = TavilySearch(
    max_results = 5,  # will try to return up to 5 relevant search results related to your query.
    topic = "general"   # specifies the category or type of information you want Tavily to search for.
)

# wrap is so ADK can use it
tavily_tool = LangchainTool(tool=tavily_search)

# give it to the agent like any other tool
root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can search the web.',
    instruction=(
        "Answer user questions accurately. "
        "Use the Tavily search tool when you need current information"
        "or need to verify facts. "),
    tools= [tavily_search]
)
