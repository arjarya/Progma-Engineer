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
    "what is your name": "i am your friendly AI chatbot.",
}
memory = {
   "name": None # None is python keyword for null value
}
while True:
    user = input("You:").lower()
    if user in ["bye", "bi", "goodbye", "exit", "quit"]:
     print("AI: Goodbye! have a great day")
     break 
    found = False
    # Store name if user says "my name is ..."
    if "my name is" in user:
        memory["name"] = user.split("my name is")[-1].strip().capitalize()
        print(f"AI: Nice to meet you, {memory['name']}")
        found = True

    # Recall name if user asks
    elif "what is my name" in user or "do you know my name" in user:
        if memory["name"]:
           print(f"AI: your name is {memory['name']}")
        else:
           print("AI: I don't know your name yet")
        found = True
    else:
         user_words = user.split()
         for key in response:
             key_words = key.split()
             if all(word in user_words for word in key_words): #use all()
              print("AI:", response[key])
              found = True
              break 
    # Default reply
    if not found:
       print("AI: I am sorry, i do not understand, Try again")