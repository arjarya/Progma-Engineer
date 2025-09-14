import string, random, os
os.system('cls')
print("password Generator")
characters = string.ascii_letters + string.digits + string.punctuation

while True:
    length = int(input("Enter numbers only: "))
    if 8 <= length <= 16:
        password = ''.join(random.choice(characters) for i in range(length))
        print("Your Password is: ", password)
    else:
        print("Password must be 8-16")
    choice = input("Do you want another(y/n)? ").lower()
    if choice != 'y':
        print("Goodbye")
        break
