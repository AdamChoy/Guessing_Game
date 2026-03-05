# Rockborne Python Project
# Guess The Number Game
# Author: Adam Choy
# Date: 6th March 2026

from random import randint

#Declaring variables to be tracked as game is played
games_played = 0
games_won = 0
score = 0

#First message that user sees
#Outside of menu() so welcome message is not repeated when menu() is called
print("\nWelcome to the Guessing Game!")

#Rules Function
def rules(): 
    "Present rules to the user"
    print("\nThese are the rules of The Guessing Game:")
    print("\n- Your objective is to guess a hidden number between 1-100.")
    print("- You have five tries to guess the hidden number.")
    print("- If you guess correctly, you win 10 points.")
    print("- If you fail to guess within five tries, you win 0 points.")
    print("- Have fun!")
    input("\nPress Enter to return to the main menu. ")
    menu()

#Menu Function with four options
def menu():
    "Presents menu to the user"
    print("\n1. Play Game")
    print("2. Read the Rules")
    print("3. See your Stats")
    print("4. Quit Game")
    menu_option = int(input("\nEnter an option: "))
    if menu_option == 1:
        guessing_game()
        return
    elif menu_option == 2:
        rules()
        return
    elif menu_option == 3:
        stats()
        return
    elif menu_option == 4:
        print("\nThank you for playing.")
        print("Goodbye!\n")
        return
    else:
        print("Please enter a number between 1 and 4.")

    
#Playing stats function       
def stats():
    print("\nYour Stats:")
    print("\nGames played:",games_played)
    print("Games won:",games_won)
    print("Score:",score)
    input("\nPress Enter to return to the main menu. ")
    menu()

#Play again or return to menu 
def play_again():
    print ("\n1. Play Again?")
    print ("2. Return to Menu?")
    again_or_quit = int(input("\nEnter number: "))
    if again_or_quit == 1:
        print("\nPlaying Again")
        guessing_game()
    elif again_or_quit == 2:
        print("\nReturning to Menu...")
        menu()
    else:
        print("Error")

#Guessing game function
def guessing_game():
    global games_played
    global games_won
    global score

    guess_counter = 0
    guess = 0
    
    #Generates random number from 1-100
    number = randint(1,100)

    #Loop attempts until player guesses correct number or is under five attempts
    while guess != number and guess_counter <5:
        print("")
        print(str(5-guess_counter)+"/5 guesses left.")
        guess = int(input("Guess a number: "))
        guess_counter = guess_counter + 1
        
        #Guess is higher
        if guess > number:
            print(guess,"is too high.")
            if (guess - number) >= 1 and (guess - number) < 4:
                print("Hint: You are within 3!")
            elif (guess - number) >= 4 and (guess - number) < 11:
                print("Hint: You are within 10...")
            elif (guess - number) >= 11 and (guess - number) < 26:
                print("Hint: You are within 25.")
            else:
                print("Hint: You are not even close.")

        #Guess is lower
        elif guess < number:
            print (guess,"is too low.")
            if (number - guess) >= 1 and (number - guess) < 4:
                print("Hint: You are within 3!")
            elif (number - guess) >= 4 and (number - guess) < 11:
                print("Hint: You are within 10...")
            elif (number - guess) >= 11 and (number - guess) < 26:
                print("Hint: You are within 25.")
            else:
                print("Hint: You are not even close.")

        #Guess is correct
        elif number == guess:
            score = score + 10
            games_won = games_won + 1
            print(str(guess)+" is correct!")
            games_played = games_played + 1
            print ("You Win!")
            print ("*10 Points*")
            play_again()
        else:
            print ("Error")
    else:
        print("\nOut of Guesses!")
        print("The hidden number was "+str(number)+".")
        games_played = games_played + 1
        play_again()

menu()
    
    

