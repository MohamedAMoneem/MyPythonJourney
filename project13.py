# import random
# word = ["silly", "ugly", "cat"]
# rand = random.choice(word)
# show = []
# for chars in rand:
#     show.append("_")
# print(show)
# while "_" in show:
#     guess = input("insert a guess letter: ").lower()
#     for loc in range(len(rand)):
#         if rand[loc] == guess:
#             show[loc] = guess
#     print(show)
import random
word = ["silly", "ugly", "cat"]
rand = random.choice(word)
show = []
for chars in rand:
    show.append("_")
print(show)
for i in range(-6,0):
    print("you have ")
    while "_" in show:
        guess = input("insert a guess letter: ").lower()
        for loc in range(len(rand)):
            if rand[loc] == guess:
                show[loc] = guess
        print(show)
        testing if change happens:
        
2eiunnnnnnnnnnnnnnnnnn23ni3r