import hangman_art
import hangman_words
import random

word_to_guess = random.choice(hangman_words.word_list) 


blanks = ""   
for letters in word_to_guess:
    blanks += "_"
print(word_to_guess)
print(f"Word to guess: {blanks}")


substring_to_find ="_"

while substring_to_find in blanks:
    user_input = input("Guess your letter: ")
    
    letter_index = word_to_guess.index(user_input)
    
    if (type(letter_index)) == int:
        print (f"You Guessed {user_input} which is correct. ")
        blanks_list = list(blanks)
        blanks_list[letter_index] = user_input
        blanks = "".join(blanks_list)
        print(blanks)
    else:
        print(f"You guess {user_input} which is incorrect. You lose a life.")



