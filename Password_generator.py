import random
import string

def generate_password():
    print("Password Generator")

#Ask for password length
length = int(input("Enter the desired password length: "))

#Create pool of characters
all_characters = string.ascii_letters + string.digits + string.punctuation

#Generate password
password = ''.join(random.choice(all_characters) for i in range(length))

#Show password
print("Your generated password is:", password)

#Run the function
generate_password()
