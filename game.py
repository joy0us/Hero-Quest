#game.py
#Aug. 30, 2014
#renwave of Reddit

import pygcurse, pygame, sys,random, time
from pygame.locals import *


def checkMenu(x): #For while loops in various menus
    global inMenu
    if x == 1:
        inMenu = True
    if x == 0:
        inMenu = False

class Display: #This is just to keep things organized
    def __init__(self,win):
        self.win = win

    def setWindow(self):
        global win
        win = pygcurse.PygcurseWindow(40, 25)
        win.autoblit = False
        #win.autoupdate = False
        return win
        
class GameStateManager: #For organization, keeps menus
    #0 start menu
    #1 pause menu
    #2 character sheet
    #3 quest log
    #4 newClass dialogue
    #5 advClass dialogue
    #6 new charecter dialogue
    #7 class selections screen
    #8 new char confirm screen

    @staticmethod
    def displayMenu(x):
        checkMenu(1)
        if x == 0: #Main window when you first run the Game
            win.setscreencolors('white', 'blue', clear=True)
            win.cursor = (5,4)
            win.write('   ### ####### ##### #####    ')
            win.cursor = (5,5)
            win.write('   #.# #.#....#.....#     #   ')
            win.cursor = (5,6)
            win.write('   #.###.#.##.#..#..#  #  #   ')
            win.cursor = (5,7)
            win.write('   #.....#....#.....#  #  #   ')
            win.cursor = (5,8)
            win.write('   #.###.# ####...##   #  #   ')
            win.cursor = (5,9)
            win.write('   #.# #.# ...#.#..##     #   ')
            win.cursor = (5,10)
            win.write('   ### ### ### ## #.#######   ')
            win.cursor = (5,11)
            win.write('             QUEST         ')
            box = pygcurse.PygcurseTextbox(win, (0,22,40,3), fgcolor='blue', bgcolor='white', border='basic',wrap=True,margin=0,caption='')
            box.text = 'F1 = New Game | F2 = Load Game'

            while inMenu is True: #While loop to get key presses, using inMenu.
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
                    if event.type == KEYDOWN:
                        if event.key == K_F1:
                            GameStateManager.displayMenu(6)
                        if event.key == K_F2:
                            Movement.playerMove()

                box.update()
                win.cursor = 0, win.height-3
                win.pygprint('')
                win.blittowindow()
            #This is the end of the Main screen.

        #"Pause" menu. F2 doesn't do anything because I haven't figured out how to save things yet.    
        if x == 1: #This might get removed, unless I find something I want to put here. I might put keyboard commands here, instead of on the side. 
            box = pygcurse.PygcurseTextbox(win, (0, 0, 40, 22), fgcolor='red', bgcolor='black', border='basic', wrap=True, margin=3, caption='Paused')
            box.text = 'Press F1 to go back to the game.'
            box2 = pygcurse.PygcurseTextbox(win, (0,22,40,3), fgcolor='blue', bgcolor='white', border='basic',wrap=True,margin=0,caption='Commands')
            box2.text = 'F1 = Back to Game | F2 = Save Game'
            while inMenu is True:
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
                    if event.type == KEYDOWN:
                        if event.key == K_F1:
                            Movement.playerMove()
                            
                win.setscreencolors('white', 'blue', clear=True)
                box.update()
                box2.update()
                win.cursor = 0, win.height-3
                win.pygprint('')
                win.blittowindow()
            #This is the end of the "Pause Menu"

        #Jumps straight to option 6, if the Player hits F1 on the main 'splash' screen, it will take them here to create/fill variables.
        #getRandomName() is a method to generate a random int and pick a name from a list. Same as your wordlist in your hangman tutorial.
        if x == 6:
            win.setscreencolors('white', 'blue', clear=True)
            win.cursor = (14,1)
            win.write('New Character')
            win.cursor = (14,5)
            win.write('Pick a name') 
            win.cursor = (14,7)
            nameChoice1 = Player.getRandomName(Player.nameOptions)
            win.write('1. ' + nameChoice1)
            win.cursor = (14,9)
            nameChoice2 = Player.getRandomName(Player.nameOptions)
            win.write('2. ' + nameChoice2)
            win.cursor = (14,11)
            nameChoice3 = Player.getRandomName(Player.nameOptions)
            win.write('3. ' + nameChoice3)
            box = pygcurse.PygcurseTextbox(win, (0,22,40,3), fgcolor='white', bgcolor='blue', border='basic',wrap=True,margin=0,caption='')
            box.text = 'Type 1,2,or 3 | F2 = Back'
            while inMenu is True:
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
                    if event.type == KEYDOWN: #Set the player's name, which isn't used anywhere (yet).
                        if event.key == K_1:
                            Player.name = nameChoice1
                            GameStateManager.displayMenu(7)
                        if event.key == K_2:
                            Player.name = nameChoice2
                            GameStateManager.displayMenu(7)
                        if event.key == K_3:
                            Player.name = nameChoice3
                            GameStateManager.displayMenu(7)
                        if event.key == K_F2:
                            GameStateManager.displayMenu(0)
                box.update()
                win.cursor = 0, win.height-3
                win.blittowindow()

        if x == 7: #After a name is chosen, pick a class from a list. 
            classChosen = 0
            win.setscreencolors('white', 'blue', clear=True)
            win.cursor = (14,1)
            win.write('New Character')
            win.cursor = (14,5)
            win.write('Pick a name')
            win.cursor = (14,7)
            win.write('1. Warrior')
            win.cursor = (14,9)
            win.write('2. Hunter')
            win.cursor = (14,11)
            win.write('3. Mage')
            box = pygcurse.PygcurseTextbox(win, (0,22,40,3), fgcolor='white', bgcolor='blue', border='basic',wrap=True,margin=0,caption='')
            box.text = 'Type 1,2,or 3 | F2 = Back'
            while classChosen == 0:
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
                    if event.type == KEYDOWN:
                        if event.key == K_1:
                            Player.setClass(0)
                            GameStateManager.displayMenu(8)
                        if event.key == K_2:
                            Player.setClass(1)
                            GameStateManager.displayMenu(8)
                        if event.key == K_3:
                            Player.setClass(2)
                            GameStateManager.displayMenu(8)
                                                        
                        if event.key == K_F2:
                            GameStateManager.displayMenu(6)
                box.update()
                win.cursor = 0, win.height-3
                win.pygprint('')
                win.blittowindow()

        if x == 8: #This is just to tell the player what they chose, and to confirm they want to stick with those choices. 
            classChosen = 0
            win.setscreencolors('white', 'blue', clear=True)
            win.cursor = (14,1)
            win.write('New Character')
            qDialogue = 'So you\'re ' + Player.name + ' and you\'re a ' + Player.classChosen + '?'
            win.cursor = (1,7)
            win.write(qDialogue)
            box = pygcurse.PygcurseTextbox(win, (0,22,40,3), fgcolor='white', bgcolor='blue', border='basic',wrap=True,margin=0,caption='')
            box.text = 'F1 = Yes! | F2 = No!'
            while classChosen == 0:
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
                    if event.type == KEYDOWN:                            
                        if event.key == K_F1:
                            Movement.playerMove()
                        if event.key == K_F2:
                            GameStateManager.displayMenu(7)

                box.update()
                win.cursor = 0, win.height-3
                win.pygprint('')
                win.blittowindow()

        

class Player:
    mapID = 4
    #the default map ID is ALWAYS 4 because that's the center of the map array. 
    zoneID = 4
    xpos = 0
    ypos = 0
    
    name = ''
    #Name list. Just a string with .split() at the end.
    nameOptions = 'Addy Aleksandru Aloys Amé Amis Athanasi Blazh Bogdan Bogumil Bogumir Boguslav Boleslav Borislav Borisu Bozhidar Bronislav Chestibor Chestirad Chestislav Col Dalibor Daw Dicun Didacus Dmitrei Dobromil Dobroslav Dragomir Dragoslav Dragutin Drazhan Elis Elric Enguerrand Ermo Estienne Eudes Geoffroi Georgei Gidie Gostislav Grigorii Guarin Guiscard Hamo Hamon Hankin Hann Herry Hob Hopkin Hudde Jackin Jan Jankin Jehan Joscelin Josse Judd Jurian Kazimir Kresimir Kyrilu Larkin Law Lorencio Lyubomir Lyudmil Mack Milivoj Milosh Miloslav Miroslav Mstislav Nikola Noll Ode Onfroi Pate Petruccio Piers Premisl PridbjøRn Pritbor Radomil Radomir Radoslav Radovan Randel Rostislav Roul Samo Sans Slavomir Stace Stanimir Stanislav Sture Svetopolk TemüJin TemüR Tenney Tielo Tomislav Vasilii Veceslav Vecheslavu Velasco Velimir Venceslaus Vlad Vladimeru Vladimir Vladislav Vlastimir Vlastislav Voitsekh Volodimeru Volodislavu Vratislav Vsevolod Wilkin Wilky Wilmot Wybert Wymond Wyot Ximeno Yaromir Yaropolk Yaroslav Yrian Zbignev Zdislav Zuan'.split()
    #Generate a random name, similar to your tutorial, if not the exact same.
    def getRandomName(self,nameList):
        nameIndex = random.randint(0, len(nameList) - 1)
        return nameList[nameIndex]
    
    #Profession Variables, used later.
    global hasProf
    hasProf = False
    global hasSpecialProf
    hasSpecialProf = False
    global isMixedProf
    isMixedProf = False

    #Warrior, Hunter, Mage
    prof = ['Warr','Hunt','Mage']

    #These aren't used (yet).
    global special_prof
    special_prof = ['Fighter','Rogue','Sorcerer']
    global mixed_prof
    mixed_prof = ['Bandit','Paladin','Bard']
    
    classChosen = ''

    #Set the classChosen variable to what the user wanted. 
    @staticmethod
    def setClass(x):
        if x == 0:
            Player.classChosen = Player.prof[x]
        if x == 1:
            Player.classChosen = Player.prof[x]
        if x == 2:
            Player.classChosen = Player.prof[x]
    
    #Core Stats, 'must haves' in my opinion.
    level = 1
    max_health = 100
    health = 100
    max_mana = 100
    mana = 100

    max_exp = 100 #needs to be a changing variable based off level
    exp = 0
    
    #Char stats (all 0 until a class is chosen). Will be used later. 
    global strength
    strength = 0
    global agility
    agility = 0
    global wisdom
    wisdom = 0
    global armor
    armor = 0

    #Skill list, will probably change later, not currently in use. 
    global skills
    skills = []

    #None of these are in use right now. 
    def takeDmg(self, dmgTaken):
        if dmgTaken > health:
            gameOver()
        else:
            health = health - dmgTaken
            print(health + '/' + max_health)

    def useMana(self, manaUsed):
        if manaUsed > mana:
            print('You can\'t use that!')
        else:
            mana = mana - manaUsed
            print(mana + '/' + max_mana)

    def learnSkill(self, skillLearned):
        self.skills.append(skillLearned)


class Movement:
    mapIsSet = 0

    # Map 1 : Coastal Plains
    map1zone0 = ['^^^^^^^^^................~~~~~','^0^^^^^................~~~~~~~','^^^^^^...............~~~~~~~~~','^^^..................~~~~~~~~~','^^^^^...###.........~~~~~~~~~~','^^^^....###........~~~~~~~~~~~','^^.......X..........~~~~~~~~~~','^.................~~~~~~~~~~~~','..................~~~~~~~~~~~~','.................~~~~~~~~~~~~~','................~~~~~~~~~~~~~~','..............~~~~~~~~~~~~~~~~','............~~~~~~~~~~~~~~~~~~','..........~~~~~~~~~~~~~~~~~~~~','........~~~~~~~~~~~~~~~~~~~~~~','......~~~~~~~~~~~~~~~~~~~~~~~~','...~~~~~~~~~~~~~~~~~~~~~~~~~~~','.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']
    map1zone1 = ['^^^^^^^^^................~~~~~','^1^^^^^................~~~~~~~','^^^^^^...............~~~~~~~~~','^^^..................~~~~~~~~~','^^^^^...###.........~~~~~~~~~~','^^^^....###........~~~~~~~~~~~','^^.......X..........~~~~~~~~~~','^.................~~~~~~~~~~~~','..................~~~~~~~~~~~~','.................~~~~~~~~~~~~~','................~~~~~~~~~~~~~~','..............~~~~~~~~~~~~~~~~','............~~~~~~~~~~~~~~~~~~','..........~~~~~~~~~~~~~~~~~~~~','........~~~~~~~~~~~~~~~~~~~~~~','......~~~~~~~~~~~~~~~~~~~~~~~~','...~~~~~~~~~~~~~~~~~~~~~~~~~~~','.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']
    map1zone2 = ['^^^^^^^^^................~~~~~','^2^^^^^................~~~~~~~','^^^^^^...............~~~~~~~~~','^^^..................~~~~~~~~~','^^^^^...###.........~~~~~~~~~~','^^^^....###........~~~~~~~~~~~','^^.......X..........~~~~~~~~~~','^.................~~~~~~~~~~~~','..................~~~~~~~~~~~~','.................~~~~~~~~~~~~~','................~~~~~~~~~~~~~~','..............~~~~~~~~~~~~~~~~','............~~~~~~~~~~~~~~~~~~','..........~~~~~~~~~~~~~~~~~~~~','........~~~~~~~~~~~~~~~~~~~~~~','......~~~~~~~~~~~~~~~~~~~~~~~~','...~~~~~~~~~~~~~~~~~~~~~~~~~~~','.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']
    map1zone3 = ['^^^^^^^^^................~~~~~','^3^^^^^................~~~~~~~','^^^^^^...............~~~~~~~~~','^^^..................~~~~~~~~~','^^^^^...###.........~~~~~~~~~~','^^^^....###........~~~~~~~~~~~','^^.......X..........~~~~~~~~~~','^.................~~~~~~~~~~~~','..................~~~~~~~~~~~~','.................~~~~~~~~~~~~~','................~~~~~~~~~~~~~~','..............~~~~~~~~~~~~~~~~','............~~~~~~~~~~~~~~~~~~','..........~~~~~~~~~~~~~~~~~~~~','........~~~~~~~~~~~~~~~~~~~~~~','......~~~~~~~~~~~~~~~~~~~~~~~~','...~~~~~~~~~~~~~~~~~~~~~~~~~~~','.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']
    map1zone4 = ['^^^^^^^^^................~~~~~','^4^^^^^................~~~~~~~','^^^^^^...............~~~~~~~~~','^^^..................~~~~~~~~~','^^^^^...###.........~~~~~~~~~~','^^^^....###........~~~~~~~~~~~','^^.......X..........~~~~~~~~~~','^.................~~~~~~~~~~~~','..................~~~~~~~~~~~~','.................~~~~~~~~~~~~~','................~~~~~~~~~~~~~~','..............~~~~~~~~~~~~~~~~','............~~~~~~~~~~~~~~~~~~','..........~~~~~~~~~~~~~~~~~~~~','........~~~~~~~~~~~~~~~~~~~~~~','......~~~~~~~~~~~~~~~~~~~~~~~~','...~~~~~~~~~~~~~~~~~~~~~~~~~~~','.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']
    map1zone5 = ['^^^^^^^^^................~~~~~','^5^^^^^................~~~~~~~','^^^^^^...............~~~~~~~~~','^^^..................~~~~~~~~~','^^^^^...###.........~~~~~~~~~~','^^^^....###........~~~~~~~~~~~','^^.......X..........~~~~~~~~~~','^.................~~~~~~~~~~~~','..................~~~~~~~~~~~~','.................~~~~~~~~~~~~~','................~~~~~~~~~~~~~~','..............~~~~~~~~~~~~~~~~','............~~~~~~~~~~~~~~~~~~','..........~~~~~~~~~~~~~~~~~~~~','........~~~~~~~~~~~~~~~~~~~~~~','......~~~~~~~~~~~~~~~~~~~~~~~~','...~~~~~~~~~~~~~~~~~~~~~~~~~~~','.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']
    map1zone6 = ['^^^^^^^^^................~~~~~','^6^^^^^................~~~~~~~','^^^^^^...............~~~~~~~~~','^^^..................~~~~~~~~~','^^^^^...###.........~~~~~~~~~~','^^^^....###........~~~~~~~~~~~','^^.......X..........~~~~~~~~~~','^.................~~~~~~~~~~~~','..................~~~~~~~~~~~~','.................~~~~~~~~~~~~~','................~~~~~~~~~~~~~~','..............~~~~~~~~~~~~~~~~','............~~~~~~~~~~~~~~~~~~','..........~~~~~~~~~~~~~~~~~~~~','........~~~~~~~~~~~~~~~~~~~~~~','......~~~~~~~~~~~~~~~~~~~~~~~~','...~~~~~~~~~~~~~~~~~~~~~~~~~~~','.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']
    map1zone7 = ['^^^^^^^^^................~~~~~','^7^^^^^................~~~~~~~','^^^^^^...............~~~~~~~~~','^^^..................~~~~~~~~~','^^^^^...###.........~~~~~~~~~~','^^^^....###........~~~~~~~~~~~','^^.......X..........~~~~~~~~~~','^.................~~~~~~~~~~~~','..................~~~~~~~~~~~~','.................~~~~~~~~~~~~~','................~~~~~~~~~~~~~~','..............~~~~~~~~~~~~~~~~','............~~~~~~~~~~~~~~~~~~','..........~~~~~~~~~~~~~~~~~~~~','........~~~~~~~~~~~~~~~~~~~~~~','......~~~~~~~~~~~~~~~~~~~~~~~~','...~~~~~~~~~~~~~~~~~~~~~~~~~~~','.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']
    map1zone8 = ['^^^^^^^^^................~~~~~','^8^^^^^................~~~~~~~','^^^^^^...............~~~~~~~~~','^^^..................~~~~~~~~~','^^^^^...###.........~~~~~~~~~~','^^^^....###........~~~~~~~~~~~','^^.......X..........~~~~~~~~~~','^.................~~~~~~~~~~~~','..................~~~~~~~~~~~~','.................~~~~~~~~~~~~~','................~~~~~~~~~~~~~~','..............~~~~~~~~~~~~~~~~','............~~~~~~~~~~~~~~~~~~','..........~~~~~~~~~~~~~~~~~~~~','........~~~~~~~~~~~~~~~~~~~~~~','......~~~~~~~~~~~~~~~~~~~~~~~~','...~~~~~~~~~~~~~~~~~~~~~~~~~~~','.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~','~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~']
    coastalZone = [map1zone0,map1zone1,map1zone2,map1zone3,map1zone4,map1zone5,map1zone6,map1zone7,map1zone8]
    
    
    def colorMap(x,y):
        for i in range(0,len(x[y])):
            win.cursor = (0,i)
            if any("^" in s for s in x[y][i]) and any("." in s for s in x[y][i]) and any("~" in s for s in x[y][i]):
                for i in range(0,len(x[y][i].count('^'))):
                    win.write("^", fgcolor='olive')
                for i in range(0,len(x[y][i].count('.'))):
                    win.write(".", fgcolor = 'lime')
                for i in range(0,len(x[y][i].count('~'))):
                    win.write("~", fgcolor = 'blue')

    def printZone(x,y):
        for i in range(0,len(x[y])):
            win.cursor = (0,i)
            win.write(x[y][i])

    
    def isOnMap(x,y):
        return x >= 0 and y >= 0 and x < 29 and y < 21

                
    def playerMove():
        
        moveLeft = moveRight = moveUp = moveDown = False
        lastmovetime = sys.maxsize

        mainClock = pygame.time.Clock()
        checkMenu(0)
        box = pygcurse.PygcurseTextbox(win, (0,22,40,3), fgcolor='white', bgcolor='black', border='basic',wrap=True,margin=0,caption='')        
        statusBox = pygcurse.PygcurseTextbox(win, (30,0,10,23), fgcolor='white', bgcolor='black', border='basic',wrap=True,margin=0,caption='Status')
        while inMenu is False:
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_F1:
                        GameStateManager.displayMenu(1)
                    elif event.key == K_F2:
                        GameStateManager.displayMenu(2)
                    elif event.key == K_F3:
                        GameStateManager.displayMenu(3)
                    elif event.key == K_w:
                        moveUp = True
                        moveDown = False
                    elif event.key == K_s:
                        moveUp = False
                        moveDown = True
                    elif event.key == K_a:
                        moveLeft = True
                        moveRight = False
                    elif event.key == K_d:
                        moveLeft = False
                        moveRight = True
                    lastmovetime = time.time() - 1

                elif event.type == KEYUP:
                    if event.key == K_w:
                        moveUp = False
                    elif event.key == K_s:
                        moveDown = False
                    elif event.key == K_a:
                        moveLeft = False
                    elif event.key == K_d:
                        moveRight = False

            moveSpeed = 0.01 #In hundreds (milliseconds)
            if time.time() - 0.05 > lastmovetime:
                if moveUp is True:
                    if Player.ypos < 1:
                        #if map id = 0,1, or 2 the player can't move up and no zones are redrawn.
                        if Player.mapID == 0:
                            Player.ypos = 0
                        elif Player.mapID == 1:
                            Player.ypos = 0
                        elif Player.mapID == 2:
                            Player.ypos = 0

                        #if map id = 3,4,or5 allow movement up and redraw the zone accordingly.
                        elif Player.mapID == 3:
                            Player.ypos = 21
                            Player.mapID = 0
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 4:
                            Player.ypos = 21
                            Player.mapID = 1
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 5:
                            Player.ypos = 21
                            Player.mapID = 2
                            #Movement.printZone(Movement.coastalZone,Player.mapID)

                        #rows 6,7, and 8. same as above.
                        elif Player.mapID == 6:
                            Player.ypos = 21
                            Player.mapID = 3
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 7:
                            Player.ypos = 21
                            Player.mapID = 4
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 8:
                            Player.ypos = 21
                            Player.mapID = 5
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                    else:
                        Player.ypos -= 1

                elif moveDown is True:
                    time.sleep(moveSpeed)
                    if Player.ypos > 20:
                        if Player.mapID == 0:
                            Player.ypos = 0
                            Player.mapID = 3
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 1:
                            Player.ypos = 0
                            Player.mapID = 4
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 2:
                            Player.ypos = 0
                            Player.mapID = 5
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 3:
                            Player.ypos = 0
                            Player.mapID = 6
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 4:
                            Player.ypos = 0
                            Player.mapID = 7
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 5:
                            Player.ypos = 0
                            Player.mapID = 8
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif mapID == 6:
                            Player.ypos = 20
                        elif Player.mapID == 7:
                            Player.ypos = 20
                        elif Player.mapID == 8:
                            Player.ypos = 20
                    else:
                        Player.ypos += 1
                            
                elif moveLeft is True:
                    time.sleep(moveSpeed)
                    if Player.xpos < 1:
                        if Player.mapID == 0:
                            Player.xpos = 0
                        elif Player.mapID == 1:
                            Player.xpos = 29
                            Player.mapID = 0
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 2:
                            Player.xpos = 29
                            Player.mapID = 1
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 3:
                            Player.xpos = 0
                        elif Player.mapID == 4:
                            Player.xpos = 29
                            Player.mapID = 3
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 5:
                            Player.xpos = 29
                            Player.mapID = 4
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 6:
                            Player.xpos = 0
                        elif Player.mapID == 7:
                            Player.xpos = 29
                            Player.mapID = 6
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 8:
                            Player.xpos = 29
                            Player.mapID = 7
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                    else:
                        Player.xpos -= 1

                elif moveRight is True:
                    time.sleep(moveSpeed)
                    if Player.xpos > 29:
                        if Player.mapID == 0:
                            Player.xpos = 0
                            Player.mapID = 1
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 1:
                            Player.xpos = 0
                            Player.mapID = 2
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 2:
                            Player.xpos = 29
                        elif Player.mapID == 3:
                            Player.xpos = 0
                            Player.mapID = 4
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 4:
                            Player.xpos = 0
                            Player.mapID = 5
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 5:
                            Player.xpos = 29
                        elif Player.mapID == 6:
                            Player.xpos = 0
                            Player.mapID = 7
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 7:
                            Player.xpos = 0
                            Player.mapID = 8
                            #Movement.printZone(Movement.coastalZone,Player.mapID)
                        elif Player.mapID == 8:
                            Player.xpos = 29
                    else:
                        Player.xpos += 1

                
               
                        
            win.setscreencolors('white', 'black', clear=True)
            Movement.printZone(Movement.coastalZone,Player.mapID)
            box.update()
            statusBox.update()  
            win.putchar('@',Player.xpos,Player.ypos,(255,255,255))
            statusBox.text = '''Class:
%s
--------
Level:  
%s
--------
Zone:
Need to
put zone
info
here.
--------
Pos:    
(%s,%s)
--------''' % (Player.classChosen,str(Player.level),str(Player.xpos),str(Player.ypos))
            box.text = 'HP:'+str(Player.health)+'/'+str(Player.max_health)+' | MP:'+str(Player.mana)+'/'+str(Player.max_mana)+' | Exp:' + str(Player.exp) + '/'+ str(Player.max_exp) +'*'

            win.blittowindow()
            win.update()

Player = Player()
Display = Display(pygcurse.PygcurseWindow(40, 25))
Display.setWindow()
GameStateManager().displayMenu(0)






