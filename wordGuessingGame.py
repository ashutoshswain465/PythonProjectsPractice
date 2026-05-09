import random
import nltk

nltk.download('words')

name = input('What is your name: ')
print(f'Welcome to word guessing game {name}')

english_words = nltk.corpus.words.words()

w_len = random.randint(4, 10)

print(f'Creating a list of 12 random words each of length {w_len}')

filtered_list = [x for x in english_words if len(x) == w_len]
words = random.sample(filtered_list, 12)

print('The word list is: ')
print(words)

print('\nSelecting the random word')
word = random.choice(words)
print('The random word is now selected. your job is to guess the word now. you have 12 guesses only.')

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print('You Win')
        print(f'The word is {word}')
        break

    guess = input("\nGuess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print(f'You have {turns} more guesses')

    if turns == 0:
        print('You Lose')
        print(f'The word was {word}')
