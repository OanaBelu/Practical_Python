import random

roll = random.randint(1, 6)
print("The computer rolled a " + str(roll))
guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print("Corrct! They rolled a " + str(roll))
