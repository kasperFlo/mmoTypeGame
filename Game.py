#implements the game data and logic.
import classes.barbarian as barb ,classes.wizzard as wiz ,os
#TODO GAME LOGIC
clear = lambda: os.system('cls')

class ocupationClass:
    def __init__(self,classType = "0",Strength = 0,Health = 0,Dexterity = 0,Intelligence = 0):
        if classType.lower() == "wizzard" or classType.lower() == "wiz":
            cc = wiz.wizzardInfo()
            self.classType = cc[0]
            self.Strength = cc[1]
            self.Health = cc[2]
            self.Dexterity = cc[3]
            self.Intelligence = cc[4]

        elif classType.lower() == "barbarian" or classType.lower() == "barb":
            cc = barb.barbarianInfo()
            self.classType = cc[0]
            self.Strength = cc[1]
            self.Health = cc[2]
            self.Dexterity = cc[3]
            self.Intelligence = cc[4]
            
    def setStrength(newStrengthValue):
        Strength = newStrengthValue
    def setHealth(newHealthValue):
        Health = newHealthValue
    def setDexterity(newDexterityValue):
        Dexterity = newDexterityValue
    def setIntelligence(newIntelligenceValue):
        Intelligence = newIntelligenceValue
   
    def getclassType(self):
        return self.classType
    def getStrength(self):
        return self.Strength
    def getHealth(self):
        return self.Health
    def getDexterity(self):
        return self.Dexterity
    def getIntelligence(self):
        return self.Intelligence



playerone = ocupationClass(input("ocupation classes are 'wizzard' 'barbarian' "))
clear()
print(f"class = {playerone.getclassType()} \nstr = {playerone.getStrength()} \nhp = {playerone.getHealth()} \ndex = {playerone.getDexterity()} \nint = {playerone.getIntelligence()}")

