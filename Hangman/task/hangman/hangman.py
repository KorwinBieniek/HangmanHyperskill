import random

# Write your code here
print("H A N G M A N")
player_word = input("Guess the word: ")
list_of_words = ['python', 'java', 'kotlin', 'javascript']
correct_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
if player_word == correct_word:
    print("You survived!")
else:
    print("You lost!")
