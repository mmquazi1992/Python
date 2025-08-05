import random

print("Welcome to the password generator!")


letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$','%','&','(',')','*','+']

password_list = []

number_of_letters = int(input("How many letters would you like in your password?"))
symbols = int(input("How many symbols would you like?"))
numbers = int(input("How many numbers would you like?"))

password_list = random.choices(letters_list, k = number_of_letters)
password_list.extend(random.choices(symbols_list, k = symbols))
password_list.extend(random.choices(numbers_list, k = numbers))

random.shuffle(password_list)

password_string = ""

for passkey in password_list:
    password_string += passkey

print(f"Your password is: {password_string}")    
