#easymaze.py
"""This is the easy mode for the pathbreaker game (pathbreak.py).
This maze will consist of five monsters, a vampire, werwolf, zomibe,
mummy and dragon.
in order to complete the maze the user will need to navagate through the maze,
using the commands 'north', 'east', 'south' and west.
if user encounters a monster they will be asked a riddle and given three
chances to guess the riddle correctly if they are unable to they will be
promted with a game over message.
If tghey guess correctly they will be transported to the last location
they were on the right path."""

#initialise veribles

complete=False

#reset monster answers to false
Evampire=False
Ewerwolf=False
Ezombie=False
Emummy=False
Edragon=False
Espider=False

#setting riddles and answers
ERvampire='A very pretty thing am I, fluttering in the pale-blue sky. Delicate, fragile on the wing, indeed I am a pretty thing. What am I?'
ERAvampire='butterfly'

ERwerwolf='What cant be burned in fire, nor drowned in water?'
ERAwerwolf='ice'

ERzombie='I have four of these, With matching extremities. They can do many things, And hardly ever bring me pain. Unless I stick them with a pin, Or burn them sometimes when... What is it that I can wiggle at will? And use in other means still?'
ERAzombie='fingers'

ERmummy="David's father has three sons : Snap, Crackle and _____ ?"
ERAmummy='david'

ERdragon='What can run but never walks, what has a mouth but never talks, has a bed but never sleeps,has a head, but never weeps?'
ERAdragon='river'

ERspider='I can fly but have no wings. I can cry but I have no eyes. Wherever I go, darkness follows me. What am I?'
ERAspider='clouds'


#game over
def game_over(steps,complete):
    print('GAME OVER!')
    print(' ')
    print(' ')
    Esteps(steps,complete)
    print(' ')
    print(' ')
    #easy maze finsihes and returns to Pathbreaker's main menu

#final steps calculater
def Esteps(steps,complete):
    final_steps=steps
    if complete==True:
        print('You completed easy mode in, ', final_steps,'!')
    else:
        print('You died in easy mode with, ',final_steps,'taken.')

#first junction
def greenroute1(steps, Evampire):
    if Evampire==True:
        print ('A the sound of the wall closes in the distance.')
        print ('You have bested the Vampire!')
        print ('you have been teleported to your last correct position.')
        print ('you are facing north you have only one direction to go, west.')
        print('You take ten steps west,')
        steps=steps+10
        print('turn and take eight steps north,')
        steps=steps+8
        print('two east, two north, two west,')
        steps=steps+6
        print('eight steps north, four east, two south')
        steps=steps+8+4+2
        print('three west, three south and two east.')
        steps=steps+3+3+2
        greenroute2(steps, Ewerwolf)
        print(' ')
    else:
        end=False
        while end==False:
            print ('The entrance closes behind you. There are two paths before you, one east the other west.')
            direction=input('Which way do you go: ')
            if direction=='east':
                print(' ')
                redroute(steps, Evampire)
                end=True
            elif direction=='west':
                print('You take ten steps west,')
                steps=steps+10
                print('turn and take eight steps north,')
                steps=steps+8
                print('two east, two north, two west,')
                steps=steps+6
                print('eight steps north, four east, two south')
                steps=steps+8+4+2
                print('three west, three south and two east.')
                steps=steps+3+3+2
                print(' ')
                greenroute2(steps, Ewerwolf)
                end=True
            else:
                print('Plase make a valid selection,')
                print('please check your spelling,')
                print('did you remember spaces or lower case only')
                print(' ')

#second junction
def greenroute2(steps, Ewerwolf):
    if Ewerwolf==True:
        print ('A the sound of the wall closes in the distance.')
        print ('You have bested the Werwolf!')
        print ('you have been teleported to your last correct position.')
        print('You are faceing east, there now only one path; south.')
        print('You walk south for three steps.')
        steps=steps+3
        print(' ')
        greenroute3(steps,Ezombie)
    else:
        while True:
            print('You are facing east, the road forks infront of you,')
            print('one path to the north, the other to the south')
            direction=input('Which way do you go: ')
            if direction=='north':
                print(' ')
                pinkroute(steps, Ewerwolf)
                break
            elif direction=='south':
                print('You walk south for three steps.')
                steps=steps+3
                print(' ')
                greenroute3(steps, Ezombie)
                break
            else:
                print('Plase make a valid selection,')
                print('please check your spelling,')
                print('did you remember spaces or lower case only')
                print(' ')
                


#third juntion            
def greenroute3(steps, Ezombie):
    if Ezombie==True:
        print ('A the sound of the wall closes in the distance.')
        print('The Zombie has been defeated!')
        print('you have been teleported to your last correct position in the maze.')
        print('You are facing south, only one path now remains; west.')
        print('You walk west for two steps.')
        steps=steps+2
        print('you turn south and walk for four steps,')
        steps=steps+4
        print('the path turns to face east for seven steps,')
        steps=steps+7
        print('you turn north to take three steps, west two steps, north for eight,')
        steps=steps+3+2+8
        print('truning east for three steps, north for two, west taking two,')
        steps=steps+3+2+2
        print('north taking two steps, east for three north again for two, east taking three')
        steps=steps+2+3+2+3
        print('you moves south for three and then east for two')
        steps=steps+3+2
        print(' ')
        greenroute4(steps, Emummy)
    else:
        while True:
            print('You are facing south, there is two roads you can take,')
            print('one path to the south, the other to the west')
            direction=input('Which way do you go: ')
            if direction=='south':
                print(' ')
                orangeroute(steps, Ezombie)
                break
            elif direction=='west':
                print('You walk west for two steps.')
                steps=steps+2
                print('you turn south and walk for four steps,')
                steps=steps+4
                print('the path turns to face east for seven steps,')
                steps=steps+7
                print('you turn north to take three steps, west two steps, north for eight,')
                steps=steps+3+2+8
                print('truning east for three steps, north for two, west taking two,')
                steps=steps+3+2+2
                print('north taking two steps, east for three north again for two, east taking three')
                steps=steps+2+3+2+3
                print('you moves south for three and then east for two')
                steps=steps+3+2
                print(' ')
                greenroute4(steps, Emummy)
                break
            else:
                print('Plase make a valid selection,')
                print('please check your spelling,')
                print('did you remember spaces or lower case only')
                print(' ')
                

#forth junction.
def greenroute4(steps, Emummy):
    if Emummy==True:
        print ('A the sound of the wall closes in the distance.')
        print('The Mummy has been defeated!')
        print('You have been teleported to your last correct position in the maze.')
        print('You are facing east, the only path that remains is; east')
        print('You walk east taking four steps')
        steps=steps+4
        print('the path turns south and you take three steps')
        steps=steps+3
        print(' ')
        greenroute5(steps,Edragon)
    else:
        while True:
            print('You are currently facing east,')
            print('there are two paths to choose from, too the right; south,')
            print('and ahead; east.')
            direction=input('Which way do you go: ')
            if direction=='south':
                print(' ')
                blueroute(steps,Emummy)
                break
            elif direction=='east':
                print('You walk east taking four steps')
                steps=steps+4
                print('the path turns south and you take three steps')
                steps=steps+3
                print(' ')
                greenroute5(steps,Edragon)
                break
            else:
                print('Plase make a valid selection,')
                print('please check your spelling,')
                print('did you remember spaces or lower case only')
                print(' ') 

#fifth junction
def greenroute5(steps, Edragon):
    if Edragon==True:
        print ('A the sound of the wall closes in the distance.')
        print('The Dragon has been slayen!')
        print('You have been teleported to your last correct position in the maze.')
        print('You are facing south, there is just one way to go; east.')
        print('You take two steps east,')
        steps=steps+2
        print('turning north you take four steps')
        print('followed by five steps west,')
        steps=steps+4+5
        print('two steps north, six east,')
        steps=steps+2+6
        print('you turn south and take eight steps, followed by two west')
        steps=steps+8+2
        print('and two south.')
        print(' ')
        greenroute6(steps,Espider)
    else:
        while True:
            print('You are currently facing south,')
            print('there are two paths to choose from, ahead there lays; south,')
            print('and to your left; east.')
            direction=input('Which way do you go: ')
            if direction=='south':
                print(' ')
                brownroute(steps,Edragon)
                break
            elif direction=='east':
                print('You take two steps east,')
                steps=steps+2
                print('turning north you take four steps')
                print('followed by five steps west,')
                steps=steps+4+5
                print('two steps north, six east,')
                steps=steps+2+6
                print('you turn south and take eight steps, followed by two west')
                steps=steps+8+2
                print('and two south.')
                greenroute6(steps,Espider)
                break
            else:
                print('Plase make a valid selection,')
                print('please check your spelling,')
                print('did you remember spaces or lower case only')
                print(' ')

#sixth junction
def greenroute6(steps,Espider,complete):
    if Edragon==True:
        print ('A the sound of the wall closes in the distance.')
        print('The Giant Spider is gone!')
        print('You have been teleported to your last correct position in the maze.')
        print('You are facing south, there is just one way to go; east.')
        print('You take two steps east,')
        steps=steps+2
        #road to end
        print(' ')
    else:
        while True:
            print('You are currently facing south,')
            print('there are two paths to choose from, ahead there lays; south,')
            print('and to your left; east.')
            direction=input('Which way do you go: ')
            if direction=='south':
                print(' ')
                purpleroute(steps,Espider)
                break
            elif direction=='east':
                print('You take two steps east,')
                steps=steps+2
                print('you turn south and take six steps,')
                steps=steps+6
                print('turning west you take twelve steps,')
                steps=steps+12
                print('you take your final turn north taking six steps.')
                steps=steps+6
                print(' ')
                complete=True
                print('WELL DONE YOU HAVE COMPLETED THE MAZE, PATHBREAKER!')
                print(' ')
                game_over(steps, complete)
                break
            else:
                print('Plase make a valid selection,')
                print('please check your spelling,')
                print('did you remember spaces or lower case only')
                print(' ')
    

#frist deviation
def redroute(steps, Evampire):
    lives=3
    print('You take ten steps east')
    steps=steps+10
    print('You hit a dead end, you turn to go back when a Vampire suddenly appears!')
    print("Answer my riddle, and I'll let you be, fail to best me and there will be a feast for me")
    while lives > 0:
        if lives==1:
            print('Warning this is your last chance.')
            print(' ')
        print(ERvampire)
        red_answer=input('What is you guess? ')
        if red_answer == ERAvampire:
            Evampire=True
            print('correct')
            print(' ')
            greenroute1(steps, Evampire)
            break
        else:
            print('incorrect')
            print(' ')
            lives=lives-1
            if lives==0:
                game_over(steps,complete)
            

#second deviation
def pinkroute(steps, Ewerwolf):
    lives=3
    print('You take three steps north,')
    steps=steps+3
    print('four steps east,')
    steps=steps+4
    print('three north, and three east.')
    steps=steps+3+3
    print('You hit a dead end, you turn to go back when a Werwolf suddenly appears!')
    print("I have a question for you, if you answer true I'll tel you through.")
    print("Answer wrong and my bite will be the end of you.")
    while lives > 0:
        if lives==1:
            print('Warning this is your last chance.')
            print(' ')    
        print(ERwerwolf)
        pink_answer=input('What is you guess? ')
        if pink_answer == ERAwerwolf:
            Ewerwolf=True
            print('correct')
            print(' ')
            greenroute2(steps, Ewerwolf)
            break
        else:
            print('incorrect')
            print(' ')
            lives=lives-1
            if lives==0:
                game_over(steps,complete)

#third deviation
def orangeroute(steps, Ezombie):
    lives=3
    print('You take three steps south,')
    steps=steps+3
    print('two steps east,')
    steps=steps+4
    print('eight north, two east, eight south and two east.')
    steps=steps+8+2+8+2
    print('You hit a dead end, you turn to go back when a Zombie suddenly appears!')
    print('Arrrhhhhhhhh!!!')
    print('Arrrhhhhhhhh!!!')
    print('there seems to be some text above him that reads:')
    print("If you can pass my bar you'll stay as you are.")
    print("Fail and i'll make you into lunch ")
    while lives > 0:
        if lives==1:
            print('Warning this is your last chance.')
            print(' ')
        if lives==3:
            print('Arrrhhhhhhhh!!!')
            print('Arrrhhhhhhhh!!!')
            print('Arrrhhhhhhhh!!!')
            print('The text above the zombies changes:')
        print(ERzombie)
        orange_answer=input('What is you guess? ')
        if orange_answer == ERAzombie:
            Ezombie=True
            print('Arrrhhhhhhhh!!!')
            print('correct')
            print(' ')
            greenroute3(steps, Ezombie)
            break
        else:
            print('Arrrhhhhhhhh!!!')
            print('incorrect')
            print(' ')
            lives=lives-1
            if lives==0:
                game_over(steps,complete)


#forth deviation
def blueroute(steps,Emummy):
    lives=3
    print('You take nine steps south,')
    steps=steps+9
    print('two steps east,')
    steps=steps+2
    print('and eight north.')
    steps=steps+8
    print('You hit a dead end, you turn to go back when a Mummy suddenly appears!')
    print("you'll stay with me if you can't answer me.")
    while lives > 0:
        if lives==1:
            print('Warning this is your last chance.')
            print(' ')    
        print(ERmummy)
        blue_answer=input('What is you guess? ')
        if blue_answer == ERAmummy:
            Emummy=True
            print('correct')
            print(' ')
            greenroute4(steps, Emummy)
            break
        else:
            print('incorrect')
            print(' ')
            lives=lives-1
            if lives==0:
                game_over(steps,complete)

#fith deviation
def brownroute(steps,Edragon):
    lives=3
    print('You take six steps south,')
    steps=steps+6
    print('two steps west,')
    steps=steps+2
    print('and seven north.')
    steps=steps+7
    print('You hit a dead end, you turn to go back when a Dragon suddenly appears!')
    print("Hhmmmmm lunch, sorry I always get ahead of myself.")
    print('Please answer wrong so I can eat!')
    while lives > 0:
        if lives==1:
            print('Warning this is your last chance.')
            print(' ')    
        print(ERdragon)
        brown_answer=input('What is you guess? ')
        if brown_answer == ERAdragon:
            Edragon=True
            print('correct')
            print(' ')
            greenroute5(steps, Edragon)
            break
        else:
            print('incorrect')
            print(' ')
            lives=lives-1
            if lives==0:
                game_over(steps,complete)

#sixth deviation
def purpleroute(steps,Espider)
    lives=3
    print('You take five steps south')
    steps=steps+5
    print('turning west you take three steps')
    print('You hit a dead end, you turn to go back when a Giant Spider suddenly appears!')
    print("Yov've wondered into my leir, now answer")
    while lives > 0:
        if lives==1:
            print('Warning this is your last chance.')
            print(' ')
        print(ERspider)
        red_answer=input('What is you guess? ')
        if red_answer == ERAspider:
            Evampire=True
            print('correct')
            print(' ')
            greenroute6(steps, Espider)
            break
        else:
            print('incorrect')
            print(' ')
            lives=lives-1
            if lives==0:
                game_over(steps,complete)

#reset steps taken
steps=0

#maze start
def easystart(steps, Evampire, Ewerwolf, Ezombie, Emummy, Edragon):
    #reset monster answers to false
    steps=0
    Evampire=False
    Ewerwolf=False
    Ezombie=False
    Emummy=False
    Edragon=False
    print ('Welcome to the maze, Pathbreaker!')
    print('The walls are as tall as the eye can see, you can not see over the maze,')
    print('You enter the maze taking two steps north.')
    steps=steps+2
    greenroute1(steps, Evampire)

