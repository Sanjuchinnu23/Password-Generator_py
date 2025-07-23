import random
import string

def generate_password():
    print("Password Generator")

length = int(input("Enter the desired password length: "))

all_characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(all_characters) for i in range(length))

print("Your generated password is:", password)

#Run the function
generate_password()
