import os; os.system('cls')
response = {
"hi": "hi there", 
"name": "chatbot AI", 
"what can you do": "assiting"
}
while True:
    user = input("You: ").lower()
    found = False
    if user in ["bye"]:
        print("Goodbye")
        break
    for key in response:
        if key in user:
            print(response[key])
            found = True
            break
    if not found:
        print("I don't understand")