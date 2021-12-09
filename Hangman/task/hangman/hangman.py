import random

# Write your code here
print("H A N G M A N")
list_of_words = ['python', 'java', 'kotlin', 'javascript']
correct_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
print(correct_word[:3], end='')
for i in range(len(correct_word) - 3):
    print('-', end='')
print()
player_word = input("Guess the word: ")

if player_word == correct_word:
    print("You survived!")
else:
    print("You lost!")
