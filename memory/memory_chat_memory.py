# memory/chat_memory.py
from langchain.memory import ConversationBufferMemory

def get_memory():
    # memory_key 'chat_history' will be used inside agent state
    return ConversationBufferMemory(memory_key="chat_history", return_messages=True)
