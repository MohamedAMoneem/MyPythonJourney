import random
numbers = [1,2,3,4,5,6,7,8,9,10]
number = random.choice(numbers)
guess = int(input("guess number between 1 and 10 : "))
while guess!= number:
    if guess < number:
        print("too low!")
    else:print("too high")
    guess = int(input("try again: "))
print("you guessed the right number!")