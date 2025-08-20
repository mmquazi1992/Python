import hangman_art
import hangman_words
import random

word_to_guess = random.choice(hangman_words.word_list) 
print(word_to_guess)


blanks=""
for letters in word_to_guess:
    blanks+="_"
print(blanks)


user_input = input("Guess your letter: ").lower()
print(user_input)
   
display = ""

for letters in word_to_guess:
    if user_input==letters:
       display+=letters
        
    else:
        display += "_"

print(display)
