import random, string, os
os.system('cls')

print("Password Generator")
characters = string.ascii_letters + string.digits + string.punctuation

while True:
 length = int(input("Please enter numbers only: "))
 if 8<= length <=20:
  password = ''.join(random.choice(characters) for i in range(length))
  print("Your Password is: ", password)
  break
 else:
  print("Password length should be 8-20.")