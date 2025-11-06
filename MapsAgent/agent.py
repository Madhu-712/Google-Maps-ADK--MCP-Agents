from google.adk.agents.llm_agent import Agent
from .customfunctions import mapsinfo
from google.adk.tools import FunctionTool

root_agent = Agent(
    model='gemini-2.5-flash',
    name='Maps_agent',
    tools=[
         FunctionTool(mapsinfo), 
    ],
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge regarding places information by using maps tool',
)

