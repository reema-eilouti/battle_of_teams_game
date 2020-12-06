import random
import math

class GameCharacter:

    def __init__(self, name, health, strength):
        
        # Instance attributes
        self.name = name.title()
        self.health = health
        self.strength = strength
        self.shield = False
   
        

    # def __str__(self):
    #     return f"\n** Stats for {self.name} \n\n\t - Health: {int(self.health)} \n\t - Strength: {int(self.strength)} \n\t - Magic: {int(self.magic)} \n"

    # # Getters and setters for the attributes
    # def set_name(self, name):
    #     self.name = name

    # def get_name(self):
    #     return self.name

    # def set_health(self, health):
    #     if health <=0:
    #         self.health = 0
    #     elif health > 100:
    #         self.health = 100
    #     else:
    #         self.health = health

    # def get_health(self):
    #     return self.health
    
    # def set_strength(self, strength):
    #     if strength <=0:
    #         self.strength = 0
    #     else:
    #         self.strength = strength

    # def get_strength(self):
    #     return self.strength

    # def set_magic(self, magic):
    #     if magic <=0:
    #         self.magic = 0
    #     else:
    #         self.magic = magic

    # def get_magic(self):
    #     return self.magic

    # Instance Methods
