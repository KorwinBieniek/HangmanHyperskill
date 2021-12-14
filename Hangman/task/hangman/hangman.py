import random

ALPHABET = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'}
LIST_OF_WORDS = ['python', 'java', 'kotlin', 'javascript']
CORRECT_WORD = LIST_OF_WORDS[random.randint(0, len(LIST_OF_WORDS) - 1)]


def start_hangman():
    lives = 8
    word_letters = set(CORRECT_WORD)
    used_letters = set()

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

        # the current word
        word_list = [letter if (letter in used_letters) else '-' for letter in
                     CORRECT_WORD]
        print('____________WORD_______________\n')
        print(''.join(word_list))
        print('\n___________________________')

        user_letter = input('Input a letter: ')

        if len(user_letter) != 1:
            print('You should input a single letter')
        elif user_letter not in ALPHABET:
            print('Please enter a lowercase English letter')

        elif user_letter in ALPHABET - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('That letter doesn\'t appear in the word')
                if lives == 1:
                    print('That letter doesn\'t appear in the word')
        elif user_letter in used_letters:
            print('You\'ve already guessed this letter')

    if lives == 0:
        print('You lost!')
    else:
        print(f'{CORRECT_WORD}\nYou guessed the word!\nYou survived!')


def menu(correct):
    while not correct:
        print("H A N G M A N")
        choice = input('Type "play" to play the game, "exit" to quit: ').upper()
        if choice == 'EXIT':
            exit(0)
        elif choice == 'PLAY':
            correct = True
            start_hangman()


if __name__ == '__main__':
    menu(False)
