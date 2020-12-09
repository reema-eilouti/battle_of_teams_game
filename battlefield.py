import random
import math
from medic import Medic
from explorer import Explorer
from warrior import Warrior
from game_character import GameCharacter
from termcolor import colored, cprint
import datetime
import time
import random
from progress.bar import FillingCirclesBar

# The variable responsible for ending the game loop
game_loop = True

# Creating instances for team_a characters from user
team_a_warrior_name = input("Team A, enter your warrior name : ") 
a_warrior = Warrior(team_a_warrior_name , 100 , 100)

team_a_medic_name = input("Team A, enter your medic name : ")
a_medic = Medic(team_a_medic_name , 100 , 100 ) 

team_a_explorer_name = input("Team A, enter your explorer name : ")
a_explorer = Explorer(team_a_explorer_name , 100 , 100)

# List of team_a object to be used when the player chooses the function attribute
list_team_a = [a_warrior , a_medic , a_explorer]


# Creating instances for team_a characters from player
team_b_warrior_name = input("\nTeam B, enter your warrior name: ") 
b_warrior = Warrior(team_b_warrior_name , 100 , 100)

team_b_medic_name = input("Team B, enter your medic name: ")
b_medic = Medic(team_b_medic_name , 100 , 100 )

team_b_explorer_name = input("Team B, enter your explorer name: ")
b_explorer = Explorer(team_b_explorer_name , 100 , 100)

# List of team_a object to be used when the player chooses the function attribute
list_team_b = [b_warrior , b_medic , b_explorer]

# Lists to be shown for the players
characters = [' (0) Warrior ',' (1) Medic ',' (2) Explorer ']
warrior_choices = [' (0) Buy Armor' , ' (1) Attack' , ' (2) Share Intelligence ']
medic_choices = [' (0) Heal ' ,' (1) Cast Spell ', ' (2) Back To The Future ' ]
explorer_choices = [' (0) Go On Quest ' , ' (1) Forbidden Library ']

# List that randomly chooses the first team turn
team_turns = ['a', 'b']
team_turn = random.choice(team_turns)


while(game_loop):
    
    # Print out the stats both of teams from line (57 to 144)
    cprint("\nTeam A has : ","red",attrs=['bold'])

    # Print out the stats of team_a warrior in an filling bar representation
    print(f" - {a_warrior.name}")
    a_warrior_h = FillingCirclesBar('Health  ', max=100)
    for i in range(int(a_warrior.health)):
        a_warrior_h.next()
        time.sleep(0.009)
    a_warrior_h.finish()

    a_warrior_s = FillingCirclesBar('Strength', max=100)
    for i in range(int(a_warrior.strength)):
        a_warrior_s.next()
        time.sleep(0.009)
    a_warrior_s.finish()

    # Print out the stats of team_a medic in an filling bar representation
    print(f" - {a_medic.name}")
    a_medic_h = FillingCirclesBar('Health  ', max=100)
    for i in range(int(a_medic.health)):
        a_medic_h.next()
        time.sleep(0.009)
    a_medic_h.finish()

    a_medic_s = FillingCirclesBar('Strength', max=100)
    for i in range(int(a_medic.strength)):
        a_medic_s.next()
        time.sleep(0.009)
    a_medic_h.finish()

    # Print out the stats of team_a explorer in an filling bar representation
    print(f" - {a_explorer.name}")
    a_explorer_h = FillingCirclesBar('Health  ', max=100)
    for i in range(int(a_explorer.health)):
        a_explorer_h.next()
        time.sleep(0.009)
    a_explorer_h.finish()

    a_explorer_s = FillingCirclesBar('Strength', max=100)
    for i in range(int(a_explorer.strength)):
        a_explorer_s.next()
        time.sleep(0.009)
        
    a_explorer_h.finish()

    cprint("\nTeam B has :","blue",attrs=['bold'])

    # Print out the stats of team_b warrior in an filling bar representation
    print(f" - {b_warrior.name}")
    b_warrior_h = FillingCirclesBar('Health  ', max=100)
    for i in range(int(b_warrior.health)):
        b_warrior_h.next()
        time.sleep(0.009)
    b_warrior_h.finish()

    b_warrior_s = FillingCirclesBar('Strength', max=100)
    for i in range(int(b_warrior.strength)):
        b_warrior_s.next()
        time.sleep(0.009)
    b_warrior_s.finish()

    # Print out the stats of team_b medic in an filling bar representation
    print(f" - {b_medic.name}")
    b_medic_h = FillingCirclesBar('Health  ', max=100)
    for i in range(int(b_medic.health)):
        b_medic_h.next()
        time.sleep(0.009)
    b_medic_h.finish()

    b_medic_s = FillingCirclesBar('Strength', max=100)
    for i in range(int(b_medic.strength)):
        b_medic_s.next()
        time.sleep(0.009)
    b_medic_h.finish()

    # Print out the stats of team_b explorer in an filling bar representation
    print(f" - {b_explorer.name}")
    b_explorer_h = FillingCirclesBar('Health  ', max=100)
    for i in range(int(b_explorer.health)):
        b_explorer_h.next()
        time.sleep(0.009)
    b_explorer_h.finish()

    b_explorer_s = FillingCirclesBar('Strength', max=100)
    for i in range(int(b_explorer.strength)):
        b_explorer_s.next()
        time.sleep(0.009)
    b_explorer_h.finish()

    # Print the team turn from the first random round from team_turns list
    if team_turn == 'a':
        cprint("\nTeam A Turn!\n", attrs=['bold'])

    elif team_turn == 'b':
        cprint("\nTeam B Turn!\n", attrs=['bold'])
    
    #[' (0) Warrior ',' (1) Medic ',' (2) Explorer ']
    print(characters)

    # Let the player choose which character they wants to play
    character = int(input("Choose your characters: (0) / (1) / (2) "))


    if character == 0 : # warrior
        print("\n")

        # [' (0) Buy Armor' , ' (1) Attack' , ' (2) Share Intelligence ']
        print(warrior_choices)

        action = int(input("Choose your Action :"))
        print("\n")

        if action == 0 : #buy_armor

            #[' (0) Warrior ',' (1) Medic ',' (2) Explorer ']
            print(characters)

            # Let the player choose which teammate they wants to give the shield 
            receiver_choics = int(input("Choose a teammate: "))

            if team_turn == 'a':
                a_warrior.buy_armor(list_team_a[receiver_choics], a_explorer)

                # Switch turns 
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_warrior.buy_armor(list_team_b[receiver_choics], b_explorer)
                
                # Switch turns 
                team_turn = 'a'
            


        elif action == 1 : # attack
            print(characters)
            opponent_choics = int(input("Choose an opponent : "))

            if team_turn == 'a':
                a_warrior.attack(list_team_b[opponent_choics])
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_warrior.attack(list_team_a[opponent_choics])
                team_turn = 'a'
                


        elif action == 2 : # share intelligence
            if team_turn == 'a':
                a_warrior.share_intelligence(a_explorer)
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_warrior.share_intelligence(b_explorer)
                team_turn = 'a'
                

    
    elif character == 1 : # medic
        
        #[' (0) Heal ' ,' (1) Cast Spell ', ' (2) Back To The Future ' ]
        print("\n")
        print(medic_choices)

        action = int(input("Choose your Action : "))
        print("\n")

        if action == 0 : # heal
            print(characters)
            character_choice = int(input("Enter a character you need to heal :"))

            if team_turn == 'a':
                a_medic.heal(list_team_a[character_choice])
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_medic.heal(list_team_b[character_choice])
                team_turn = 'a'
                

        elif action == 1 : #cast_spell_on
            print(characters)
            opponent_choics = int(input("Enter an oppenent to want cast spell : "))

            if team_turn == 'a':
                a_medic.cast_spell_on(list_team_b[opponent_choics] , a_explorer)
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_medic.cast_spell_on(list_team_a[opponent_choics] , b_explorer)
                team_turn = 'a'
                

        elif action == 2 : # back_to_the_future

            if team_turn == 'a':
                a_medic.back_to_the_future()
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_medic.back_to_the_future()
                team_turn = 'a'
                


    elif character == 2 : # explorer

        #[' (0) Go On Quest ' , ' (1) Forbidden Library ']
        print("\n")
        print(explorer_choices)

        action = int(input("Choose your Action : "))

        if action == 0 : # go_on_quest
            if team_turn == 'a':
                a_explorer.go_on_quest()
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_explorer.go_on_quest()
                team_turn = 'a'
                

        elif action == 1 : # forbidden_library
            if team_turn == 'a':
                a_explorer.forbidden_library()  
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_explorer.forbidden_library()  
                team_turn = 'a'                

    # How the game ends
    if a_warrior.health <= 0 and a_medic.health <= 0:
        cprint("Team B won the game !", "green", attrs=['bold'])
        print("GAME OVER ")
        game_loop = False
        
    elif b_warrior.health <= 0 and b_medic.health <= 0:
        cprint("Team A won the game !", "green", attrs=['bold'])
        print("GAME OVER ")
        game_loop = False