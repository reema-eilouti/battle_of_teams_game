import random
import math
import time
from game_character import GameCharacter
from treasure_maps import maps
from termcolor import colored, cprint     

class Explorer(GameCharacter):
    
    def __init__(self, name, health, strength):

        self.gold = 0
        self.foresight  = 1
        self.sectumsempra = None

        super().__init__(name, health,strength)

        print(f"Your explorer '{self.name}' at your service.\n ")  

    def __str__(self):
        return (f"""
Explorer Stats: \t {colored(f"Health  : {self.health}%","green", attrs=['bold'])} 
\n\t\t\t {colored(f"Strength: {self.strength}%","blue", attrs=['bold'])}
\n\t\t\t {colored(f"Gold    : {self.gold}$", "yellow", attrs=['bold'])}
""") 
        
    def go_on_quest(self):

        print(f"\nExplorer '{self.name}' is on their quest right now.\n ")

        map = random.choice(maps)
        
        index = [0,1,2,3]

        row = random.choice(index)
        column = random.choice(index)  
              
        while map[row][column] != 'X':
            row = random.choice(index)
            column = random.choice(index)
        
        
        map[row][column] = 'E'
        
        for row_in_map in map:              #print the map
            print(row_in_map, '\t')

        # money_pouch = 0

        if row - 1 in index:
            if map[row - 1][column] == '$':
                self.gold += 1
                map[row - 1][column] = 'X'

        if row + 1 in index:    
            if map[row + 1][column] == '$':
                self.gold += 1
                map[row + 1][column] = 'X'

        if column + 1 in index:
            if map[row][column + 1] == '$':
                self.gold += 1
                map[row][column + 1] = 'X'

        if column - 1 in index:    
            if map[row][column - 1] == '$':
                self.gold += 1
                map[row][column - 1] = 'X'

        if (row - 1 in index) and (column + 1 in index):
            if map[row - 1][column + 1] == '$':
                self.gold += 1
                map[row - 1][column + 1] = 'X'

        if (row + 1 in index) and (column - 1 in index):    
            if map[row + 1][column - 1] == '$':
                self.gold += 1
                map[row + 1][column - 1] = 'X'

        if (row - 1 in index) and (column - 1 in index):
            if map[row - 1][column - 1] == '$':
                self.gold += 1
                map[row - 1][column - 1] = 'X'

        if (row + 1 in index) and (column + 1 in index):    
            if map[row + 1][column + 1] == '$':
                self.gold += 1
                map[row + 1][column + 1] = 'X'
        # foresight == 2

        if self.foresight >= 2:
            if row - 2 in index:
                if map[row - 2][column] == '$':
                    self.gold += 1
                    map[row - 2][column] = 'X'

            if row + 2 in index:    
                if map[row + 2][column] == '$':
                    self.gold += 1
                    map[row + 2][column] = 'X'

            if column + 2 in index:
                if map[row][column + 2] == '$':
                    self.gold += 1
                    map[row][column + 2] = 'X'

            if column - 2 in index:    
                if map[row][column - 2] == '$':
                    self.gold += 1
                    map[row][column - 2] = 'X'

            if (row - 2 in index) and (column + 2 in index):
                if map[row - 2][column + 2] == '$':
                    self.gold.gold += 1
                    map[row - 2][column + 2] = 'X'

            if (row + 2 in index) and (column - 2 in index):    
                if map[row + 2][column - 2] == '$':
                    self.gold += 1
                    map[row + 2][column - 2] = 'X'

            if (row - 2 in index) and (column - 2 in index):
                if map[row - 2][column - 2] == '$':
                    self.gold += 1
                    map[row - 2][column - 2] = 'X'

            if (row + 2 in index) and (column + 2 in index):    
                if map[row + 2][column + 2] == '$':
                    self.gold += 1
                    map[row + 2][column + 2] = 'X'
            
        
        if self.foresight == 3:
            if row - 3 in index:
                if map[row - 3][column] == '$':
                    self.gold += 1
                    map[row - 3][column] = 'X'

            if row + 3 in index:    
                if map[row + 3][column] == '$':
                    self.gold += 1
                    map[row + 3][column] = 'X'

            if column + 3 in index:
                if map[row][column + 3] == '$':
                    self.gold += 1
                    map[row][column + 3] = 'X'

            if column - 3 in index:    
                if map[row][column - 3] == '$':
                    self.gold += 1
                    map[row][column - 3] = 'X'

            if (row - 3 in index) and (column + 3 in index):
                if map[row - 3][column + 3] == '$':
                    self.gold += 1
                    map[row - 3][column + 3] = 'X'

            if (row + 3 in index) and (column - 3 in index):    
                if map[row + 3][column - 3] == '$':
                    self.gold += 1
                    map[row + 3][column - 3] = 'X'

            if (row - 3 in index) and (column - 3 in index):
                if map[row - 3][column - 3] == '$':
                    self.gold += 1
                    map[row - 3][column - 3] = 'X'

            if (row + 3 in index) and (column + 3 in index):    
                if map[row + 3][column + 3] == '$':
                    self.gold += 1
                    map[row + 3][column + 3] = 'X'
   
        map[row][column] = 'X'       #return the 'E' to 'X'      
        
        time.sleep(3)

        print(f"\nExplorer '{self.name}' has found {self.gold} golden coins in his quest.\n ")
        self.strength -= self.gold * 2 
        print(f"Your explorer had a long quest, their strength decreased {self.strength}! ")          

        print(self)
    
    def forbidden_library(self):
        if self.strength > 10:
            print(f"The explorer {self.name} has entered the forbidden library !\n")
            time.sleep(3) 
            print(f"'{self.name}' is enternig the vault of fear, one of the five cursed vaults !\n") 
            time.sleep(3) 
            print("They are searching for 'Secrets of The Darkest Arts' book.\n")
            time.sleep(7) 
            print("They acquired one of the unforgivable spells... and the spell is.. \n")
            time.sleep(2) 
            cprint("SECTUMSEMPRA.\n", 'red', attrs=['reverse'])

            found_time = random.randint(10,50) 
            
            self.sectumsempra = True   #flag for the spell, for the midic to use
                                        
            self.strength = self.strength - found_time

            if self.strength < 0:
                self.health = 0
                print(f"You explorer {self.name} lost all of his strength in this quest. They cannot go back.")
                time.sleep(5)
                print(f"{self.name} died in the vault and their body will forever be forgotten in the darkness...")      
        else:
            print("Your strength is not enough to enter the forbidden library.")                   