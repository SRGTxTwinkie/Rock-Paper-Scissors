from time import sleep as wait ### Lazy Bastard that doesn't want to type time.sleep()
from random import randint as rand ### Same deal as sleep

def userTalking(): ### Sets up the game and let's the user know how to play
    print('Standard Rock Paper Scissors, you know how it goes.')
    print('Press enter to play!') ### Just wanted a little break so you can read it before playing, cuz it goes fast
    input() 
    gameplay()

def gameplay(): ### The meat that actually handles the game, it could have been about 3 functions but what the hell
    y = True
    x = rand(1,3) ### Picks the R,P,S type chosen

    while y == True: ### Ghetto Error checking, could have been a function
        
        userChoice = input('Type your choice here: ')

        if userChoice.upper() == 'SCISSORS': ### Assigns the User choice to a R,P,S type as an int
            staleMate = 1
            y = False
        elif userChoice.upper() == 'PAPER':
            staleMate = 3
            y = False
        elif userChoice.upper() == 'ROCK':
            staleMate = 2
            y = False
        else: ### This checks for a non-number or a number outside the range of 1-3
            print()
            print('Little spelling mistake you got there huh, why don\'t you try again?')
            print()
            y = True
    ### A countdown for __SUSPENSE__
    print(3)
    wait(1)
    print(2)
    wait(1)
    print(1)
    wait(1.3)

    if x == 1: ### Handles the computer Choice using the randint() from above
        print('I choose Scissors!')
    elif x == 2:
        print('I choose Rock!')
    elif x == 3:
        print('I choose Paper!')

    if staleMate == x: ### If the two answers are the same this is what happens
        print('Oops, we choose the same.')
        ending()
    ### This is what happens when the answers are not the same
    if userChoice.upper() == 'SCISSORS' and x == 3:
        wait(.5)### A little wait because the code runs crazy fast
        print('Ahh, you got me!')
    if userChoice.upper() == 'PAPER' and x == 2:
        wait(.5)
        print('Ahh, you got me!')
    if userChoice.upper() == 'ROCK' and x == 1:
        wait(.5)
        print('Ahh, you got me!')
    else: ### This is an else, because of the previous error checking nothing should be able to get through this far 
        print('I win')
    ending()

def ending(): ### Simple to ask to go again
    x = True
    while x == True:
        userAnswer = input('Would you like to go again? Y/N: ')
        if userAnswer.upper() == 'Y':
            gameplay()
        elif userAnswer.upper() != 'N':
            print('Y/N')
            x = True
        else:
            x = False
    
        
        


userTalking() ### Beginning command to start it all
