#this code is hangman game
import random
man = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word = ["silly", "ugly", "cat"]
rand = random.choice(word)
show = ["_"] * len(rand)
print(' '.join(show))
tries = 6
guessed = []
print(man[0])
while "_" in show and tries > 0:
    guess = input("guess the letter: ").lower()
    if guess in guessed:
       print(f"you already guessed this before\nyou have {tries} left")
       continue
    guessed.append(guess)
    if guess not in rand:
        tries -= 1
        print(man[6 - tries])
    else:
        for pos in range(len(rand)):
            if rand[pos] == guess:
                show[pos] = guess
                print
    print(' '.join(show))
    print(f"you have {tries} more left")

if tries == 0:
    print("you lose")
    print(man[-1])
else:
    print("you win")
