import os
from agents.simple_agent import SimpleAgent

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Please set the GEMINI_API_KEY environment variable.")
        return
    agent = SimpleAgent(api_key)
    print("Agent initialized. Type your message (or 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = agent.chat(user_input)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()
