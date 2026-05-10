import random
import nltk

nltk.download('words')

name = input('What is your name: ')
print(f'Welcome to word guessing game {name}')

english_words = nltk.corpus.words.words()

w_len = random.randint(4, 10)

print(f'Creating a list of 12 random words each of length {w_len}')

filtered_list = [x.lower() for x in english_words if len(x) == w_len]
words = random.sample(filtered_list, 12)

print('The word list is: ')
print(words)

print('\nSelecting the random word')
word = random.choice(words)
print('The random word is now selected. your job is to guess the word now. you have 12 guesses only.')

turns = 12
pos = 0

while turns > 0:
    failed = 0

    for index, char in enumerate(word):
        if index < pos:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1

    if failed == 0:
        print('\nYou Win')
        print(f'The word is {word}')
        break

    guess = input("\nGuess a character: ")

    if guess != word[pos]:
        turns -= 1
        print("Wrong")
        print(f'You have {turns} more guesses')
    else:
        if len(guess) == 1:
            if guess.isalpha():
                pos += 1

    if turns == 0:
        print('You Lose')
        print(f'The word was {word}')
