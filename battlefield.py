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


game_loop = True

team_a_warrior_name = input("Team A, enter your warrior name : ") 
a_warrior = Warrior(team_a_warrior_name , 100 , 100)

team_a_medic_name = input("Team A, enter your medic name : ")
a_medic = Medic(team_a_medic_name , 100 , 100 ) 

team_a_explorer_name = input("Team A, enter your explorer name : ")
a_explorer = Explorer(team_a_explorer_name , 100 , 100)


list_team_a = [a_warrior , a_medic , a_explorer]



team_b_warrior_name = input("\nTeam B, enter your warrior name: ") 
b_warrior = Warrior(team_b_warrior_name , 100 , 100)

team_b_medic_name = input("Team B, enter your medic name: ")
b_medic = Medic(team_b_medic_name , 100 , 100 )

team_b_explorer_name = input("Team B, enter your explorer name: ")
b_explorer = Explorer(team_b_explorer_name , 100 , 100)

list_team_b = [b_warrior , b_medic , b_explorer]






characters = [' (0) Warrior ',' (1) Medic ',' (2) Explorer ']
warrior_choices = [' (0) Buy Armor' , ' (1) Attack' , ' (2) Share Intelligence ']
medic_choices = [' (0) Heal ' ,' (1) Cast Spell ', ' (2) Back To The Future ' ]
explorer_choices = [' (0) Go On Quest ' , ' (1) Forbidden Library ']


team_turns = ['a', 'b']
team_turn = random.choice(team_turns)

while(game_loop):

    cprint("\nTeam A has : ","red",attrs=['bold'])
    cprint(f"\t - {a_warrior.name}, {a_warrior.health},{a_warrior.strength}","red")
    cprint(f"\t - {a_medic.name},{a_medic.health},{a_medic.strength}","red")
    cprint(f"\t - {a_explorer.name},{a_explorer.health},{a_explorer.strength}","red")

    cprint("\nTeam B has :","blue",attrs=['bold'])
    cprint(f"\t - {b_warrior.name},{b_warrior.health},{b_warrior.strength}","blue")
    cprint(f"\t - {b_medic.name},{b_medic.health},{b_medic.strength}","blue")
    cprint(f"\t - {b_explorer.name},{b_explorer.health},{b_explorer.strength}","blue")

    if team_turn == 'a':
        cprint("\nTeam A Turn!\n", attrs=['bold'])

    elif team_turn == 'b':
        print("\nTeam B Turn!\n", attrs=['bold'])
    
    print(characters)
    character = int(input("Choose your characters: (0) / (1) / (2) "))


    if character == 0 :
        print("\n")
        print(warrior_choices)

        action = int(input("Choose your Action :"))
        print("\n")

        if action == 0 :
            print(characters)
            receiver_choics = int(input("Choose a teammate: "))

            if team_turn == 'a':
                a_warrior.buy_armor(list_team_a[receiver_choics], a_explorer)
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_warrior.buy_armor(list_team_b[receiver_choics], b_explorer)
                team_turn = 'a'
            


        elif action == 1 :
            print(characters)
            opponent_choics = int(input("Choose an opponent : "))

            if team_turn == 'a':
                a_warrior.attack(list_team_b[opponent_choics])
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_warrior.attack(list_team_a[opponent_choics])
                team_turn = 'a'
                


        elif action == 2 :
            if team_turn == 'a':
                a_warrior.share_intelligence(a_explorer)
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_warrior.share_intelligence(b_explorer)
                team_turn = 'a'
                


    elif character == 1 :

        print("\n")
        print(medic_choices)

        action = int(input("Choose your Action : "))
        print("\n")

        if action == 0 :
            print(characters)
            character_choice = int(input("Enter a character you need to heal :"))

            if team_turn == 'a':
                a_medic.heal(list_team_a[character_choice])
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_medic.heal(list_team_b[character_choice])
                team_turn = 'a'
                

        elif action == 1 :
            print(characters)
            opponent_choics = int(input("Enter an oppenent to want cast spell : "))

            if team_turn == 'a':
                a_medic.cast_spell_on(list_team_b[opponent_choics] , a_explorer)
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_medic.cast_spell_on(list_team_a[opponent_choics] , b_explorer)
                team_turn = 'a'
                

        elif action == 2 :

            if team_turn == 'a':
                a_medic.back_to_the_future()
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_medic.back_to_the_future()
                team_turn = 'a'
                


    elif character == 2 :

        print("\n")
        print(explorer_choices)

        action = int(input("Choose your Action : "))

        if action == 0 :
            if team_turn == 'a':
                a_explorer.go_on_quest()
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_explorer.go_on_quest()
                team_turn = 'a'
                

        elif action == 1 :
            if team_turn == 'a':
                a_explorer.forbidden_library()  
                team_turn = 'b'
                
            elif team_turn == 'b':
                b_explorer.forbidden_library()  
                team_turn = 'a'                

    if a_warrior.health <= 0 and a_medic.health <= 0:
        cprint("Team B won the game !", "green", attrs=['bold'])
        game_loop = False
    elif b_warrior.health <= 0 and b_medic.health <= 0:
        cprint("Team A won the game !", "green", attrs=['bold'])
        game_loop = False

