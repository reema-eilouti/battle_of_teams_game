from game_character import GameCharacter
from explorer import Explorer
from medic import Medic 
from termcolor import colored, cprint

class Warrior(GameCharacter):

    def __init__(self, name, health, strength):

        self.popularity = 0
        self.shield = False
        

        super().__init__(name, health, strength)

        print(f"{self.name} is ready to fight! \n")

    
    def __str__(self):
        return (f"""
Warrior Stats: \t\t {colored(f"Health  : {self.health}%","green", attrs=['bold'])} 
\n\t\t\t {colored(f"Strength: {self.strength}%","blue", attrs=['bold'])}
\n\t\t\t {colored(f"Popularity: {self.popularity}", "grey", attrs=['bold'])}
""") 


    def buy_armor(self , receiver , explorer):
        if explorer.gold < 1 :
            print(f"Your explorer team member {explorer.name} has zero gold ! \nyou can send your explorer on a quest to collect more gold")
        else :
            print(f"The warrior {self.name} has gone to the market and bought a new shield for a price of one gold")
            explorer.gold -= 1
            receiver.shield = True
            self.popularity += 1
            self.strength -= 2

    def attack(self, opponent):
        attack_strength = int((self.health * 0.6 + self.strength * 0.4 + self.magic * 0.2)/12)

        print(f"> {self.name} is attacking {opponent.name}. {(attack_strength)}")
    
        opponent.set_health(opponent.get_health() - (attack_strength))

    def share_intelligence(self, explorer):
        if self.popularity >= 3:
            explorer.foresight  += int(self.popularity / 3) 
            
        else:
            print(f"your warrior {self.name} seems a bit shy, they need more than 3 popularity points to share their inteligence. ")