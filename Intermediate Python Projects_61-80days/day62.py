# 62: Random Password Generator (with strength meter)

import random
import string

def generate_password_with_number(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        length = int(input("Enter the length of the password: "))
        if length < 8:
            print("Password length must be at least 8 characters.")
            continue
        password = generate_password_with_number(length)
        print("Generated password:", password)
        break

if __name__ == "__main__":  
    main()