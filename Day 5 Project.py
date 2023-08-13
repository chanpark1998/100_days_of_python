#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
import random

pass_letters = ""
for i in range(0, nr_letters):
  pass_letters += letters[random.randint(0, len(letters) - 1)]

pass_symbols = ""
for i in range(0, nr_symbols):
  pass_symbols += symbols[random.randint(0, len(symbols) - 1)]

pass_numbers = ""
for i in range(0, nr_numbers):
  pass_numbers += numbers[random.randint(0, len(numbers) - 1)]

print(f"Your password is: {pass_letters}{pass_symbols}{pass_numbers}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
l = nr_letters
s = nr_symbols
n = nr_numbers
password = ""

i = 0
while i != (nr_letters + nr_symbols + nr_numbers):
  rng = random.randint(0,2)
  if(rng == 0 and l != 0):
    password += letters[random.randint(0, len(letters) - 1)]
    l -= 1
    i += 1
  elif(rng == 1 and s != 0):
    password += symbols[random.randint(0, len(symbols) - 1)]
    s -= 1
    i += 1
  elif(rng == 2 and n != 0):
    password += numbers[random.randint(0, len(numbers) - 1)]
    n -= 1
    i += 1
  else:
    i += 0

print(f"Your randomized password is: {password}")