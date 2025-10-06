import string, random, os; os.system('cls')
print("Password Generator")


while True:
    length = int(input("Enter Password Length: "))
    if 8<= length <= 16:
        break
    else:
        print("Password length must be 8-16")


include_upper = input("do you want uppercase letters? (y/n) ").lower() == "y"
include_lower = input("do you want lowercase letter? (y/n) ").lower() == "y"
include_digit = input("do you want digit? (y/n) ").lower() == "y"
include_symbol = input("do you want symbol? (y/n)").lower() == "y"

#Build character set
characters = ""
if include_upper:
    characters += string.ascii_uppercase
if include_lower:
    characters += string.ascii_lowercase
if include_digit:
    characters += string.digits
if include_symbol:
    characters += string.punctuation

if not characters:
    print("default password: ")
    characters = string.ascii_letters + string.digits + string.punctuation
    
password = ''.join(random.choice(characters) for i in range(length))
print("Your Password is: ", password)