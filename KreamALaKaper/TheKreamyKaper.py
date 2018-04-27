##The Kreamy Kaper v.1
##The MIT License (MIT)
##Copyright (c) 2016 Bernard Grant
##
##Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
##(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish,
##distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the
##following conditions:
##
##The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
##MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
##FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
##SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
##
import time
import os
import sys
import random
global lives
lives=3
global inventory
inventory=[]
class items():#determines what you get from boxes and fallen guards
    def __init__(self):
        get=random.randrange(1,4)
        if get==1:
            inventory.append('Donut')
            print('donut')
        elif get==2:
            inventory.append('Night Vision Goggles')
            print('night vision goggles')
        elif get==3:
            inventory.append('Pepper Spray')
            print('pepper spray')
def world(save):#actual game
    global lives
    global inventory
    lives=3
    os.system('cls')
    savefile=open(save,'r')
    roomsave=savefile.readline()
    savefile.close()
    if roomsave=='1':
        filename='tutorial1.txt'
    elif roomsave=='2':
        filename='tutorial2.txt'
    elif roomsave=='3':
        filename='tutorial3.txt'#checking to see what level you are on
    elif roomsave=='4':
        filename='tutorial4.txt'
    file=open(filename,'r')
    line=file.readline()
    file.close()
    player=line.split()
    guardnum=0
    switch=0
    while lives!=0:#entire game takes place inside an enormous "while you aren't dead" loop
        file=open(filename,'r')
        line=file.readline()
        line=file.readline()
        rowlist=[]
        while line:
            line=line.split()
            rowlist.append(int(line[0]))
            line=file.readline()
        file.close()
        row=1
        if switch!=1:
            for i in range(max(rowlist)):#visuals
                visual=''
                file=open(filename,'r')
                line=file.readline()
                line=file.readline()
                while line:
                    line=line.split()
                    isplayer=[]
                    isplayer.append(line[0])
                    isplayer.append(line[1])
                    if int(line[0])==row:#creates strings of each line of the world, then prints them
                        if player!=isplayer:
                            if str(line[2])=='none':
                                visual=visual+'-'
                            elif str(line[2])=='guard':
                                visual=visual+'G'
                            elif str(line[2])=='wall':
                                visual=visual+'X'
                            elif str(line[2])=='box':
                                visual=visual+'B'
                            elif str(line[2])=='door':
                                visual=visual+'D'
                            elif str(line[2])=='sight':
                                if guardnum<1:
                                    if 'Night Vision Goggles' in inventory:
                                        visual=visual+'V'
                                    else:
                                        visual=visual+'-'
                                else:
                                    visual+='-'
                            elif str(line[2])=='switch':
                                visual=visual+'S'
                        if isplayer[0]==player[0]:#players location
                            if isplayer[1]==player[1]:
                                visual+='@'
                    line=file.readline()
                print(visual)
                row+=1
                file.close()
        file=open(filename,'r')
        line=file.readline()
        x=int(player[0])
        y=int(player[1])
        move=input("move ")
        if move=='d':#simple coordinate based movement
            y+=1
        elif move=='a':
            y-=1
        elif move=='w':
            x-=1
        elif move=='s':
            x+=1
        elif move=='i':
            stuffs=str(inventory)
            stuffs=stuffs.replace(',','\n')
            stuffs=stuffs.replace("'",'')
            stuffs=stuffs.replace('[','')
            stuffs=stuffs.replace(']','')
            print(stuffs)
        else:
            print('Please use WASD for movement.')
        player=[]
        x=str(x)
        y=str(y)
        player.append(x)
        player.append(y)
        line=file.readline()
        while line:#i don't remember what this is supposed to do, so it is probably very, very important
            line=line.split()
            tile=line[2]
            del line[2]
            if player==line:
                break
            else:
                line=file.readline()
        line=''
        file.close()#these are simply determining what happens because of the area you are on in the map
        if tile=='none':
            tile=''
        elif tile=='guard':#running into a guard is quite dangerous, uses random to determine if you successfully fight the guard, running is always successful though.
            if guardnum>=1:
                print('Nothing but an unconsious guard. ')
            else:
                try:
                    forf=int(input('There is a guard here.\n1. Quick Takedown\n2. Run\n'))
                except:
                    forf=int(input('There is a guard here.\n1. Quick Takedown\n2. Run\n'))
                if forf!=1:
                    if forf!=2:
                        forf=int(input('There is a guard here.\n1. Quick Takedown\n2. Run\n'))
                if forf==1:
                    if 'Pepper Spray' in inventory:
                        print('Success!')
                        search=input('Will you search the guard?\ny/n')
                        guardnum+=1
                        if search=='y':
                            items()
                        elif search=='n':
                            print('You leave before anything else happens')
                    else:
                        lose=int(random.randrange(1,3))
                        if lose==1:
                            print('Success!')
                            search=input('Will you search the guard?\ny/n')
                            guardnum+=1
                            if search=='y':
                                items()
                            elif search=='n':
                                print('You leave before anything else happens')
                        elif lose==2:
                            print('Failure.')
                            lives-=1
                            file=open(filename,'r')
                            line=file.readline()
                            player=line.split()
                            file.close()
                            print('Lives =',lives)
                elif forf==2:#it's just the wall code
                    print('You leave without being seen.')
                    x=int(player[0])
                    y=int(player[1])
                    player=[]
                    if move=='d':
                        y-=1
                    elif move=='a':
                        y+=1
                    elif move=='w':
                        x+=1
                    elif move=='s':
                        x-=1
                    x=str(x)
                    y=str(y)
                    player.append(x)
                    player.append(y)
                tile=''
                time.sleep(3)
        elif tile=='wall':#was actually quite fun trying to figure out walls, they just move you in the opposite direction you tried to move, so you end up not actuall moving, i'll probably use this for other things later
            print('that is a wall, you cant go that way')
            x=int(player[0])
            y=int(player[1])
            player=[]
            if move=='d':
                y-=1
            elif move=='a':
                y+=1
            elif move=='w':
                x+=1
            elif move=='s':
                x-=1
            x=str(x)
            y=str(y)
            player.append(x)
            player.append(y)
            time.sleep(3)
        elif tile=='box':#runs item class
            print('There is a box here.')
            box=str(input('1. Open Box\n2. Leave box\nWhat will you do? '))
            if box=='1':
                items()
            elif box=='2':
                print('You leave the box alone.')
                time.sleep(2)
        elif tile=='sight':
            if guardnum>=1:
                tile=''
            else:
                if switch!=1:
                    print("You've been spotted! ")
                    lives-=1
                    print('Lives =',lives)
                    file=open(filename,'r')
                    line=file.readline()
                    player=line.split()
                    file.close()
                    time.sleep(2)
        elif tile=='switch':
            flip=int(input('There is a switch here.\n1. Flip the switch\n2. Leave it alone\nWhat will you do? '))
            if flip==1:
                if switch==1:
                    switch-=1
                elif switch==0:
                    switch+=1
                x=int(player[0])
                y=int(player[1])
                player=[]
                if move=='d':
                    y-=1
                elif move=='a':
                    y+=1
                elif move=='w':
                    x+=1
                elif move=='s':
                    x-=1
                x=str(x)
                y=str(y)
                player.append(x)
                player.append(y)
                time.sleep(3)
                print('*flip*')
            elif flip==2:
                print('You leave the switch alone')
                x=int(player[0])
                y=int(player[1])
                player=[]
                if move=='d':
                    y-=1
                elif move=='a':
                    y+=1
                elif move=='w':
                    x+=1
                elif move=='s':
                    x-=1
                x=str(x)
                y=str(y)
                player.append(x)
                player.append(y)
                time.sleep(3)
        elif tile=='door':#opens next sequential file, I guess all of them will be named tutorial, but o well this isn't supposed to be professional
            print('yay\n\n\n\n\n\non to the next room then')
            guardnum=0
            switch=0
            filename=list(filename)
            roomnum=filename[-5]
            roomnum=int(roomnum)
            roomnum+=1
            roomnum=str(roomnum)
            save=open(save,'w')
            save.write(roomnum)
            save.close()
            filename='tutorial'+roomnum+'.txt'
            if filename=='tutorial5.txt':
                victory()
            file=open(filename,'r')
            line=file.readline()
            player=line.split()
            file.close()
            time.sleep(3)
        os.system('cls')
    print('''
 _______  _______  _______  _______    _______           _______  _______ 
/  ____ \/ _____ \/       \/  ____ \  /  ___  \|\     /|/  ____ \/ _____ \    
| /    \/| \   / || /\ /\ || /    \/  | /   \ || \   / || /    \/| \   / |
| |      | /___\ || || || || \___     | |   | || |   | || \___   | /___\ |
| | ____ | _____ || |\_/| ||  __/     | |   | |\ \   / /|  __/   |    ___/
| | \_  \| \   / || |   | || /        | |   | | \ \_/ / | /      | |\ \   
| \___/ || /   \ || /   \ || \____/\  | \___/ |  \   /  | \____/\| / \ \__
\_______/|/     \||/     \|\_______/  \_______/   \_/   \_______/|/   \__/
    ''')
    time.sleep(5)
    menu1()
def tutorial(file):#gives tutorial information
    print('Welcome to The Kreamy Kaper!\nThe controls for this game are quite simple.\n - WASD represent the four cardinal directions, and can be used in order to move.\n - I opens your inventory.\n - You must press enter after each key press in order to progress.')
    cont=input('press enter to continue')
    print("You will notice a series of characters appearing on the screen upon startup, these characters represent the world.\n - X is a wall.\n - - represents nothing on a tile.\n - G is a guard.\n - V represents a guard's field of vision, and can only be seen whilst wearing Night Vision Goggles\n - B is a chest which one can open to reveal goodies of all sorts\n - S is a light switch which will negate a guards vision, but will also negate your own.\n - D is a door which will lead one to the next room.")
    cont=input('press enter to continue')
    print("If you want extra loot, you can get some by using pepper spray to take down a guard, if you don't have pepper spray, you can try your luck and go after them anyway, but there are no guarentees there.")
    world(file)
def victory():
    print('''
 _    _ _____ _______ _______  _____   ______ __   __
  \  /    |   |          |    |     | |_____/   \_/  
   \/   __|__ |_____     |    |_____| |    \_    |   
                                                     
''')
    sys.exit()
def menu1():#simple main menu
    try:
        os.system('cls')
        print('''
 ____ _          _  __                               _  __                     
|  __| |__   ___| |/ /_ __ ___  __ _ _ __ ___  _   _| |/ /__ _ _ __   ___ _ __ 
| |  | '_ \ / _ | ' /| '__/ _ \/ _` | '_ ` _ \| | | | ' // _` | '_ \ / _ | '__|
| |  | | | |  __| . \| | |  __| (_| | | | | | | |_| | . | (_| | |_) |  __| |   
|_|  |_| |_|\___|_|\_|_|  \___|\__,_|_| |_| |_|\__, |_|\_\__,_| .__/ \___|_|   
                                               |___/          |_|              


                                                        ''')
        gamestart=int(input('1. New Game\n2. Load Game\n3. Quit Game\nPlease select an available option. '))
        if gamestart==1:
            os.system('cls')
            filename=int(input('File 1\nFile 2\nFile 3\nPlease select a file. '))
            if filename==1:
                yorn=input('Are you sure you wish to use File 1?\ny/n ')
                if yorn=='y':
                    file=open('File 1.txt','w')
                    file.write('1')#overwrites all file data
                    file.close()
                    tutorial('File 1.txt')#just passes which file to open along for saving purposes
                else:
                    menu1()
            elif filename==2:
                yorn=input('Are you sure you wish to use File 2?\ny/n ')
                if yorn=='y':
                    file=open('File 1.txt','w')
                    file.write('1')
                    file.close()
                    tutorial('File 2.txt')
                else:
                    menu1()
            elif filename==3:
                yorn=input('Are you sure you wish to use File 3?\ny/n ')
                if yorn=='y':
                    file=open('File 1.txt','w')
                    file.write('1')
                    file.close()
                    tutorial('File 3.txt')
                else:
                    menu1()
        elif gamestart==2:#passes proper info now
            os.system('cls')
            filename=int(input('File 1\nFile 2\nFile 3\nPlease select a file. '))
            if filename==1:
                yorn=input('Are you sure you wish to use File 1?\ny/n ')
                if yorn=='y':
                    tutorial('File 1.txt')#just passes which file to open along for saving purposes
                else:
                    menu1()
            elif filename==2:
                yorn=input('Are you sure you wish to use File 2?\ny/n ')
                if yorn=='y':
                    tutorial('File 2.txt')
                else:
                    menu1()
            elif filename==3:
                yorn=input('Are you sure you wish to use File 3?\ny/n ')
                if yorn=='y':
                    tutorial('File 3.txt')
                else:
                    menu1()
        elif gamestart==3:
            sys.exit()
        else:
            print('Please select an available option. ')
            time.sleep(2)
            menu1()
    except:
        menu1()
def intro():#gives basic story infos and stuff, maybe with simple ascii art
    menu1()
## Just gonna take this out to make debugging quicker
##    intro=input('Would you like to skip the introduction?\ny/n ')
##    if intro=='n':
##        print("")
##        time.sleep(2)
##        menu1()
##    elif intro=='y':
##        print("")
##        time.sleep(2)
##        menu1()
##    else:
##        print('please select an available option')
##        time.sleep(2)
##        os.system('cls')
##        intro()
intro()
