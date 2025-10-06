import re

txt = "That will be 59 dollars"

x = re.findall('dog', 'dog cat dog')
print(x)

if x:
    print("yes")
else:
    print("No")