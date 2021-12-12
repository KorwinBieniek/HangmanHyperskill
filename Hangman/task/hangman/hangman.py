import random
import string

lives = 8
print("H A N G M A N\n")
used_letters = set()
alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'}
list_of_words = ['python', 'java', 'kotlin', 'javascript']
correct_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
word_letters = set(correct_word)
random_letter = set()
# for i in range(3):
# random_letter.add(random.choice(correct_word))

# word_letters = word_letters.union(word_letters, random_letter)

while len(word_letters) > 0 and lives > 0:
    # print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

    # the current word
    word_list = [letter if (letter in random_letter or letter in used_letters) else '-' for letter in correct_word]
    print('\n')
    print(''.join(word_list))

    user_letter = input('Input a letter: ')

   # if user_letter in {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       #'T', 'u',
                       #'V', 'W', 'X', 'Y', 'Z'}:
    if len(user_letter) != 1:
        print('You should input a single letter')
    elif user_letter not in alphabet:
        print('Please enter a lowercase English letter')

    elif user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            # used_letters.add(user_letter)
            print('\n')
        else:
            lives -= 1
            print('That letter doesn\'t appear in the word')
            if lives == 1:
                print('That letter doesn\'t appear in the word')
    elif user_letter in used_letters:
        print('You\'ve already guessed this letter')
        # print('\n')
        # lives -= 1

if lives == 0:
    print('You lost!')
else:
    print(f'{correct_word}\nYou guessed the word!\nYou survived!')
