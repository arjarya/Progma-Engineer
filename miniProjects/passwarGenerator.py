import random, string, os
os.system('cls')
print("Password Generator")

while True:
 length = int(input("You: Enter the length of password: "))
 characters = string.ascii_letters + string.digits + string.punctuation
 if 8<= length <=20:
  password = ''.join(random.choice(characters) for i in range(length))
  print("Your Password is: ", password)
  break
 else:
  print("Password length should be 8-20 characters")