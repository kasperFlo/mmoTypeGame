#implements the game data and logic.
#import classes.barbarian as barb
#clear = lambda: os.system('cls') # windows
clear = lambda: os.system('clear') # mac
from math import ceil
from mimetypes import init
from tabnanny import check
from webbrowser import get
import classes.barbarian as barb,classes.wizzard as wiz,os
textCenterAmount = 60
def selectOcupation(selectClass):
    global ocupation
    if selectClass.lower() == "barbarian" or selectClass.lower() == "barb":
        ocupation = barb.barbarianInfo
    elif selectClass.lower() == "wizard" or selectClass.lower() == "wiz":
        ocupation = wiz.wizzardInfo
def startGame():    
    """
    run this on start to run the game
    """
    landingPad()    
    selectOcupation(input("ocupation classes are 'wizard' 'barbarian' "))
def landingPad():
    """
    lobby screen
    """
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
        print("Class = {}".format(self.getclassType()).center(textCenterAmount))
        print("Str = {}".format(self.getStrength()).center(textCenterAmount))
        print("Hp = {}".format(self.getHealth()).center(textCenterAmount))
        print("Dex = {}".format(self.getDexterity()).center(textCenterAmount))
        print("Int = {}".format(self.getIntelligence()).center(textCenterAmount))
        print("Speed = {}".format(self.getSpeed()).center(textCenterAmount))
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
        print("mobType = {}".format(self.getMobType()).center(textCenterAmount))
        print("Str = {}".format(self.getStrength()).center(textCenterAmount))
        print("Hp = {}".format(self.getHealth()).center(textCenterAmount))
        print("Speed = {}".format(self.getSpeed()).center(textCenterAmount))
        print("Defense = {}".format(self.getDeff()).center(textCenterAmount))
        print("Resistance = {}".format(self.getRess()).center(textCenterAmount))
        print("")

    def changeMob(self,newEni):
        if newEni.lower() == "slime":
            import mobs.slime as slime
            cc = slime.slimeInfo()
            print(f"mob returned stats are {cc}\n".center(textCenterAmount)) # test return value
            self.setMobType(cc[0])
            self.setStrength(cc[1])
            self.setHealth(cc[2])
            self.setSpeed(cc[3])
            self.setDeff(cc[4])
            self.setRess(cc[5])
def checkAlive(thing):
    """
    check if the inputed thing is alive returns true if it is
    """
    x = thing.getHealth()
    if(x > 0):
        return True
    else:
        return False
def youAtk(player, enemy):

    #base dammage calculations
        print("\nwhat plan of attack :".center(textCenterAmount))
        print("(A) cast a spell".center(textCenterAmount))
        print("(B) charge in and swing".center(textCenterAmount))

        atkType = input("")
#spell damage calculations
        if(atkType.lower() == "a"):        
            print("You start charging your Spell ".center(textCenterAmount))
            eleDmg = (player.getStrength() * 0.5) + (player.getIntelligence() * 1) + (player.getDexterity() * 0.8) #spell damage formula 50% str + int + 80% of dex 
            if (eleDmg < 0):  # floor spell damage
                eleDmg = 0.5
            dmgReduction = round(eleDmg * (enemy.getRess()/100),2 )  

            print(f"dmg is reduced by {dmgReduction} because of the targets resistance ".center(textCenterAmount)) 
            trueDamage = eleDmg - dmgReduction # calculate true dmg check factoring in def / res

# physical damage calculations
        else:               
            print("You start readying your Sword ".center(textCenterAmount))
            physDmg = ((player.getStrength() * 1) + (player.getDexterity() * 0.8) + (player.getHealth()) * 0.5)   #sword damage formula str + 80% dex + 50% hp
            if (physDmg < 0):  # floor phys dammage
                physDmg = 1
            dmgReduction = round((physDmg * (enemy.getDeff()/100) ),2) 
            print(f"dmg is reduced by {dmgReduction} because of the defense ".center(textCenterAmount))
            trueDamage = physDmg - dmgReduction  # calculate true dmg check factoring in def / res

# deal dammage to enemy
        trueDamage = round(trueDamage,2)
        enemy.setHealth(enemy.getHealth() - trueDamage)
# check enemy has been defeated
        if(checkAlive(enemy) != True): 
            print(f"{enemy.getMobType()} has been slain".center(textCenterAmount))
            return False
        else:
            if(eleDmg != 0):
                print(f"you hit the {enemy.getMobType()} with a spell dealing {trueDamage} dammage leaveing it with {round(enemy.getHealth(),2)} hp".center(textCenterAmount))
                input("\n----press enter to continue to next turn----\n".center(textCenterAmount))
            else:
                print(f"you hit the {enemy.getMobType()} with a sword swing dealing {trueDamage} dammage leaveing it with {round(enemy.getHealth(),2)} hp".center(textCenterAmount))
                input("\n----press enter to continue to next turn----\n".center(textCenterAmount))

        return True

def takeAtk(player, enemy):
    # deal dammage to user

        enemyDamage = (enemy.getStrength() + enemy.getSpeed()/4)
        print(f"taking damage {enemyDamage}")
        player.setHealth(player.getHealth() - enemyDamage)
        if(checkAlive(player) != True): 
            print(f"you have fainted as you have {player.getHealth}hp remaining ")
            return False

def fight(player, enemy):
    running = True
    print(f"you are fighting a {enemy.getMobType()}".center(textCenterAmount))


    while (running == True):
        #clear()
        eleDmg = 0
        physDmg = 0
        global trueDamage

# state enimies
        print(f"{enemy.getMobType()} currently has {round(enemy.getHealth(),2)} hp".center(textCenterAmount))

#speed check
        if (player.getSpeed() >  enemy.getSpeed()): 
            running = youAtk(player, enemy)
            running = takeAtk(player, enemy)
        else:
            priority = 2
            running = takeAtk(player, enemy)
            running = youAtk(player, enemy)


# starting ----------------------------------

# creating character class
playerone = ocupationClass()
clear()
playerone.printStats()

# creating default enemy
e1 = eni()
#e1.printStats()

# changing enemy to a slime
e1.changeMob("slime")
e1.printStats()

#start fight
fight(playerone,e1)

