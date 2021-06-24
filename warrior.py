from game_character import GameCharacter
from explorer import Explorer
from medic import Medic 
from termcolor import colored, cprint
import datetime
import time
import random
# import winsound

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


    def buy_armor(self, receiver, explorer):
        """This function adds a shield/armor for any teammate member, in exchange for a one piece of gold 
        also, this actions reduces the strength of the warrior but increases its popularity"""

        if self.health <=0 :
            print("Your warrior is dead")

        else :    
            if explorer.gold < 1 :
                print(f"Your explorer team member {explorer.name} has zero gold ! \nYou can send your explorer on a quest to collect more gold.")
            else :
                print(f"The warrior {self.name} has gone to the market and bought a new shield for a price of one gold")
                explorer.gold -= 1

                #This common attribute if set to true then the next attack will be discarded
                receiver.shield = True

                self.popularity += 1
                self.strength -= 2


    def attack(self, opponent):
        """This function decreases the health of the opponent by a factor of [(1/5)*warrior strength] 
        also the strength of the warrior who launched the attack decreases"""
        if self.health <= 0 :
            print("Your warrior is dead") 

        else :    
            if opponent.health <= 0:
                cprint("\nYour opponent seems dead. You can't attack them.", attrs=['underline'])
                
            #testing for strength and health to be less 5 because else the attacker will lose all of their strength    
            elif self.strength < 5 or self.health < 5:
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
                    
                    #Opponent health will be reduced by dividing the strength of the warrior by 5 
                    opponent.health -= self.strength/5            
                    self.strength -= 5  
                    
                    # Limiting the lower bound of health to zero
                    if opponent.health <= 0:
                        opponent.health = 0

                
                    print(f"{opponent.name} has died")
                    
                    #This function-call makes the computer Beep to announce the death of the character
                    # frequency = 100 , duration = 2000
                    # winsound.Beep(1000, 2000)

            
            print(f"{self.name} stats are: ")
            print(self)

            print(f"{opponent.name} stats are: ")
            print(opponent)


    def share_intelligence(self, explorer):
        """This function adds 1 to the explorer's foresight for every 3 popularity points"""
        if self.health <= 0 :
            print("Your warrior is dead")

        else :    
            if self.popularity >= 3:
                
                #Increase the foresight by dividing the warrior popularity by 3
                explorer.foresight  += int(self.popularity / 3) 
                
                #Setting a limit for foresight 
                if explorer.foresight > 3:
                    explorer.foresight = 3
            
            else:
                print(f"your warrior {self.name} seems a bit shy, they need more than 3 popularity points to share their inteligence. ")