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

# is_running = False
# while is_running:


## Testing Explorers
explorer_1 = Explorer("pathfinder", 50, 100)
# explorer_1.go_on_quest()
# print(explorer_1)
# explorer_1.forbidden_library()
# print(explorer_1.sectumsempra)
# print(explorer_1.health)


## Testing Medics
medic_1= Medic('Doc. Brown' , 100 ,100)
medic_1.heal(explorer_1)
# print(medic_1)
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
