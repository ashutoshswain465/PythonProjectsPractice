import random
import threading
import pyautogui
from collections import Counter


def get_Input(container):
    try:
        c = input('Enter a letter to guess(5s limit): ').lower()
        return container.append(c)
    except EOFError:
        pass


someWords = '''apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')

word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a fruit.')

    for _ in word:
        print('_', end=' ')
    print()

    letterGuessed = ''
    chances = len(word) + 2
    flag = 0

    try:
        while chances > 0 and flag == 0:
            print()
            chances -= 1

            guess_list = []
            input_thread = threading.Thread(target=get_Input, args=(guess_list,), daemon=True)
            input_thread.start()
            input_thread.join(timeout=5)

            guess = "".join(guess_list)

            if not guess:
                print('\nTime up. No input received.')
                pyautogui.press('enter')
            else:
                if not guess.isalpha():
                    print('Enter only a letter!')
                    continue
                elif len(guess) > 1:
                    print('Enter only a single letter!')
                    continue
                elif guess in letterGuessed:
                    print('You already guessed that letter!')
                    continue

            if guess in word:
                letterGuessed += guess * word.count(guess)

            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')

            if Counter(letterGuessed) == Counter(word):
                print(f'\nCongratulations! You guessed the word: {word}')
                flag = 1
                break

        if chances <= 0 and Counter(letterGuessed) != Counter(word):
            print(f'\nYou Lost! the word was {word}')

    except KeyboardInterrupt:
        print('\nGame interrupted. Bye!')
        exit()
