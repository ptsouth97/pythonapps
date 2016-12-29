import random

print('--------------------------------')
print('    GUESS THAT NUMBER APP       ')
print('--------------------------------')
print()

the_number = random.randint(0, 100)

guess_text = input('Guess a number between 0 and 100: ')

guess = int(guess_text)

print(guess_text, type(guess_text))
print(guess, type(guess))
