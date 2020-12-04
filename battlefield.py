import random
import math
from medic import Medic
from explorer import Explorer
from warrior import Warrior
from game_character import GameCharacter



    
explorer_1 = Explorer("pathfinder", 100, 100)
# explorer_1.go_on_quest()
# print(explorer_1)
explorer_1.forbidden_library()
print(explorer_1.sectumsempra)
medic_1= Medic('bruno' , 100 ,100)
medic_1.cast_spell_on(explorer_1,explorer_1)


# warrior_1 = Warrior("wraith", 100, 100)
# warrior_1.buy_armor( warrior_1 ,explorer_1)
# warrior_1.share_intelligence(explorer_1)

# medic1=Medic('bruno' , 100 ,100 , 1)
# medic1.cast_spell_on(explorer_1)
# print(explorer_1.health)

# medic1.back_to_the_future()
