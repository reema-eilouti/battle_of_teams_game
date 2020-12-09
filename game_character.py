class GameCharacter:


    def __init__(self, name, health, strength):
        
        self.name = name.title()
        self.health = health
        self.strength = strength
   
        #Setting default value to the shield 
        self.shield = False
        #Shield : what the warrior buy when the function buy_armor is called
        #If a character have a shield the attack on then is will be discarded  