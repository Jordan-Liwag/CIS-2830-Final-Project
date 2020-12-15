import random
#import random is used to pick a random element from a list, in this case choosing a number between 1 and 6
def dice_roll():
    #define function gives the function a unique identifier
    while True:
        #while loop allows for the code to execute a command as long as the statement is true
        print("The Dice rolled: " + str(random.randint(1,6)))
        #prints "the Dice rolled" and a random number in the range of 1 being the minimum and 6 being the maximum
        roll_dice_again = input("Would you like to roll again? \nyes or no? ")
        #the dice can be rolled again, but requires the user to input if they want to roll or not 
        while roll_dice_again != 'yes':
            #when the user inputs yes the dice is rolled again to provide a new number
            if roll_dice_again == 'no':
                #if the user inputs "no" then the dice is not rolled and a statement is printed 
                return print("Thank You for rolling")
            #statement that is printed if the input is "no"
            else:
                #else function
                print("Input not recognized")
                #prints if input is not "yes" or "no"
                roll_dice_again = input("Would you like to roll again? \nyes or no:  ")
                #allows user to input "yes" or "no"

def gamestart():
    #define function for beginning of the dice rolling game 
    game_start = input("Would you like to roll the dice?")
    #allows the user to roll the dice at the first interaction
    if game_start == 'yes':
        #when user inputs "yes" the dice roll function is started
        dice_roll()
        #call to function "dice_roll"
    else:
        #if an input besides "yes" or "no" is put the game will not start
        print('Invalid Response: Dice Rolling Game must be restarted')
        #prints "Invalid Response"

if __name__ == '__main__':
    #executes all code in the function while true
    gamestart()
    #starts the first function 