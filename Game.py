#implements the game data and logic.
#import classes.barbarian as barb
import classes.barbarian as barb,classes.wizzard as wiz,os
#clear = lambda: os.system('cls') # windows
clear = lambda: os.system('clear') # mac


def selectOcupation(selectClass):
    global ocupation
    if selectClass.lower() == "wizzard" or selectClass.lower() == "wiz":
        ocupation = wiz.wizzardInfo
    elif selectClass.lower() == "barbarian" or selectClass.lower() == "barb":
        ocupation = barb.barbarianInfo

def startGame():
    selectOcupation(input("ocupation classes are 'wizzard' 'barbarian' "))

startGame()

class ocupationClass(ocupation):
    def setStrength(self,newStrengthValue):
        self.Strength = newStrengthValue
    def setHealth(self,newHealthValue):
        self.Health = newHealthValue
    def setDexterity(self,newDexterityValue):
        self.Dexterity = newDexterityValue
    def setIntelligence(self,newIntelligenceValue):
        self.Intelligence = newIntelligenceValue
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
    
    def printStats(self):
        pad = 30
        print("Class = {}".format(self.getclassType()).center(pad))
        print("Str = {}".format(self.getStrength()).center(pad))
        print("Hp = {}".format(self.getHealth()).center(pad))
        print("Dex = {}".format(self.getDexterity()).center(pad))
        print("Int = {}".format(self.getIntelligence()).center(pad))
        
clear()
playerone = ocupationClass()
playerone.printStats()
