import os
os.system('cls')
print("AI: Welcome to ChatBot AI, say bye to exit. \n")
response = {
    "hello": "hi there! 👋",
    "hi": "hello! 👋",
    "how you": "I'm good, how can help you?",
    "how are you": "I'm good, how can help you?",
    "what can you do": "i can help you with various tasks.",
    "thanks": "you are welcome!",
    "thank you": "welcome!",
    "name": "i am a simple AI chatbot.",
    "what is your name": "i am your friendly AI chatbot.",
}
while True:
    user = input("You:").lower()
    if user in ["bye", "bi", "goodbye", "exit", "quit"]:
     print("AI: Goodbye! have a great day")
     break 
    found = False
    user_words = user.split() # split user input into words
    for key in response:
       if key in user:  # check if any key is in user input:
          print("AI:", response[key])
          found = True
          break 
    if not found:
       print("AI: I am sorry, i do not understand, Try again")
