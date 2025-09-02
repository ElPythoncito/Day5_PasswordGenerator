# Day 5
# 100 Days of Code with Python
# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

user_password = ""

for letter in range(nr_letters):
    user_password += random.choice(letters)
for symbol in range(nr_symbols):
    user_password += random.choice(symbols)
for number in range(nr_numbers):
    user_password += random.choice(numbers)
# Password Str
print(user_password)
# Password List (random.shuffle)
my_password_list = list(user_password)
random.shuffle(my_password_list)
# -------------------------------------------------------------------------------
end_password = ""
for item_password in my_password_list:
    end_password += item_password

print(f"Your password is 🔐: {end_password}")

input("Type ENTER to finish!!!")
