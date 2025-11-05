# agent_core.py
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from memory.chat_memory import get_memory
from tools.web_search import web_search_tool_fn
from tools.calculator import calculate
from tools.python_exec import execute_python_code
from tools.file_reader import read_file

# Build the llm(s)
def _build_models():
    # Default basic model
    basic = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    # Advanced model (fallback / dynamic selection)
    advanced = ChatOpenAI(model="gpt-4o", temperature=0.2)
    return basic, advanced

def build_agent():
    basic, advanced = _build_models()
    # Wrap functions as Tools
    tools = [
        Tool.from_function(func=web_search_tool_fn, name="web_search", description="Search the web and return short summary."),
        Tool.from_function(func=calculate, name="calculator", description="Evaluate math expressions."),
        Tool.from_function(func=execute_python_code, name="python_exec", description="Executes a Python snippet and returns output."),
        Tool.from_function(func=read_file, name="file_reader", description="Read local file by relative path."),
    ]

    # memory
    memory = get_memory()

    # initialize agent; using a zero-shot tool-calling agent here
    agent = initialize_agent(
        tools=tools,
        llm=basic,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        memory=memory
    )

    # note: middleware is added automatically inside initialize_agent in some versions.
    # If you need to inject middleware, you can wrap the llm calls (see middleware/model_selector.py)
    return agent
