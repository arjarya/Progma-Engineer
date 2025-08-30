user = input("You: ").lower()

if "hello" in user or "hi" in user:
    print("AI: Hi there! 👋")
elif "how are you" in user:
    print("AI: I’m just code, but I’m great! 😃")
elif "bye" in user:
    print("AI: Goodbye! Have a nice day 👋")
elif "thanks" in user or "thank you" in user:
    print("AI: You’re welcome! 🙌")
elif "name" in user:
    print("AI: I’m a simple AI chatbot 🤖")
else:
    print("AI: Sorry, I don’t understand that yet.")
