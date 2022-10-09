# implements the interactivity with the user.
global running
textCenterAmount = 80
ocupation = None
import sys,time,player,os
clear = lambda: os.system('cls') # windows
#clear = lambda: os.system('clear') # mac
screen_width=112
def text(words):
    for characters in words:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.0000)
def startGame():   
    answer = "" 
    global pName
    clear()
    print("  __       __  __       __   ______         _______   _______    ______  \n /  \     /  |/  \     /  | /      \       /       \ /       \  /      \ \n $$  \   /$$ |$$  \   /$$ |/$$$$$$  |      $$$$$$$  |$$$$$$$  |/$$$$$$  |\n $$$  \ /$$$ |$$$  \ /$$$ |$$ |  $$ |      $$ |__$$ |$$ |__$$ |$$ | _$$/ \n $$$$  /$$$$ |$$$$  /$$$$ |$$ |  $$ |      $$    $$< $$    $$/ $$ |/    |\n $$ $$ $$/$$ |$$ $$ $$/$$ |$$ |  $$ |      $$$$$$$  |$$$$$$$/  $$ |$$$$ |\n $$ |$$$/ $$ |$$ |$$$/ $$ |$$ \__$$ |      $$ |  $$ |$$ |      $$ \__$$ |\n $$ | $/  $$ |$$ | $/  $$ |$$    $$/       $$ |  $$ |$$ |      $$    $$/ \n $$/      $$/ $$/      $$/  $$$$$$/        $$/   $$/ $$/        $$$$$$/  \n                                ")
    text(f"Hello there travaler from another world, I plead you to save our world \n")
    text(f"Ohh my where are my manners. Before I continue may I ask for you name travaler \n")
    pName = input("> ")
    player.setName(pName)
    text(f"That's a wonderful name {pName} My name is #### or as some people like to refer to me as the unknown goddess. My role is to oversee my world but right now although don't want to admit it but my world has been forcefully taken over by the demon lord People live in a horrible oppression under the demon lord wish for my people to be happy, so I summoned you from another world Can I count on you in saving the world from demon king '{pName}'??")
    while(answer.lower() != "yes" ):
        answer = input("\n> ")
    text(f"Thank you so much {pName} I knew I could count on you!!! \n") 
    text(f"Before I summon you I must ask you ")
    
startGame()
import Game as g
clear()

#init 
g.clear()
playerone = g.ocupationClass() # creating character class
e1 = g.eni() # creating enemy

# ---- starting game ----

text(f"Thank you for accepting to save this word from the demon king and as you wish I will incarnate you as a {playerone.getclassType()} class hero. In this world you are the one and only hero that they have been waiting for. As I mentioned earlier, I ask you to free this world. You must defeat The demon lord, as he is the source of all anguish in my world. Without him around all of his servants would collapse without a leader to lead him. The demon lord waits for a worthy challenger on his throne at the top of his castle. I beg of you hero please climb his castle and defeat him and free the world. Before I go you may come across foes along your journey that you must fight, please keep in mind that depending on the class you are some courses of action are better than others in disposing of foes like a wizard is better at casting spells than attacking with the sword. The goddess starts mumbling to herself in a sort of way that could only be described as an ancient language. Suddenly a blinding light appears. I instinctively close my eyes. Once I reopen my eyes as the light fades I suddenly find myself surrounded by lush green mountains as far as the eye could see. This is except for one giant tower overshadowing the landscape.\n")
playerone.setHealth(playerone.getHealth()+5)
playerone.printStats()
input("---press enter to continue---".center(textCenterAmount))


#entrence to dungen
g.clear()
text(f"As you wander away from where the goddess entered you into the world you spot the humongous tower that you assumed to be the demon lords tower you enter through the out of place regular looking door. You gather your strength and resolve and start to ascend the tower\n")
input("---press enter to continue---".center(textCenterAmount))


#start first fight ------------------------

text("on the way up the tower you are stoped by a slime which blocks your way up , you steel your self for a fight\n")
e1.changeMob("slime") # set enemy to a slime
clear()
won = g.fight(playerone,e1)

text("\n\n\ncongrats traveler on passing the first trial ")
text("but there is still more")
player.waitingScreen("loading ",1)
    # loading/waiting screen 

clear()   # chance to increse stats using dice  
playerone.printStats()
x = g.gamblingHouse(playerone.getStrength(),playerone.getHealth(),playerone.getDexterity(),playerone.getIntelligence(),playerone.getSpeed())
if (x[0] == "str"):
    playerone.setStrength(playerone.getStrength()+ x[1])
    text("your new stats are as follows") 
    playerone.printStats()
elif (x[0] == "hp"):
    text(f"{x[0]} +{x[1] }")
    playerone.setHealth(playerone.getHealth()+ x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
elif (x[0] == "dex"):
    playerone.setDexterity(playerone.getDexterity()+x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
elif (x[0] == "int"):
    playerone.setIntelligence(playerone.getIntelligence()+ x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
elif (x[0] == "speed"):
    playerone.setSpeed(playerone.getSpeed()+ x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
else:
    pass
player.waitingScreen("loading ",1)

#stage two ------------------------
clear()
text("you pass by the defeated slime and move up the winding stair case catching your breath as you go. \n you keep moving forward untill a hilichurl blocks the path forward\n")
e1.changeMob("hilichurls")
won = g.fight(playerone,e1)
text("\n\ncongrats traveler on passing the second trial ")
text("but there is always more")
if (x[0] == "str"):
    playerone.setStrength(playerone.getStrength()+ x[1])
    text("your new stats are as follows") 
    playerone.printStats()
elif (x[0] == "hp"):
    text(f"{x[0]} +{x[1] }")
    playerone.setHealth(playerone.getHealth()+ x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
elif (x[0] == "dex"):
    playerone.setDexterity(playerone.getDexterity()+x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
elif (x[0] == "int"):
    playerone.setIntelligence(playerone.getIntelligence()+ x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
elif (x[0] == "speed"):
    playerone.setSpeed(playerone.getSpeed()+ x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
else:
    pass
player.waitingScreen("loading ",1)

#stage three ------------------------
clear()
text("after the hard fight with the hilichurl, it lays in front of you defeated you see hes droped an ruby amulet you decide to pick it up. you feel a surge of energy within you (+5 hp) ")
playerone.setHealth(playerone.getHealth()+5)
e1.changeMob("maguu_kenki")
won = g.fight(playerone,e1)
text("\n\ncongrats traveler on passing the second trial ")
text("but there is always more")
if (x[0] == "str"):
    playerone.setStrength(playerone.getStrength()+ x[1])
    text("your new stats are as follows") 
    playerone.printStats()
elif (x[0] == "hp"):
    text(f"{x[0]} +{x[1] }")
    playerone.setHealth(playerone.getHealth()+ x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
elif (x[0] == "dex"):
    playerone.setDexterity(playerone.getDexterity()+x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
elif (x[0] == "int"):
    playerone.setIntelligence(playerone.getIntelligence()+ x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
elif (x[0] == "speed"):
    playerone.setSpeed(playerone.getSpeed()+ x[1])
    text("your new stats are as follows")
    playerone.printStats()
    text(f"{x[0]} +{x[1] }")
else:
    pass
player.waitingScreen("loading ",1)

#stage three ------------------------
clear()
text("you pass by the defeated maguu kenki and move up the winding stair case catching your breath as you go. \n you keep moving forward untill you reach the top and only the demon lord stands infront of you \n")
e1.changeMob("demonlord")
won = g.fight(playerone,e1)
text("\n\ncongrats traveler on defeating the demon lord ")
text("but there is this really the end")
input("> .................. till next time")

