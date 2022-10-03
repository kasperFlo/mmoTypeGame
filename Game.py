#implements the game data and logic.

#TODO GAME LOGIC

from traceback import print_tb


class ocupationClass:
    def __init__(self,classType,Strength = 0,Health = 0,Dexterity = 0,Intelligence = 0):
        if classType.lower() == "wizzard":
            self.classType = "Wizzard"
            self.Strength = -2
            self.Health = 1
            self.Dexterity = 1 
            self.Intelligence = 2

        elif classType.lower() == "barbarian":
            self.classType = "Barbarian"
            self.Strength = 2
            self.Health = 1
            self.Dexterity = 1
            self.Intelligence = -2
            
    def setStrength(newStrengthValue):
        Strength = newStrengthValue
    def setHealth(newHealthValue):
        Health = newHealthValue
    def setDexterity(newDexterityValue):
        Dexterity = newDexterityValue
    def setIntelligence(newIntelligenceValue):
        Intelligence = newIntelligenceValue
   
    def getStrength(self):
        return self.Strength
    def getHealth(self):
        return self.Health
    def getDexterity(self):
        return self.Dexterity
    def getIntelligence(self):
        return self.Intelligence


playerone = ocupationClass(input("ocupation classes are 'wizzard' 'barbarian' "))
print(f"str = {playerone.getStrength()} \nhp = {playerone.getHealth()} \ndex = {playerone.getDexterity()} \nint = {playerone.getIntelligence()}")