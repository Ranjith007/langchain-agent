# main.py
import os
from dotenv import load_dotenv
from agent_core import build_agent

load_dotenv()

def main():
    print("LangChain Agent (type 'exit' to quit)\n")
    agent = build_agent()

    while True:
        user = input("You: ").strip()
        if not user:
            continue
        if user.lower() in ("exit", "quit"):
            print("Bye!")
            break

        try:
            # agent.run returns a string response in this setup
            resp = agent.run(user)
            print("\nAgent:", resp, "\n")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
