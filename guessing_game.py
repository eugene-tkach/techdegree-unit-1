import random

LOWER_LIMIT = 1     # Constant for lower limit
UPPER_LIMIT = 10    # Constant for higher limit

# Checks that developer has not mixed up UPPER and LOWER limits and corrects if needed. Proof of concept.
#if UPPER_LIMIT < LOWER_LIMIT:
#    temp = UPPER_LIMIT
#    UPPER_LIMIT = LOWER_LIMIT
#    LOWER_LIMIT = temp
#else:

# Define a function to input your guess, for future use to allow changes in wording
def input_answer():
    return input("Pick a number between {} and {}:   ".format(LOWER_LIMIT,UPPER_LIMIT))

def start_game():

    #Welcome screen
    print("---------------------------------------------------------------")
    print("-------------Welcome to the Numbers Guessing Game!-------------")
    print("---------------------------------------------------------------")
    
    rand_num = random.randint(LOWER_LIMIT,UPPER_LIMIT)  # Generates the first random number based on a range as defined but CONSTANTS declared at the start of the script, to check against player's guess
    playing = "y"                                       # Defines and sets the variable to check condition for the game to continue before exiting
    answer = ""                                         # Declares and sets player input as it is referenced before user's first input
    num_of_guesses = 0                                  # Declares and sets the starting number of guesses a player has made
    highscore = 100                                     # Declares and defines highscore to a high number to check against the first iteration of the game. The score is high so that the first iteration of the game prompts the player that they've set a new highscore

    # Checks that you still want to continue playing the game
    while playing.upper() == "Y":
                
        try:
            # While the answer is not equal to the random number, continue to ask for input
            while answer != rand_num:
                
                answer = int(input_answer())
                
                # Checks if the answer is within the random numbers range
                if answer < LOWER_LIMIT or answer > UPPER_LIMIT:
                    print("That number is outside of specified range.")
                
                # If the answer is higher, prompt user
                elif answer > rand_num:
                    print("It is lower!")
                    num_of_guesses += 1
                
                # If the answer is not higher nor is it the correct answer, the guess must be lower.
                elif answer < rand_num: 
                    print("It is higher!")
                    num_of_guesses += 1
                else:
                    num_of_guesses += 1
                    
            else:
                
                # Prompt the user that they guessed correctly
                print("You got it! It took you {} tries.".format(num_of_guesses))
                
                # Check the number of guesses against the highscore, if they are lower than the highscore prompt user that they set a new highscore
                if highscore > num_of_guesses:
                    highscore = num_of_guesses
                    print("Congrats! You set a new highscore of {}!".format(highscore))
                    
                # If the player tied with the current highscore, prompt them as such     
                elif highscore == num_of_guesses:
                    print("Looks like you tied the old highscore. Still, well done!")
                
                # If the player didn't beat the highscore nor tied, they must have had more guesses than the highscore
                else:
                    print("Looks like you didn't quite beat the highscore of {}. Might want to give it another go.".format(highscore))
                
                # Prompt the user to see if they would like to continue playing
                choice = input("Would you like to play again? [y]es/[n]o?  ")
                
                # If the choice is neither Y or N, then prompt the user their input is invalid
                while choice.upper() != "Y" and choice.upper() != "N":
                    print("Please answer either Y or N.")
                    choice = input("Would you like to play again? [y]es/[n]o?  ")
                    
                # Otherwise, check their choice against the IF tree
                else:                     
                    if choice.upper() == "Y":
                        print("Great! The HIGHSCORE to beat is {}.".format(highscore))
                        
                        # Generate a new random number and reset the player's number of guesses and answer
                        rand_num = random.randint(1,10)
                        num_of_guesses = 0
                        answer = ""
                        
                    # If the input is valid and it is a N, then set condition to exit loop to N to exit game    
                    else:
                        print("Gotcha! Thanks for playing!")
                        playing = "N"
        
        # Handle any inputs other than numeric inputs as an error
        except ValueError as err:
            print("Oops! Sorry, I only understand numerical inputs. Please try again...")
        
    else:
        print("Exiting program.")
            


# Kick off the program by calling the start_game function.
start_game()