#Guessingn  Game - Husuke Nishioka

import  random

def  generate_random_number():
    return random.randint(1, 100)
    

def get_user_guess():
    while True:
        user_input = int(input("Please guess a number between 1 through 100:"))
        if  user_input >= 1 and user_input <= 100:
            return user_input
        else:
            print("Invalid input")

def playing_guessing_game():
    secret_number = int(generate_random_number())
    guesses = 0
    i = 1
    while i >= 1 or i <= 100:
        user_guess = get_user_guess()
        guesses += 1
        if user_guess < secret_number:
            print("Your guess is too low.")
        elif user_guess > secret_number:
            print("Your guess is too large.")
        else:
            print(f"Your guess is correct! It took you {guesses} guesses!")
            break

def game_loop(): 
    while True:
        playing_guessing_game()
        play_again = (input ("Would you like to play again?"))
        if play_again == "yes":
            playing_guessing_game()
        if play_again == "no":
            break


        
        
        


if __name__ == "__main__": 
    game_loop()



    


    

