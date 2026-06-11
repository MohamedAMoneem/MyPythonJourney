#this project is about rock paper scissors game

import random
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
rock = """
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
choices = ["rock" ,"paper" , "scissors"]
computer = random.choice(choices)
computer_index = choices.index(computer)
start = input("welcome to rock paper scissors game\npress enter to start or type (help) for help : ").lower()
if start == "help":
    print("RULES:\nyou choose and the computer choose\nrock beat scissors\npaper beats rock\scissors beat paper")
    print("\nlets start\n")
else:
    print("\nlets start\n")
answer = input("choose. rock, paper or scissors? : ").lower()
index = (choices.index(answer))
tie = index
if answer in choices:
    if index == computer_index:
        print("TIE!")
        if tie == 0:
            print(f"""
the computer chose:
            {rock}
you chose:
            {rock}
""")
        elif tie == 1:
            print(f"""
the computer chose:
            {paper}
you chose:
            {paper}
""")
        else:
            print(f"""
the computer chose:
            {scissors}
you chose:
            {scissors}
""")
    elif (index == 0 and computer_index == 1) or (index == 1 and computer_index == 0):
        if index == 0:
            print(f"""
                  computer wins!
you chose:
        {rock} 
computer chose:
        {paper}
                  """)
        else:
            print(f"""
                  you win!
you chose:
        {paper} 
computer chose:
        {rock}
                  """)
    elif (index == 1 and computer_index == 2) or (index == 2 and computer_index == 1):
        if index == 1:
            print(f"""
                  computer wins!
you chose:
        {paper} 
computer chose:
        {scissors}
                  """)
        else:
            print(f"""
                  you win!
you chose:
        {scissors} 
computer chose:
        {paper}
                  """)
    else:
        if index == 2:
            print(f"""
                  computer wins!
you chose:
        {scissors} 
computer chose:
        {rock}
                  """)
        else:
            print(f"""
                  you win!
you chose:
        {rock} 
computer chose:
        {scissors}
                  """)
else:

    print("invalid choice")