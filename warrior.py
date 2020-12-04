from game_character import GameCharacter
from explorer import Explorer
from medic import Medic 
class Warrior(GameCharacter):

    def __init__(self, name, health, strength):

        self.popularity = 0
        self.shield = False
        

        super().__init__(name, health, strength)

        print(f"{self.name} is ready to fight! \n")

    
    def buy_armor(self , receiver , explorer):
        if explorer.gold < 1 :
            print(f"Your explorer team member {explorer.name} has zero gold ! \nyou can send your explorer on a quest to collect more gold")
        else :
            print(f"The warrior {self.name} has gone to the market and bought a new shield for a price of one gold")
            explorer.gold -= 1
            receiver.shield = True
            self.popularity += 1
            self.strength -= 2


    def share_intelligence(self, explorer):
        if self.popularity >= 3:
            explorer.foresight  += int(self.popularity / 3) 
            
        else:
            print(f"your warrior {self.name} seems a bit shy, they need more than 3 popularity points to share their inteligence. ")