import random

Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '?', ',', '.']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letter_amount = int(input('Enter the amount of letter you want : '))
chars_amount = int(input('Enter the amount of special chars you want : '))
number_amount = int(input('Enter the amount of number you want : '))
letter_list = []
chars_list = []
number_list = []

for i in range(0, letter_amount):
    letter_list.append(random.choice(Letters))
for i in range(0, chars_amount):
    chars_list.append(random.choice(Special_chars))
for i in range(0, number_amount):
    number_list.append(random.choice(Numbers))

raw_password = letter_list + chars_list + number_list
random.shuffle(raw_password)
password = "".join(raw_password)
print(password)
