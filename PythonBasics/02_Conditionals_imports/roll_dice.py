import random
roll= random.randint(1,6)
guess= int(input('Guess the dice roll:\n'))

if guess== roll:
    print("CORRECT! They rolled a "+ str(roll))
else:
    print("WRONG! They rolled a "+ str(roll))