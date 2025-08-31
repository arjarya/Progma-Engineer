import os

# Clear screen (works for Windows, for Linux/macOS replace 'cls' with 'clear')
os.system('cls')

print("Welcome to the AI Chatbot! Type 'bye' to exit.\n")

# Dictionary of simple responses
responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! 😊",
    "how are you": "I’m just code, but I’m great! 😃",
    "what can you do": "I can chat with you and answer simple questions! 🤖",
    "thanks": "You are welcome! 🙌",
    "thank you": "No problem! 👍",
    "name": "I’m a simple AI chatbot 🤖",
    "what is your name": "I’m your friendly chatbot 🤖"
}

while True:
    user = input("You: ").lower()
    
    if user in ["bye", "goodbye", "exit", "quit"]:
        print("AI: Goodbye! Have a nice day 👋")
        break  # Exit the loop
    
    elif user in responses:
        print("AI:", responses[user])
    
    else:
        print("AI: Sorry, I don’t understand that yet.")
