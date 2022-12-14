#implements the game data and logic.
#import classes.barbarian as barb
clear = lambda: os.system('cls') # windows
#clear = lambda: os.system('clear') # mac
from mimetypes import init
from operator import truediv
from tabnanny import check
from webbrowser import get
import classes.barbarian as barb,classes.wizard as wiz,os,sys,time,player
textCenterAmount = 80
screen_width=112
from random import randint
#--------------------------------------------- main method


def text(words):
    for characters in words:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.0018)
def selectOcupation():
    global ocupation
    while(True):
        text("what do type of fighter do best picture yourself as (wizzard) (barbarian)")
        answer = input("\n > ")
        if(answer.lower() == "wizard" or answer.lower() == "wiz"):
            ocupation = wiz.wizardInfo
            break
        elif(answer.lower() == "barb" or answer.lower() == "barbarian"):
            ocupation = barb.barbarianInfo
            break
selectOcupation()
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

        print('\033[94m')

        print(f"Name = {player.getName()}".center(textCenterAmount))
        
        print("Class = {}".format(self.getclassType()).center(textCenterAmount))
        time.sleep(0.18)
        print("Str = {}".format(self.getStrength()).center(textCenterAmount))
        time.sleep(0.18)
        print("Hp = {}".format(self.getHealth()).center(textCenterAmount))
        time.sleep(0.18)
        print("Dex = {}".format(self.getDexterity()).center(textCenterAmount))
        time.sleep(0.18)
        print("Int = {}".format(self.getIntelligence()).center(textCenterAmount))
        time.sleep(0.18)
        print("Speed = {}".format(self.getSpeed()).center(textCenterAmount))

        print('\u001b[0m')
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
        print(f"\u001b[36myou currently are fighting a {self.getMobType()} the details are as follows\u001b[0m\n")
        print('\033[93m')    
        print("mob clasification = {}".format(self.getMobType()).center(textCenterAmount))
        
        print("Str = {}".format(self.getStrength()).center(textCenterAmount))
        time.sleep(0.18)
        print("Hp = {}".format(round(self.getHealth(),2)).center(textCenterAmount))
        time.sleep(0.18)
        print("Speed = {}".format(self.getSpeed()).center(textCenterAmount))
        time.sleep(0.18)
        print("Defense = {}".format(self.getDeff()).center(textCenterAmount))
        time.sleep(0.18)
        print("Resistance = {}".format(self.getRess()).center(textCenterAmount))
        print('\033[0m')
        print("")
    def changeMob(self,newEni):
        if newEni.lower() == "slime":
            import mobs.slime as slime
            cc = slime.slimeInfo()
        elif newEni.lower() == "hilichurls":
            import mobs.hilichurls as hilichurls
            cc = hilichurls.hilichurlsInfo()
        elif newEni.lower() == "maguu_kenki":
            import mobs.maguu_kenki as maguu_kenki
            cc = maguu_kenki.maguu_kenkiInfo()
        elif newEni.lower() == "demonlord":
            import mobs.demonLord as demonLord
            cc = demonLord.demonLordInfo()

        #print(f"mob returned stats are {cc}\n".center(textCenterAmount)) # test return valueGame.py
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
    eleDmg = 0
    physDmg = 0
    #base dammage calculations
    print("\u001b[32m\nwhat plan of attack :\u001b[0m".center(textCenterAmount))
    print("\u001b[32m(A) cast a spell\u001b[0m".center(textCenterAmount))
    print("\u001b[32m(B) charge in and swing\u001b[0m".center(textCenterAmount))

    atkType = input("")
#spell damage calculations
    if(atkType.lower() == "a"):        
        print("\u001b[35mYou start charging your Spell \u001b[0m".center(textCenterAmount))
        eleDmg = (player.getStrength() * 0.5) + (player.getIntelligence() * 1) + (player.getDexterity() * 0.8) #spell damage formula 50% str + int + 80% of dex 
        if (eleDmg < 0):  # floor spell damage
            eleDmg = 0.5
        dmgReduction = round(eleDmg * (enemy.getRess()/100),2 )  

        print(f"dmg is \u001b[34mreduced by {dmgReduction} \u001b[0mbecause of the targets resistance ".center(textCenterAmount)) 
        trueDamage = eleDmg - dmgReduction # calculate true dmg check factoring in def / res

# physical damage calculations
    else:               
        print("\u001b[35mYou start readying your Sword \u001b[0m".center(textCenterAmount))
        physDmg = ((player.getStrength() * 1) + (player.getDexterity() * 0.8) + (player.getHealth()) * 0.5)   #sword damage formula str + 80% dex + 50% hp
        if (physDmg < 0):  # floor phys dammage
            physDmg = 1
        dmgReduction = round((physDmg * (enemy.getDeff()/100) ),2) 
        print(f"dmg is \u001b[34mreduced by {dmgReduction}\u001b[0m because of the defense ".center(textCenterAmount))
        trueDamage = physDmg - dmgReduction  # calculate true dmg check factoring in def / res

# deal dammage to enemy
    trueDamage = round(trueDamage,2)
    enemy.setHealth(enemy.getHealth() - trueDamage)
# check enemy has been defeated
    if(checkAlive(enemy) != True): 
        if(eleDmg > 0): # enemy slain 
             #spell has been cast
            print(f"\u001b[35m{enemy.getMobType()} has been slain with a mighty spell dealing {trueDamage}dmg\u001b[0m".center(textCenterAmount))
        else:  #sword has been used
            print(f"\u001b[35m{enemy.getMobType()} has been slain with a sword swing dealing {trueDamage}dmg\u001b[0m".center(textCenterAmount))
        return False
    else:  # enemy alive
        if(eleDmg > 0): #spell has been cast
            print(f"you hit the {enemy.getMobType()} with a spell \u001b[32mdealing {trueDamage} damage\u001b[0m leaveing it with {round(enemy.getHealth(),2)} hp".center(textCenterAmount))
        else: #sword has been used
            print(f"you hit the {enemy.getMobType()} with a sword swing \u001b[32mdealing {trueDamage} damage\u001b[0m leaveing it with {round(enemy.getHealth(),2)} hp".center(textCenterAmount))
    return True
def takeAtk(player, enemy):
    # deal dammage to user

        enemyDamage = (enemy.getStrength() + enemy.getSpeed()/4)
        player.setHealth(player.getHealth() - enemyDamage)
        print(f"You take a hit from \u001b[31m{enemy.getMobType()} taking {enemyDamage} damage\u001b[0m leaving you with {player.getHealth()}hp")
        if(checkAlive(player) != True):  # player fainted
            print(f"You have fainted as you have {player.getHealth()}HP remaining ")
            return False
        return True
def fight(player, enemy) -> bool:
    """
    returns winner of fight with bool
    False player lose
    True player won
    """
    running = True
    print(f"You are engage in combat with a {enemy.getMobType()}")
    turn = 1

    while (running == True):
        global trueDamage
        fightWinner = None
        #clear()
# state enimies
        print(f"{enemy.getMobType()} currently \u001b[35m has {round(enemy.getHealth(),2)} HP\u001b[0m".center(textCenterAmount))
        print(f"You currently\u001b[35m have {round(player.getHealth(),2)} HP\u001b[0m".center(textCenterAmount))
        print(f"\u001b[36mTurn {turn}\u001b[0m\n")
        player.printStats()
        enemy.printStats()
#speed check
        if (player.getSpeed() >  enemy.getSpeed()): 
            #priority move
            type(f"you move fast on your feet getting the first move")
            running = youAtk(player, enemy)
            if running == False:
                fightWinner = True
                return fightWinner
            running = takeAtk(player, enemy)
            if running == False:
                gameEnd()
        else:
            #priority second
            type(f"your opponent moves faster getting the first move")
            running = takeAtk(player, enemy)
            if running == False:
                gameEnd()   
            running = youAtk(player, enemy)
            if running == False:
                fightWinner = True
                return fightWinner
        input(u"\u001b[36m\n----press enter to continue to next turn----\n\u001b[0m".center(textCenterAmount))
        turn += 1   
def gameEnd():
    time.sleep(5)
    clear()
    text("  ______                                            ______                                \n /      \                                          /      \                               \n/$$$$$$  |  ______   _____  ____    ______        /$$$$$$  | __     __  ______    ______  \n$$ | _$$/  /      \ /     \/    \  /      \       $$ |  $$ |/  \   /  |/      \  /      \ \n$$ |/    | $$$$$$  |$$$$$$ $$$$  |/$$$$$$  |      $$ |  $$ |$$  \ /$$//$$$$$$  |/$$$$$$  |\n$$ |$$$$ | /    $$ |$$ | $$ | $$ |$$    $$ |      $$ |  $$ | $$  /$$/ $$    $$ |$$ |  $$/ \n$$ \__$$ |/$$$$$$$ |$$ | $$ | $$ |$$$$$$$$/       $$ \__$$ |  $$ $$/  $$$$$$$$/ $$ |      \n$$    $$/ $$    $$ |$$ | $$ | $$ |$$       |      $$    $$/    $$$/   $$       |$$ |      \n $$$$$$/   $$$$$$$/ $$/  $$/  $$/  $$$$$$$/        $$$$$$/      $/     $$$$$$$/ $$/       \n                                                                                          \n                                                                                          \n                                                                                          ")
    text("\nthere is always next time traveler i hope to see you again ")
    sys.exit()

def properWager(wagerTypeInp,wagerAmount,stre,hp,dex,intl,speed):
    if(wagerTypeInp == "str"):
        if(wagerAmount <= stre and wagerAmount > 0) :
            return True
    elif(wagerTypeInp == "hp"):
            if (wagerAmount >= hp) and wagerAmount > 0:
                return True
    elif(wagerTypeInp == "dex"):
        if(wagerAmount <= dex and wagerAmount > 0): 
            return True
    elif(wagerTypeInp == "int"):
        if(wagerAmount <= intl and wagerAmount > 0):
            return True
    elif(wagerTypeInp == "speed"):
        if(wagerAmount <= speed and wagerAmount > 0 ):
            return True
    else:
        return False
def gamblingHouse(stre,hp,dex,intl,speed):
    running = True

    text(f"on the way u you see a shady looking individual, he spots you and asks")
    text(f"would you like to wager some or your strength for a chance for greater strength hero? (yes or no)\n")
    victim = input("> ")
    if (victim.lower().strip() == "yes" or victim.lower().strip() == "y"): 
        text("this shady individual asks you ")
        while(running == True):
            text("what part of you would you like to wager ")
            text("(str)(hp)(dex)(int)(speed)\n")
            while(True):
                wagerType = str(input("> "))
                if (wagerType != "str" and wagerType != "hp" and wagerType != "dex" and wagerType != "int" and wagerType != "speed" ):
                    print("pick an actual stat that you have")
                else:
                    break
            text("how much of this stat would you like to wager?\n")
            wagerTypeAmount = float(input("> "))
            if(properWager(wagerType,wagerTypeAmount,stre,hp,dex,intl,speed)):
                break
            else:
                text(f"you do not have enough {wagerType} stats to wager\n")
                text("the shady man asks you again\n\n\n")
        #actual betting
        text(f"the house says they can double your wager puting {wagerTypeAmount*2} {wagerType} stat points on the table\n")
        text(f"he tells you to roll a six sided dice, the dealer decides for you to win the wager you must roll a number higher then four\n")
        text(f"you take the dice in your hand clinching your fist, and just like that you rolled the dice\n")
        player.waitingScreen(" rolling",0.7)
        roll = randint(1,6)
        text(f"\nyou rolled a {roll} ")
        if (roll > -1): 
            text(f"congrats on the winning the wager. Im a man of my word il keep my end of the deal here you go {wagerTypeAmount*2} {wagerType} stat points\n")
            player.waitingScreen("pleasure doing business with you sir I hope to see you around again ",1)
            return wagerType,(wagerTypeAmount*2)
        else:
            text(f"unlucky on your end unfortunatly I must be taking {wagerTypeAmount} {wagerType} from you\n")
            player.waitingScreen("pleasure doing business with you sir I hope to see you around again \n",1)
            return wagerType,(wagerTypeAmount*-1)


    else: # says no to gambling
        text("very well then good day to you\n")
        return "nothing" , 0