# Rockborne Python Project
# Guess The Number Game
# Author: Adam Choy
# Date: 6th March 2026

from random import randint

#Present rules to the user
print("Welcome to the Guessing Game!")
print("The objective is to guess a number between 1-100.")
print("You have five guesses to guess correctly.")

print("1. Play Game")
print("2. See Rules")
print("3. See Stats")
print("4. Quit")
option = int(input("Enter an option: "))




#Generating random number 
number = randint(1,100)
#print(number)
guess = 0
score = 0
guess_counter = 0
#Loop guesses until player guesses correct number
#def guessing_game():
while guess != number and guess_counter <5:
    print("")
    print(str(5-guess_counter)+"/5 guesses left.")
    guess = int(input("Guess a number: "))
    guess_counter = guess_counter + 1
    
    #Number is too high
    if guess > number:
        print (guess,str(" is too high"))
        if (guess - number) >= 1 and (guess - number) < 4:
            print("Within 3!")
        elif (guess - number) >= 4 and (guess - number) < 11:
            print("Within 10")
        else:
            print("Far...")
    #Number is too low
    elif guess < number:
        print (guess,str(" is too low"))
        if (number - guess) >= 1 and (number - guess) < 4:
            print("Within 3!")
        elif (number - guess) >= 4 and (number - guess) < 11:
            print("Within 10")
        else:
            print("Far...")
    #Guess is correct
    elif number == guess:
        print(str(guess)+" is correct!")
        print ("You Win!")
        print ("*10 Points*")
        score = score + 10
        print("")
        print ("1. Play Again?")
        print ("2. Quit")
        again_or_quit = int(input("Enter number: "))
        print("")
        if again_or_quit == 1:
            print("Playing Again")
        elif again_or_quit == 2:
            print("Thank you for playing!") 
    else:
        print ("Error")
else:
    print("Out of Guesses!")
    print("The hidden number was"+str(number))

    
    

