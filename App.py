# implements the interactivity with the user.
global running
textCenterAmount = 80
ocupation = None
import sys,time,player,os
#clear = lambda: os.system('cls') # windows
clear = lambda: os.system('clear') # mac
screen_width=112

def text(words):
    for characters in words:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.0)


def startGame():   
    answer = "no" 
    """
    run this on start to run the game
    """
    clear()
    print("  __       __  __       __   ______         _______   _______    ______  \n /  \     /  |/  \     /  | /      \       /       \ /       \  /      \ \n $$  \   /$$ |$$  \   /$$ |/$$$$$$  |      $$$$$$$  |$$$$$$$  |/$$$$$$  |\n $$$  \ /$$$ |$$$  \ /$$$ |$$ |  $$ |      $$ |__$$ |$$ |__$$ |$$ | _$$/ \n $$$$  /$$$$ |$$$$  /$$$$ |$$ |  $$ |      $$    $$< $$    $$/ $$ |/    |\n $$ $$ $$/$$ |$$ $$ $$/$$ |$$ |  $$ |      $$$$$$$  |$$$$$$$/  $$ |$$$$ |\n $$ |$$$/ $$ |$$ |$$$/ $$ |$$ \__$$ |      $$ |  $$ |$$ |      $$ \__$$ |\n $$ | $/  $$ |$$ | $/  $$ |$$    $$/       $$ |  $$ |$$ |      $$    $$/ \n $$/      $$/ $$/      $$/  $$$$$$/        $$/   $$/ $$/        $$$$$$/  \n                                ")
    text("Hello there travaler from another world, I plead you to save our world \n")
    text("Ohh my where are my manners. Before I continue may I ask for you name travaler \n")
    global pName
    pName = input("> ")
    player.setName(pName)
    text("\nThats a wonderful name '") ; text(pName)
    text("' My name is #### or as some people refer to me as the unknown goddess \n")
    text("My role is to oversee my world but right now although \n")
    text("I dont want to admit it but my world has been forcefully taken over by the demon lord \n")
    text("People live in a horible opresion under the demon lord  \n")
    text("I wish for my people to be happy, so I summoned you from another world \n")
    text("Can I count on you in saving the world from demon king '")
    text(pName) ; text("' ??\n")
    while(answer.lower() != "yes" ):
        answer = input("> ")
    answer = "i agree"
    text("Thank you so much '") ; text(pName) ; text("' I knew I could count on you!!! \n") 
    text("Before I summon you \nI must ask you what do type of fighter do best picture yourself as ")
startGame()
import Game as g

player.waitingScreen("\nstarting",0.8)
# ---- starting game ----

g.clear()
#init
playerone = g.ocupationClass() # creating character class
e1 = g.eni() # creating enemy
"""
playerone.printStats()
text("wow is this you so butifull so strong sheeeeeeeeeeeeesh ^^^^\n".center(textCenterAmount))

#stage one
print("random bullshit enter ready to enter the dungen".center(textCenterAmount))
input("---press enter to continue---".center(textCenterAmount))
player.waitingScreen("",0.8)
# changing enemy to a slime
e1.changeMob("slime")

#start first fight
g.clear()
won = g.fight(playerone,e1)
if (won == True):
    text("\n\n\ncongrats traveler on passing the first trial ")
    text("but there is still more")
player.waitingScreen("",1)
    # loading/waiting screen 
"""

clear()    
playerone.printStats()
g.gamblingHouse(playerone.getStrength(),playerone.getHealth(),playerone.getDexterity(),playerone.getIntelligence(),playerone.getSpeed())

#stage two
clear()
text("random lore dump enter stage / trial two blah blah blahcblah blah blahcblah blah blahc\n")
e1.changeMob("goblin")
won = g.fight(playerone,e1)
if (won == True):
    text("\n\n\congrats traveler on passing the second trial ")
    text("but there is always more")
input("> ")