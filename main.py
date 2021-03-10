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
print("Here is your easy password: ")
for nl in range(1,nr_letters+1):
  print(random.choice(letters), end="")
for ns in range(1,nr_symbols+1):
  print(random.choice(symbols), end="")
for nn in range(1,nr_numbers+1):
  print(random.choice(numbers), end="")
print()
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

length = nr_letters+nr_numbers+nr_symbols
l = []

for nl in range(1,nr_letters+1):
  l.append(random.choice(letters))
for ns in range(1,nr_symbols+1):
  l.append(random.choice(symbols))
for nn in range(1,nr_numbers+1):
  l.append(random.choice(numbers))

random.shuffle(l)
print("Here is your hard password: ")
for no in range(1,length+1):
  print(l[no-1] , end="")