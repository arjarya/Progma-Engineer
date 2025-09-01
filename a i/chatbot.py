import os
print("Welcome to AI, say bye to exit. \n")
response = {
    "hello": "hi there! 👋",
    "hi": "hello! 👋",
    "how are you": "I'm good, how can help you?",
    "what can you do": "i can help you with various tasks.",
    "thanks": "you are welcome!",
    "thank you": "welcome!",
    "name": "i am a simple AI chatbot.",
    "what is your name": "i am your friendly AI chatbot.",
}
while True:
    user = input("You: ").lower()
    if user in ["bye", "bi", "goodbye", "exit", "quit"]:
     print("AI: Goodbye! have a great day")
     break
    elif user in response:
     print("AI:", response[user])
    else:
     print("AI: I'm sorry, I don't understand that.")
