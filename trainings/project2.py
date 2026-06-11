import string
sentance = input("type in sentance: ")
new_sent = ""
for i in sentance:
    if i not in string.punctuation:
        new_sent += i
print(new_sent)