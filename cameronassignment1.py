import random
from random import randint
print('Welcome to the number guessing game!')
seed = input('Enter random seed: ')
random.seed(seed)
print()
def game():
    number = randint(1, 100)
    
    guess = int(input("Please enter a guess: "))
    count = 1

    while count >= 1:
        if number > guess:
            count += 1
            print("Higher")
            print()
            guess = int(input("Please enter a guess: "))
        elif number < guess:
            count += 1
            print("Lower")
            print()
            guess = int(input("Please enter a guess: "))
        else:
            print("Congratulations. You guessed it!")
            print("It took you " + str(count) + " guesses.")
            print()
            again = input("Would you like to play again (yes/no)?")
            if again == 'yes':
              print()
              game()
            else:
              break  
              
    print('Thank you. Goodbye.')        
game()