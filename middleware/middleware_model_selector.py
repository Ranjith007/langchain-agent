# middleware/model_selector.py
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# instantiate models to choose between
_basic = ChatOpenAI(model="gpt-4o-mini", temperature=0)
_advanced = ChatOpenAI(model="gpt-4o", temperature=0.2)

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """
    Simple heuristic: if conversation (state) longer than threshold, pick advanced model.
    """
    try:
        messages = request.state.get("messages") or []
        msg_count = len(messages)
    except Exception:
        msg_count = 0

    if msg_count >= 6:
        request.model = _advanced
    else:
        request.model = _basic

    return handler(request)
