import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password


while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Error: Length should be a positive integer")
        else:
            break
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer")

print(generate_password(length))
