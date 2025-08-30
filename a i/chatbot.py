import os
os.system('cls')
user = input("You:").lower()
if "hello" in user:
    print("AI: Hello There!")
elif "how are you" in user:
    print("AI: I'm a chatbot, but I am good")
else:
    print("AI: Sorry! I don't understand")  