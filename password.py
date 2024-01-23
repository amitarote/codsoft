import random
import string

print("MENU")
print("1. Easy Password")
print("2. Medium Password")
print("3. Hard Password")

choice = int(input("Enter your Password choice: "))
length = int(input("Enter the length of your password: "))


if choice == 1:
    char = string.digits
elif choice == 2:
    char = string.digits + string.ascii_letters
elif choice == 3:
    char = string.digits + string.ascii_letters + string.punctuation
else:
    print("Invalid choice. Please choose 1, 2, or 3.")
    exit()

password = ""
for i in range(length):
    next_char = random.choice(char)
    password += next_char

print("Your random password is:", password)

