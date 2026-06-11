#this is a password generator code

import random
import string
print("welcome to password generator")
password = []
chars_num = int(input("insert amount of characters you want in the password: "))
symb_num = int(input("insert number of symbols: "))
char_assci = int(input("insert number of assci: "))
num_num = int(input("insert number of num: "))
if symb_num + char_assci + num_num != chars_num:
    print("the sum does not match the numbers you inserted!")
else:
    random1 = random.choices(string.ascii_letters, k=char_assci)
    random2 = random.choices(string.punctuation, k=symb_num)
    random3 = random.choices(string.digits, k=num_num)
    password.extend(random1)
    password.extend(random2)
    password.extend(random3)
    random.shuffle(password)
    final = "".join(password)
    print(final)

