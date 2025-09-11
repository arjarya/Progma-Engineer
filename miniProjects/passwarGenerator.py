import random, string, os
os.system('cls')

print("Password Generator")
user = int(input("You: Enter the length of passward: "))
characters = string.ascii_letters + string.digits + string.punctuation
passward = ''.join(random.choice(characters) for i in range(user))
print("Your Password is:", passward)