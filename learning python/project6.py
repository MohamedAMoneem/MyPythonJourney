#this code is about head or tails

import random
rand_int = random.randint(0,1)
rand_rand = random.random()
input("press enter to start. . .")
start = int(input("""
welcome to head or tails game! choose method:
    random.randint() : (1)
    random.random()  : (2)
insert number from given only. . .
              """))
if start == 1:
    answer = input("Cool! Now choose, Head or tails? : ")
    if answer.lower() == "head" or answer.lower() == "tails":
        if rand_int == 1:
            print(f"you won! the computer chose {answer}")
        else:
            print(f"you lost! the computer did not choose {answer}")
    else:
        print("Please write only head or tails!")
elif start == 2:
    answer2 = input("Cool! Now choose, Head or tails? : ")
    if answer2.lower() == "head" or answer2.lower() == "tails":
        if rand_rand <0.5:
            print(f"you won! the computer chose {answer2}")
        else:
            print(f"you lost! the computer did not choose {answer2}")
    else:
        print("Please write only head or tails!")           
else:
    print("please choose bewteen (1) and (2)")