import random

print("Hi! Let's start the number guessing game")
print("You have only 7 chances to guess the number. Best of Luck.")

l_limit = int(input('Enter lower limit: '))
u_limit = int(input('Enter upper limit: '))

rNum = random.randint(l_limit, u_limit)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    gNum = int(input(f'Enter your Guess{gc}: '))

    if gNum == rNum and gc < ch:
        print('Correct')
        print(f'You guessed it in {gc} tries')
        break
    elif gc >= ch and gNum != rNum:
        print('Incorrect. Chance Over')
    elif gNum > rNum:
        print('Too high')
    elif gNum < rNum:
        print('Too low')
