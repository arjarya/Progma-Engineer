import os
os.system('cls')
print("Welcome to the AI Chatbot, Type 'bye' to exit the chat.")
while True:
  user = input("you: ").lower()
  if "hello" in user or "hi" in user:
        print("AI: Hi there! 👋")
  elif "how are you" in user:
        print("AI: I’m just code, but I’m great! 😃")
  elif "what can you do" in user:
        print("AI: I can chat with you and answer simple questions! 🤖")
  elif "bye" in user or "goodbye" in user:
        print("AI: Goodbye! Have a nice day👋")
        break # Exit the loop and end the chat
  elif "thanks" in user or "thank you" in user:
        print("AI: you are welcome! 🙌")
  elif "name" in user or "what is your name" in user:
        print("AI: I’m a simple AI chatbot 🤖")
  else:
        print("AI: Sorry, I don’t understand that yet.")
