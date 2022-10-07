pName = None
import sys,time
def text(words):
    for characters in words:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.018)
def getName():
    return pName
def setName(word):
    global pName
    pName = word
def waitingScreen(words,t):
    text(f"{words}")
    for i in range(3):
        text(". ")
        time.sleep(1*t)