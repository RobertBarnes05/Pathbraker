# Pathbreaker.py
'''
This is a maze game, with three modes.
easy, medium and hard.
The user will type their level, play through the maze by typing the commands
'north', 'east', 'south' and 'west'.
When meeting a dead end, they will encounter a monster, which
will ask them a riddle.
The user will have three changes to answer their riddle.
If they are unable to answer they will get a game over message
and to start again.
If they can answer they will be transported to the last place where
they were on the right path.
After completing or not completing the maze they will be given the total
number of steps taken and the options of playing again.
'''

#game mode import
from Easymaze import*

#import importlib


exit=False

#Egame=False
#Mgame=False
#Hgame=False

#funtion for the game's main menu
def main_menu():
    print('MAIN MENU')
    print(' New Game')
    print(' How To Play')
    #print(' last Score')
    print(' Exit')

#menu for a new game where user selects game difficulty 
def new_game_menu():
    while True:
        print('  NEW GAME')
        print('   Easy')
        print('   Back')
        ng_menu=input('   Please type difficulty: ')
        if ng_menu=='back':
            break
            main_menu()
        elif ng_menu=='easy':
            easy()
            break
            main_menu()
        else:
            print('   Plase make a valid selection,')
            print('   please check your spelling,')
            print('   did you remember spaces or lower case only')
            print(' ')
    
#loading the easy game mode
def easy ():
    easystart(steps, Evampire, Ewerwolf, Ezombie, Emummy, Edragon)
    
#game instructions
def insturctions():
    print(' GAME INSTURCTIONS:')
    print (' ')
    main_menu
    
#display player last steps taken score
#currently not working due to modules variables reseting to defult after game mode plays out
#def score():
    #importlib.reload(Easymaze)
    print(' ')
    Esteps(steps)
    #Msteps(steps)
    #Hsteps(steps)
    
#Game loop
while not exit:
    main_menu()
    main_input = input(' Please type your selection: ' )
    if main_input == 'exit':
        #change exit to true ending the program
        exit=True
    elif main_input == 'new game':
        #open up new game menu
        new_game_menu()
    elif main_input=='how to play':
        ##open how to play text
        insturctions()
    #elif main_input=='last score':
        #display last score
        score()
    else:
        print(' Plase make a valid selection,')
        print(' please check your spelling,')
        print(' did you remember spaces or lower case only')
        print(' ')


