# PROGRAMER: Ethan mingerink
# Date:2.29.24
# Program: AI Playground

print("This will be a place for me to play with programing with AI technology")

import random

def greet():
    responses = ["Hello!", "Hi there!", "Greetings!"]
    return random.choice(responses)

def farewell():
    responses = ["Goodbye!", "See you later!", "Farewell!"]
    return random.choice(responses)

def respond(message):
    message = message.lower()
    if "hello" in message or "hi" in message or "hey" in message:
        return greet()
    elif "goodbye" in message or "bye" in message:
        return farewell()
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("AI: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI: Goodbye!")
            break
        else:
            response = respond(user_input)
            print("AI:", response)

if __name__ == "__main__":
    main()
