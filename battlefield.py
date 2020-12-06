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


team_a_warrior_name = input("Enter your warrior name : ") 
team_a_medic_name = input("Enter your medic name : ")
team_a_explorer_name = input("Enter your explorer name : ")
##
team_b_warrior_name = input("\nEnter your warrior name : ") 
team_b_medic_name = input("Enter your medic name : ")
team_b_explorer_name = input("Enter your explorer name : \n")
##
a_warrior=Warrior(team_a_warrior_name , 100 , 100)
a_medic=Medic(team_a_medic_name , 100 , 100 ) 
a_explorer=Explorer(team_a_explorer_name , 100 , 100)
##
b_warrior=Warrior(team_b_warrior_name , 100 , 100)
b_medic=Medic(team_b_medic_name , 100 , 100 )
b_explorer=Explorer(team_b_explorer_name , 100 , 100)
##
warrior_actions={
    'buy_armor': Warrior.buy_armor,
    'attack': Warrior.attack,
    'share_intelligence': Warrior.share_intelligence
}
##
medic_actions={
    'heal': Medic.heal,
    'cast_spell_on': Medic.cast_spell_on,
    'back_to_the_future': Medic.back_to_the_future
}
##
explorer_actions={
    'go_on_quest': Explorer.go_on_quest,
    'forbidden_library' : Explorer.forbidden_library
}
##
characters = ['0-Warrior','1-Medic','2-Explorer']
print(characters)
character = int(input("Choose your characters[0-1-2] : "))

warrior_choices = ['0-Buy_armor' , '1-Attack' , '2-Share_intelligence']
medic_choices = ['0-Heal' ,'1-Cast_spell_on ', '2-Back_to_the_future' ]
explorer_choices = ['0-Go_on_quest' , '1-Forbidden_library']

list_team_a = [a_warrior , a_medic , a_explorer]
list_team_b = [b_warrior , b_medic , b_explorer]


##
if character == 0 :
    print(warrior_choices)
    action = input("Choose your Action : ")
    if warrior_choices == 0 :
        print(characters)
        receiver_choics = int(input("Choice the opponent : "))
        player.buy_armor(list_team_a[receiver_choics] , a_explorer)
    elif warrior_choices == 1 :
        opponent_choics = int(input("Choice the opponent : "))
        player.attack(list_team_b[opponent_choics])
    elif warrior_choices == 2 :
        player.Share_intelligence(a_explorer)



elif character == 1 :
    print(medic_choices)
    action = input("Choose your Action : ")
    if medic_choices == 0 :
        print(characters)
        character_choice = int(input("Enter a character you need to heal :"))
        player.heal(list_team_a[character_choice])
    elif medic_choices == 1 :
        print(characters)
        opponent_choics = int(input("Enter an oppenent to want cast spell : "))
        player.cast_spell_on(list_team_b[opponent_choics] , a_explorer)
    elif medic_choices == 2 :
        player.Back_to_the_future()



elif character == 2 :
    print(explorer_choices)
    action = input("Choose your Action : ")
    if explorer_choices == 0 :
        player.Go_on_quest()
    elif explorer_choices == 1 :
        player.Forbidden_library()  
##

    









# is_running = False
# while is_running:


## Testing Explorers
# explorer_1 = Explorer("pathfinder", 50, 100)
# explorer_1.go_on_quest()
# print(explorer_1)
# explorer_1.forbidden_library()
# print(explorer_1.sectumsempra)
# print(explorer_1.health)


## Testing Medics
# medic_1= Medic('Doc. Brown' , 100 ,100)
# medic_1.heal(explorer_1)
# # print(medic_1)
# medic_1.cast_spell_on(explorer_1,explorer_1)
# medic1=Medic('bruno' , 100 ,100 , 1)
# medic1.cast_spell_on(explorer_1)
# medic1.back_to_the_future()


## Testing Warriors
# warrior_1 = Warrior("wraith", 100, 100)
# warrior_1.buy_armor( medic_1, explorer_1)
# # print(warrior_1)
# warrior_1.attack(medic_1)
# print(medic_1)

# warrior_1.share_intelligence(explorer_1)
