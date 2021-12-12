import random
import string

lives = 8
print("H A N G M A N\n")
used_letters = set()
alphabet = set(string.ascii_lowercase)
list_of_words = ['python', 'java', 'kotlin']
correct_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
word_letters = set(correct_word)
random_letter = set()
#for i in range(3):
    #random_letter.add(random.choice(correct_word))

#word_letters = word_letters.union(word_letters, random_letter)

while lives > 0:
    # print("You have", lives, "lives left and you have used these letters: ", ' '.join(used_letters))

    # the current word
    word_list = [letter if (letter in random_letter or letter in used_letters) else '-' for letter in correct_word]
    print(''.join(word_list))

    user_letter = input('Input a letter: ').lower()

    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print('\n')
        else:
            lives -= 1
            print('That letter doesn\'t appear in the word\n')
    elif user_letter in used_letters:
        #print('\nYou have already used that letter. Please try again.')
        print('\n')
        lives -= 1
    #else:
        #print("\nThat is not a valid letter")

'''if lives == 0:
    print('\nYou died, sorry. The word was', correct_word)
else:
    word_list = [letter if (letter in random_letter or letter in used_letters) else '-' for letter in correct_word]
    print(''.join(word_list))
    print('\n')
    #print("\nYou won! You guess the word", correct_word)'''

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
