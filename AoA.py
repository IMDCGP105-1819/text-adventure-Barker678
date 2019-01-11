import time
import random

class WEAPONS(object):
    def __init__(self):
        self.WEAPONS = {
        'Fist': (3,8),
        'stick': (4,9),
        'pulse_baton': (5,10),
        'alien_blaster': (5,12),
        }
        self.weapon = WEAPONS['Fist']

    def add_WEAPONS(self,name, weapon):
        self.WEAPONS[name] = weapon
        print ('You have picked up {} to your inventory').format(name.upper())

    def __str__(self):
        for WEAPONS in self.WEAPONS.values():
            print ('\t'.join([str(x)for x in [WEAPONS.name]]))
            if not WEAPONS.inventory:
                print ('You Have Nothing!')

class player(object):
    def __init__(self):
        self.health = {
            'health': (16)
        }

def game():

    def playagain():
        if playagain == ['y', 'Y', 'Yes', 'YES', 'yes']:
            chapter_1()
            if playagain in ['n', 'N', 'No', 'NO', 'no']:
                print("Thank you for playing, hope you enjoyed the adventure!")

    def end_game():
        print('You Suddenly wake up!')
        print('It was just a dream.')
        print('Well... thats what they')
        print('want you to think')
        playagain

    def print_alien():
        time.sleep(2)
        print("    dMMMb._              .adOOOOOOOOOba.              _,dMMMb_ ")
        print("  dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb")
        print("  V      ~MMb          dOOOOOOOOOOOOOOOOOb          dM~      V")
        print("           `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'         ")
        print("            `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'          ")
        print("       __     `YMMM| OP'~0OOOOOOOOOOO0~`YO |MMMP'     __     ")
        print("     ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb    ")
        print("  _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._")
        print(" <MMP'     `~YMMa_   YOOo   @  OOO  @   oOOP   _adMP~'      `YMM>")
        print("              `YMMMM\`OOOo     OOO     oOOO'/MMMMP'            ")
        print("      ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa    ")
        print("    ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb. ")
        print("   ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.")
        print("   MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM")
        print("   YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP")
        print("    `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM' ")
        print("      `'                  `OObNNNNNdOO'                   `'   ")
        print("                            `~OOOOO~'                          ")

    def fight_enemy(enemy_name, min_enemy_damage, max_enemy_damage, min_player_damage, max_player_damage):
        enemy_damage_dealt = random.randint(min_enemy_damage, max_enemy_damage)
        player_damage_dealt = random.randint(min_player_damage, max_player_damage)

        if enemy_damage_dealt > player_damage_dealt:
            print("Uh-oh! You got Hurt!")
        elif enemy_damage_dealt < player_damage_dealt:
            print("You killed the {enemy_name}".format(enemy_name=enemy_name))
        else:
            print("You walk away unscathed, but the {enemy_name} still lives.".format(enemy_name=enemy_name))

    def chapter_1():
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print ('Welcome to the Army of Aliens!')
        print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        time.sleep(2)
        print ('Hello human,')
        print ('....')
        time.sleep(1)
        print ('....')
        time.sleep(1)
        print ('Human')
        time.sleep(1)
        print ('...')
        time.sleep(1)  # NOTE: this is the intro
        print ('\nAnswer Me!\n')
        time.sleep(1)
        print ('....')
        time.sleep(1)
        print ('\ngrr, I will go see other humans\n')
        time.sleep(1)
        print ('....')
        time.sleep(1)
        print('''You Wake up on what looks to be a dissection table,''')
        time.sleep(1)
        print('''and from the sound and look of it, You Are On an Alien Vessel''')
        time.sleep(1)
        print("...")
        time.sleep(1)
        print ('Before you can fully take in your surroundings a slimy')
        time.sleep(1)
        print ('and disgusting alien walks in and stares at you,')
        time.sleep(1)
        print ('You feel the urge to run')
        time.sleep(1) 
        canContinue = False
        canContinue1 = False
        canContinue2 = False
        canContinue3 = False
        canContinue4 = False
        canContinue5 = False
        canContinue6 = False
        canContinue7 = False
        end = False
        
        turn = 0
        escape = 0
        shriek = 0

        while(canContinue == False):                                                                                # NOTE: in chapter 1 the player will mostly answer yes or no questions with there being different things happen throughout
            ch1 = str(input('What Would You like to Do?  ')) 
            if ch1 in ['help', 'Help', 'HELP']: 
                print('Run or Forward, to leave the room')                                                        # NOTE: this will change throughout the game; chapter 2 has more things to do as i feel like chapter 1 opens the story of where the player is and
                print('Nothing or Stay, to stay where you are')
                print('Talk, to communicate with the Alien')
                canContinue = False
            if ch1 in ['run', 'Run', 'RUN', 'forward', 'Forward', 'FORWARD']:                                                             # NOTE: what they should be doing, i will make some changes so that the player has more choices in chapter 1
                print ('You spring up from the table and run out the door, not looking back')
                time.sleep(2)
                print("...")
                time.sleep(2)
                print ('lights start to flash around the ship')
                time.sleep(1)
                print ('...')
                escape = 1
                turn = 1
                canContinue = True
            elif ch1 in ['nothing', 'Nothing','NOTHING', 'STAY' 'Stay', 'stay', 'die', 'Die', 'DIE']:
                print ('You stay laying on the table awaiting your fate')
                time.sleep(2)
                escape = 0
                turn = 1
                canContinue = True
            elif ch1 in ['talk', 'Talk', 'TALK', 'alien', 'Alien', 'ALIEN']:
                if turn == 1 and shriek == 1:
                    print("you try to talk to the alien again")
                    time.sleep(1)
                    print("it turns around and looks at you and growls before returning to its work")
                else:
                    print("You try to communicate with the Alien, as you do it turns round and shrieks")
                    time.sleep(1)
                    print("You think its best to keep quiet")
                    escape = 0
                    turn = 1
                    shriek = 1
            else:
                print("I don't understand, please try again")

        if turn == 1:
            if escape == 1:
                print ('As you run down some corridors you start to slow down')
                print("There is a room infront of you, also corridors to the left and to the right")
                while (canContinue2 == False):
                    ch2 = str(input('What would you like to do?  '))
                    if ch2 in ['help', 'Help', 'HELP']:
                        print('Forward or Room, to enter the room infront of you')
                        print('left... to go left... pretty obvious right?')
                        print('Right ... for right... this should be easy')
                        canContinue2 = False
                    if ch2 in ['forward', 'Forward', 'FORWARD', 'room', 'Room', 'ROOM']:
                        time.sleep(1)
                        print("you walk into the room and it seems to be a small armory")
                        time.sleep(1)
                        canContinue2 = True

                        while(canContinue6 == False):
                            ch56 = str(input('what would you like to do?  '))
                            if ch56 in ['help', 'Help', 'HELP']:
                                print('Inspect or Look, to search for weapons in the armory')
                                canContinue6 = False
                            if ch56 in ['gander', 'inspect', 'survey', 'look', 'LOOK', 'Look']:
                                loot1 = int(random.randint(3, 10))
                                nloot1 = int(random.randint(1, 10))
                                nloot2 = int(random.randint(2, 10))
                                if loot1 > nloot1:
                                    print ('As you look around you find a nothing')
                                    loot1 = int(random.randint(3, 10))
                                    nloot1 = int(random.randint(1, 10))
                                    ch10 = 1
                                    canContinue6 = True
                                elif loot1 < 5:
                                    print ('As you look around you find a prodding stick')
                                    weapon = ["stick"]
                                    ch10 = 1
                                    loot1 = int(random.randint(3, 10))
                                    nloot2 = int(random.randint(2, 10))
                                    canContinue6 = True
                                else:
                                    print ('You find a plasma pistol!')
                                    weapon = ["alien_blaster"]
                                    ch10 = 1
                                    canContinue6 = True
                            else:
                                print("I do not understand, give valid command")

                            if ch10 == 1:
                                print ('After looking around you notice you are at a deadend and')
                                time.sleep(2)
                                print ('you hear thuds coming from the long corridor you came from')
                                time.sleep(2)
                            while (canContinue3 == False):
                                ch5 = str(input('What would you like to do?  '))
                                if ch5 in ['help', 'Help', 'HELP']:
                                    print('Stay, to hide and avoid the unknown entity')
                                    print('Fight, to ambush the alien')
                                    print('Run, to flee past the alien')
                                    canContinue3 = False
                                if ch5 in ['stay', 'STAY', 'Stay', 'WAIT', 'Wait', 'wait']:
                                    time.sleep(2)
                                    print ('The alien walks pass the doorway')
                                    print ("You manage to sneak past and run away")
                                    escape = 2
                                    turn = 2
                                    canContinue3 = True
                                if ch5 in ['fight', 'Fight', 'FIGHT', 'ATTACK', 'attack', 'Attack']:
                                    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print ("                  Fighting...                  ")
                                    print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                    print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print_alien()
                                    fight_enemy('ALIEN', 3, 6, 1, 15)
                                    print ('The alien turns into a puddle of goo on the floor')
                                    print ('you find nothing in the goo')
                                    time.sleep(2)
                                    escape = 2
                                    turn = 2
                                    canContinue3 = True
                                    if ch5 in ['run', 'Run', 'RUN', 'flee', 'FLEE', 'Flee']:
                                        print("you run down the corridor and you see a green figure up ahead")
                                        print("as you get closer it shreiks at you")
                                        print("you jump as high as you can clearing the aliens head")  
                                        escape = 2 
                                        turn = 2
                                        canContinue3 = True
                                    else: 
                                        print('I do not understand, please give valid command')
        
                    if ch2 in ['Left', 'l', 'L', 'LEFT', 'left']:
                        print ('After travelling down the corridor you find a corpse at a deadend')
                        time.sleep(2)
                        print("it seems to of been here for months")
                        time.sleep(1)
                        print("as you start to walk the way you came")
                        print ('you hear thuds coming from the long corridor')
                        time.sleep(2)
                        canContinue2 = True
                        ch9 = str(input('What would you like to do?  '))
                        if ch9 in ['help', 'Help', 'HELP']:
                            print('Stay or Wait for the noise to get closer')
                        if ch9 in ['stay', 'STAY', 'Stay', 'WAIT', 'Wait', 'wait']:
                            print ('You wait for the thudding to get closer')
                            time.sleep(2)
                            print ('The alien walks pass the doorway')
                            ch98 = str(input('What would you like to do?  '))
                            if ch98 in ['fight', 'Fight', 'FIGHT', 'ATTACK', 'attack', 'Attack']:
                                time.sleep(2)
                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print ("                  Fighting...                  ")
                                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print_alien()
                                fight_enemy('ALIEN', 3, 6, 1, 15)
                                time.sleep(2)
                                print ('You killed the alien!')
                                end_game()
                                canContinue4 = True
                                time.sleep(2)
                            if ch98 in ['flee', 'Flee', 'FLEE', 'run', 'Run', 'RUN']:
                                print("as the alien gets close you make a break for it past the alien")
                                time.sleep(2)
                                print("you make it past the alien without it noticing!")
                                escape = 2
                                turn = 2
                                canContinue4 = True
                            else:
                                print('I do not understand, please enter valid command')

                    if ch2 in ['right', 'Right', 'RIGHT', 'r', 'R']:
                        print("you turn right")
                        time.sleep(1)
                        print("you start to walk ")
                        print('You come to a empty room and hear noise coming towards you')
                        canContinue2 = True

                        ch8 = str(input("What would you like to do? "))
                        if ch8 in ['help', 'Help', 'HELP']:
                            print('Stay or Wait for the noise to get closer')
                        if ch8 in ['stay', 'STAY', 'Stay', 'WAIT', 'Wait', 'wait']:
                            print ('You wait for the thudding to get closer')
                            time.sleep(2)
                            print ('The alien walks pass the doorway')
                            ch6 = str(input('What would you like to do?  '))
                            if ch6 in ['fight', 'Fight', 'FIGHT', 'ATTACK', 'attack', 'Attack']:
                                time.sleep(2)
                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print ("                  Fighting...                  ")
                                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print_alien()
                                fight_enemy('ALIEN', 3, 6, 1, 15)
                                time.sleep(2)
                                print ('You killed the alien!')
                                end_game()
                                canContinue4 = True
                                time.sleep(2)
                            if ch6 in ['flee', 'Flee', 'FLEE', 'run', 'Run', 'RUN']:
                                print("as the alien gets close you make a break for it past the alien")
                                time.sleep(2)
                                print("you make it past the alien without it noticing!")
                                escape = 2
                                turn = 2
                                canContinue4 = True
                        else:
                            print('I do not understand, please enter valid command')

            if turn == 2:  
                if escape == 2:
                    print("You hear drills coming from a room closeby")
                    while(canContinue5 == False):
                        ch19 = str(input('What would you like to do?  '))
                        if ch19 in ['help', 'Help', 'HELP']:
                            print('Stay, to wait')
                            print('Look or Investigate.. to look in the room')
                            canContinue5 = False
                        if ch19 in ['stay', 'STAY', 'Stay', 'WAIT', 'Wait', 'wait']:
                            print ('The drilling gets louder')
                            print ('An alien walks pass the doorway')
                            canContinue5 = True
                            while(canContinue7 == False):
                                ch20 = str(input('What would you like to do?  '))
                                if ch20 in ['help', 'Help', 'HELP']:
                                    print('Fight, to attack the alien')
                                    print('Run to try and flee the Alien')
                                    canContinue7 = False
                                if ch20 in ['fight', 'Fight', 'FIGHT', 'ATTACK', 'attack', 'Attack']:
                                    time.sleep(2)
                                    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print ("                  Fighting...                  ")
                                    print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                    print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print_alien()
                                    fight_enemy('ALIEN', 3, 6, 1, 15)
                                    time.sleep(2)
                                    print ('You killed the alien!')
                                    print ('You find the corpse of a woman with drills in the side of her head')
                                    print ('But you do find a Pulse Baton...ey')
                                    weapon = ["pulse_baton"]
                                    canContinue5 = True
                                    end_game()
                                    time.sleep(2)
                                else:
                                    print('I do not understand, please enter valid command')

                    while (canContinue1 == False):
                        if ch19 in ['investigate', 'Investigate', 'INVESTIGATE', 'look', 'Look', 'LOOK']:
                            print("You peer into the room next door")
                            time.sleep(2)
                            print ('An Alien stares directly at you')
                            canContinue1 = True
                            ch100 = str(input('what would you like to do?  '))
                            if ch100 in ['fight', 'Fight', 'FIGHT', 'ATTACK', 'attack', 'Attack']:
                                time.sleep(2)
                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print ("                  Fighting...                  ")
                                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print_alien()
                                fight_enemy('ALIEN', 3, 6, 1, 15)
                                time.sleep(2)
                                print ('You killed the alien!')
                                print ('You find the corpse of a woman with drills in the side of her head')
                                print ('But you do find a Pulse Baton')
                                weapon = ["pulse_baton"]
                                end_game()
                                canContinue1 == True
                            else:
                                print('I do not understand, please enter valid command')
                                if ch20 in ['Run', 'RUN', 'run', 'FLEE', 'flee', 'Flee']:
                                    print ('You choose not to fight the alien.')
                                    time.sleep(1)
                                    print ("you see the alien staring at you, you turn round and flee, the alien close behind.")
                                    time.sleep(1)
                                    print("you are able to evade the alien for now")
                                    canContinue1 == True

                                    print("you wait and hide waiting for the thudding of aliens footsteps to stop")
                                    time.sleep(2)
                                    print("they've finally stopped looking for you")
                                    end_game()
                                else:
                                    print("\nI Dont understand, please input valid command\n")

            if escape == 0:
                if turn == 1:
                    if ch1 in ['nothing', 'Nothing','NOTHING', 'STAY' 'Stay', 'stay', 'die', 'Die', 'DIE']:
                        print ('you hear what seems to be drills coming from the room next to the one your in')
                        ch3 = str(input('Would you like to do?  '))
                        if ch3 in ['investigate', 'Investigate', 'INVESTIGATE', 'look', 'Look', 'LOOK']:
                            print("You peer into the room next door")
                            time.sleep(2)
                            print ('An Alien stares directly at you')
                            ch100 = str(input('what would you like to do?  '))
                            if ch100 in ['fight', 'Fight', 'FIGHT', 'ATTACK', 'attack', 'Attack']:
                                time.sleep(2)
                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print ("                  Fighting...                  ")
                                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print_alien()
                                fight_enemy('ALIEN', 3, 6, 1, 15)
                                time.sleep(2)
                                print ('You killed the alien!')
                                time.sleep(2)
                                print ('You find the corpse of a woman with drills in the side of her head')
                                time.sleep(1)
                                print ('But you do find a Pulse Baton...')
                                weapon = ["pulse_baton"]
                                end_game()
                            else:
                                print("\nI don't understand, please try again\n")

                            if turn == 2:  
                                if escape == 2:
                                    if end == True:
                                        print ('you hear what seems to be drills coming from the room next to the one your in')
                                        ch7 = str(input('What would you like to do?  '))
                                        if ch7 in ['Look', 'LOOK', 'look', 'INVESTIGATE', 'Investigate', 'investigate']:
                                            print ('You get up slowly and peer into the room next door')
                                            time.sleep(2)
                                            print ('An Alien stares directly at you')
                                            ch4 = str(input('What would you like to do?  '))
                                            if ch4 in ['attack', 'ATTACK', 'Attack', 'FIGHT', 'Fight', 'fight']:
                                                time.sleep(2)
                                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print ("                  Fighting...                  ")
                                                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE ALIEN    ")
                                                print ("IF THE ALIEN HITS HIGHER THAN YOU, YOU WILL DIE")
                                                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                                print_alien()
                                                fight_enemy('ALIEN', 3, 6, 1, 15)
                                                time.sleep(2)
                                                print ('You killed the alien!')
                                                print ('You find the corpse of a woman with drills in the side of her head')
                                                print ('But you do find a Pulse Baton...ey')
                                                weapon = ["pulse_baton"]
                                                end_game()
                                                time.sleep(2)

                                            if ch4 in ['Run', 'RUN', 'run', 'FLEE', 'flee', 'Flee']:
                                                print ('You choose not to fight the alien.')
                                                time.sleep(1)
                                                print ("you see the alien staring at you, you turn round and flee, the alien close behind.")
                                                time.sleep(1)
                                                ch11 = str(input("you are able to evade the alien for now"))
                                                if ch11 in['stay', 'Stay', 'STAY', 'HIDE', 'hide', 'Hide']:
                                                    print("you wait and hide waiting for the thudding of aliens footsteps to stop")
                                                    time.sleep(2)
                                                    print("they've finally stopped looking for you")
                                                    end_game()
                                                        
                                            else:
                                                print("\nI Dont understand, please input valid command\n")                        

    chapter_1()

game()