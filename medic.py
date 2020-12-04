import termcolor
from game_character import GameCharacter
import datetime
import time
import random

class Medic(GameCharacter):
    # sectumsempra = False
    def __init__(self, name, health , strength) :

        self.nanobots = 0
        self.nanobots_accuracy_level=1
        self.magic = 1
        
        super().__init__(name, health ,strength)

        print(f"Your medic {self.name}, to the rescue!")


    def heal(self, character):
        heal_value = self.nanobots * self.nanobots_accuracy_level
        print(f"> {self.name} is healing {character.name}. {(heal_value)}")

        if character.get_health() + heal_value > 100 :
            character.set_health(100)
        else:
            character.set_health(character.get_health() + heal_value)

        print(f"The medic {self.name} healed their teammate {character.name}")


    def cast_spell_on(self, opponent, explorer):
        if explorer.sectumsempra == True:                           #use the stronger spell
            print(f"> {self.name} is trying to cast a spell sectumsempra on {opponent.name}.")
            print(f"> Sectumsempra... casting the spell.")

            opponent.health /= 2
            if opponent.health < 0 :
                print(termcolor.colored(f"The character you are trying to cast spell on {opponent.name} is dead !! ':(' ", 'red'))
                self.strength = self.strength - 15                        
                self.magic = self.magic + 2

            explorer.sectumsempra == False              
        else:            
            print(f"> {self.name} is trying to cast a spell Abracadabra on {opponent.name}.")

            print(f"> Abracadabra... casting the spell.")

            opponent.health -= self.magic * (self.strength / 10)
            if opponent.health < 0 :
                print(termcolor.colored(f"The character you are trying to cast spell on {opponent.name} is dead !! ':(' ", 'red'))
            self.strength = self.strength - 10
            
            self.magic = self.magic + 1        


    def back_to_the_future(self):
        print(f"Brace yourself, the medic '{self.name}' is getting into the DeLorean.\n")
        time.sleep(3) 
        print(f"'{self.name}' is checking the flux capacitor and fixing the input on the time circuits.\n") 
        time.sleep(3) 
        print("Starting the engine and accelerating...\n")
        time.sleep(3) 
        print("88 miles/hour in 1.21 giggawatts! (one light bolt) off we go!\n") 
        # times = [range(1,11)]
        datetime = random.randint(1,11)
        time.sleep(datetime) 
        print(f"'{self.name}' has traveled forward in time by {datetime} nanoseconds!\n") 
        self.nanobots += datetime
        print(f"This means they have extra {datetime} nanobots now. To make the total: {self.nanobots} nanobots.") 
        self.nanobots_accuracy_level += 1
        print(f"Also, the accuracy level of the bots has been increased to {self.nanobots_accuracy_level}.")