from termcolor import colored, cprint 
from game_character import GameCharacter
import datetime
import time
import random

class Medic(GameCharacter):
    def __init__(self, name, health , strength) :

        self.nanobots = 1
        self.nanobots_accuracy_level = 1
        self.magic = 1
        
        
        super().__init__(name, health ,strength)

        print(f"Your medic '{self.name}', to the rescue!\n")

    def __str__(self):
        return (f"""
Medic Stats: \t\t {colored(f"Health  : {self.health}%","green", attrs=['bold'])} 
\n\t\t\t {colored(f"Strength: {self.strength}%","blue", attrs=['bold'])}
\n\t\t\t {colored(f"Wizardry Level: {self.magic}", "magenta", attrs=['bold'])}
\n\t\t\t {colored(f"Nanobots: {self.nanobots}", "cyan", attrs=['bold'])}
\t\t\t {colored(f"Accuracy: {self.nanobots_accuracy_level}", "cyan", attrs=['bold'])}
""") 

    def heal(self, character):
        if character.health <= 0:
            print(f"your teammate {character.name} is dead.")

        elif self.nanobots < 1:
            print("You have to get back to the future.")

        else:
            character.health += self.nanobots * self.nanobots_accuracy_level            
            print(f"> {self.name} is now healing {character.name}.")
            time.sleep(3)
            self.strength -= 5
            print("Healing was not easy, the medic strength was decreased.")
            print(self)
            print(character)

        
               
    def cast_spell_on(self, opponent, explorer):
        if self.health <= 0 or self.strength <= 0:
            cprint("\nYour energy seems too low or you are dead. You can't cast a spell.", attrs=['underline'])

        elif opponent.health <= 0:
            cprint("\nYour opponent seems dead. You can't cast a spell on them.", attrs=['underline'])

        else:

            if explorer.sectumsempra == True:                         
                print(f"'{self.name}' is going to cast the spell 'Sectumsempra' on '{opponent.name}'.\n")
                time.sleep(2)
                print(f"SECTUMSEMPRAAA!\n")

                # Reseting the flag.
                explorer.sectumsempra = False 

                opponent.health /= 2
                print(f"{opponent.name}'s health has been cut in half!\n")

                if opponent.health < 0 :

                    print(colored(f"'{opponent.name}' is dead...", 'red'))

                    self.strength = self.strength - 15
                    print(f"Wow, that was a powerful spell. Your strength is now: {self.strength}%.\n")   

                    self.magic = self.magic + 2
                    if self.magic > 8:
                        self.magic = 7
                    print(f"Your wizardry level has increased to {self.magic}%.\n")

            else:            
                print(f"'{self.name}' is going to cast a spell on '{opponent.name}'.\n")

                print("casting the spell... Petrificus Totalus/Confringo/Everte Statum!\n")

                opponent.health -= self.magic * (self.strength / 10)

                if opponent.health < 0 :
                    print(colored(f"'{opponent.name}' has died..\n", 'red'))

                print(opponent)

                self.strength -= 10
                print(f"That wasn't easy. Your strength has decreased.\n")
                
                self.magic += 1 
                if self.magic > 8:
                    self.magic = 7
                print(f"Your wizardry level has increased .\n")   

                print(self)    


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