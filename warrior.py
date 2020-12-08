from game_character import GameCharacter
from explorer import Explorer
from medic import Medic 
from termcolor import colored, cprint
import datetime
import time
import random
import winsound

freq= 1000
dur = 2000

class Warrior(GameCharacter):

    def __init__(self, name, health, strength):

        self.popularity = 0
        
        

        super().__init__(name, health, strength)

        print(f"Your warrior '{self.name}' is ready to fight! \n")

    
    def __str__(self):
        return (f"""
Warrior Stats: \t\t {colored(f"Health  : {self.health}%","green", attrs=['bold'])} 
\n\t\t\t {colored(f"Strength: {self.strength}%","blue", attrs=['bold'])}
\n\t\t\t {colored(f"Popularity: {self.popularity}", "grey", attrs=['bold'])}
""") 


    def buy_armor(self , receiver , explorer):
        if explorer.gold < 1 :
            print(f"Your explorer team member {explorer.name} has zero gold ! \nYou can send your explorer on a quest to collect more gold.")
        else :
            print(f"The warrior {self.name} has gone to the market and bought a new shield for a price of one gold")
            explorer.gold -= 1
            receiver.shield = True
            self.popularity += 1
            self.strength -= 2

    def attack(self, opponent):
        if opponent.health <= 0:
            cprint("\nYour opponent seems dead. You can't attack them.", attrs=['underline'])

        elif self.strength < 10 or self.health < 10:
            cprint("\nYour energy seems too low or you are dead. You can't attack.", attrs=['underline'])
     
        else:
            if opponent.shield == True:
                opponent.shield = False
                print(f"the opponent {opponent.name} have shield, it repiled this attack and they lost thier shield ")

            else:            
                time.sleep(3)
                print(f"the warrior {self.name} attacked {opponent.name}")
                time.sleep(3)
                print(f"{opponent.name} is bleading out !")
                opponent.health -= 10            
                self.strength -= 10  

            if opponent.health <= 0:
                opponent.health = 0
                print(f"{opponent.name} has died")
                winsound.Beep(freq,dur)

        
        print(f"{self.name} stats are: ")
        print(self)

        print(f"{opponent.name} stats are: ")
        print(opponent)

    def share_intelligence(self, explorer):
        if self.popularity >= 3:
            explorer.foresight  += int(self.popularity / 3) 
            
        else:
            print(f"your warrior {self.name} seems a bit shy, they need more than 3 popularity points to share their inteligence. ")