#this project encrypts whatever you write
import string
chars = string.ascii_lowercase
chars_upper = string.ascii_uppercase
other = string.punctuation
numbers = string.digits
word = input("insert something you want to encrypt: ")
number = int(input("insert encryption number: "))
def encrypt(sent,turns):
    final = ""
    for i in sent:
        if i in other or i == " " or i in numbers:
            final += i
            continue
        if i in chars:
            pos = chars.index(i)
            new_pos = pos + turns
        else:
            pos = chars_upper.index(i)
            new_pos = pos + turns
        if new_pos > 26:
            new_pos -= 26
        if i in chars:
            final += chars[new_pos]
        else:
            final += chars_upper[new_pos]

    print(final)
encrypt(word,number)