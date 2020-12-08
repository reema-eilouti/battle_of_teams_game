class GameCharacter:

    def __init__(self, name, health, strength):
        
        self.name = name.title()
        self.health = health
        self.strength = strength
        self.shield = False