#implements the game data and logic.
#import classes.barbarian as barb
#clear = lambda: os.system('cls') # windows
clear = lambda: os.system('clear') # mac
from math import ceil
from mimetypes import init
from webbrowser import get
import classes.barbarian as barb,classes.wizzard as wiz,os

def selectOcupation(selectClass):
    global ocupation
    if selectClass.lower() == "wizzard" or selectClass.lower() == "wiz":
        ocupation = wiz.wizzardInfo
    elif selectClass.lower() == "barbarian" or selectClass.lower() == "barb":
        ocupation = barb.barbarianInfo
def startGame():    
    landingPad()    
    selectOcupation(input("ocupation classes are 'wizzard' 'barbarian' "))
def landingPad():
    clear()
    print("  __       __  __       __   ______         _______   _______    ______  \n /  \     /  |/  \     /  | /      \       /       \ /       \  /      \ \n $$  \   /$$ |$$  \   /$$ |/$$$$$$  |      $$$$$$$  |$$$$$$$  |/$$$$$$  |\n $$$  \ /$$$ |$$$  \ /$$$ |$$ |  $$ |      $$ |__$$ |$$ |__$$ |$$ | _$$/ \n $$$$  /$$$$ |$$$$  /$$$$ |$$ |  $$ |      $$    $$< $$    $$/ $$ |/    |\n $$ $$ $$/$$ |$$ $$ $$/$$ |$$ |  $$ |      $$$$$$$  |$$$$$$$/  $$ |$$$$ |\n $$ |$$$/ $$ |$$ |$$$/ $$ |$$ \__$$ |      $$ |  $$ |$$ |      $$ \__$$ |\n $$ | $/  $$ |$$ | $/  $$ |$$    $$/       $$ |  $$ |$$ |      $$    $$/ \n $$/      $$/ $$/      $$/  $$$$$$/        $$/   $$/ $$/        $$$$$$/  \n                                ")
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
    def setSpeed(self,newSpeedValue):
        self.Speed = newSpeedValue

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
    def getSpeed(self):
        return self.speed
    
    def printStats(self):
        pad = 30
        print("Class = {}".format(self.getclassType()).center(pad))
        print("Str = {}".format(self.getStrength()).center(pad))
        print("Hp = {}".format(self.getHealth()).center(pad))
        print("Dex = {}".format(self.getDexterity()).center(pad))
        print("Int = {}".format(self.getIntelligence()).center(pad))
        print("Speed = {}".format(self.getSpeed()).center(pad))
        print("")

class eni():
    def __init__(self) -> None:
            self.mobType = "default"
            self.Strength = 0
            self.Health = 0
            self.Speed = 0
            self.Deff = 0
            self.Ress = 0

    def getMobType(self):
        return self.mobType
    def getStrength(self):
        return self.Strength
    def getHealth(self):
        return self.Health
    def getSpeed(self):
        return self.Speed
    def getDeff(self): 
        return self.Deff
    def getRess(self): 
        return self.Ress

    def setMobType(self,newMobType):# dammage
        self.mobType = newMobType
    def setStrength(self,newStrengthValue):# dammage
        self.Strength = newStrengthValue
    def setHealth(self,newHealthValue):# health
        self.Health = newHealthValue
    def setSpeed(self,newSpeedValue):# speed 
        self.Speed = newSpeedValue
    def setDeff(self,newDeffValue):# defense 
        self.deff = newDeffValue
    def setRess(self,newRessValue):# resistance 
        self.Ress = newRessValue
    

    def printStats(self):
        pad = 30
        print("mobType = {}".format(self.getMobType()).center(pad))
        print("Str = {}".format(self.getStrength()).center(pad))
        print("Hp = {}".format(self.getHealth()).center(pad))
        print("Speed = {}".format(self.getSpeed()).center(pad))
        print("Defense = {}".format(self.getDeff()).center(pad))
        print("Resistance = {}".format(self.getRess()).center(pad))

    def changeMob(self,newEni):
        if newEni.lower() == "slime":
            import mobs.slime as slime
            cc = slime.slimeInfo()
            print(f"slime testing {cc}\n") # test return value
            self.setMobType(cc[0])
            self.setStrength(cc[1])
            self.setHealth(cc[2])
            self.setSpeed(cc[3])
            self.setDeff(cc[4])
            self.setRess(cc[5])

def fight(player, enemy):
    running = True
    eDmg = 0
    pDmg = 0

    while (running == True):
        #clear()
#speed check
        if (player.getSpeed() >  enemy.getSpeed()): 
            priority = 1
        else:
            priority = 2
#base dammage calculations
        atkType = input("what plan of attack : \n(A) cast a spell\n(B) change in and swing\n") 
        if( atkType.lower() == "a"):        #spell damage calculations
            print("You start charging your Spell ")
            eleDmg = (player.getStrength() * 0.5) + (player.getIntelligence() * 1) + (player.getDexterity() * 0.8) #spell damage formula 50% str + int + 80% of dex 
            if (eleDmg < 0):  # floor spell damage
                eleDmg = 0.5
            dmgReduction = round((eleDmg * (enemy.getRess()/100) ))
            print(f"dmg is reduced by {dmgReduction} because of the targets resistance ")
            damageTaken = eleDmg - dmgReduction
            print(f"you hit the {enemy.getMobType()} with a spell dealing {damageTaken} dammage ")

        else:
            print("You start readying your Sword ")
            physDmg = ((player.getStrength() * 1) + (player.getDexterity() * 0.8) + (player.getHealth()) * 0.5)   #sword damage formula str + 80% dex + 50% hp
            if (physDmg < 0):  # floor phys dammage
                physDmg = 1
            dmgReduction = round((physDmg * (enemy.getDeff()/100) ),3)
            print(f"dmg is reduced by {dmgReduction} because of the defense ")
            damageTaken = physDmg - dmgReduction
            
            print(f"you hit the {enemy.getMobType()} with a sword swing dealing {damageTaken} dammage ")

        input("----press enter to continue to next turn----")
# actual dmg check 
        

        



# starting ----------------------------------

# creating character class
playerone = ocupationClass()
clear()
playerone.printStats()

# creating default enemy
e1 = eni()
e1.printStats()

# changing enemy to a slime
e1.changeMob("slime")
e1.printStats()

#start fight
fight(playerone,e1)