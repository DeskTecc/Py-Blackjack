from random import randint as ri
import keyboard
from time import sleep as delay
from os import system as com
from os import name as sysname
kar_val = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
kar_var = ["_T","_A","_S","_G"]
kar_art= [
    ["A_T","A_A","A_S","A_G","2_T","2_A","2_S","2_G","3_T","3_A","3_S","3_G","4_T","4_A","4_S","4_G","5_T","5_A","5_S","5_G","6_T","6_A","6_S","6_G","7_T","7_A","7_S","7_G","8_T","8_A","8_S","8_G","9_T","9_A","9_S","9_G","10_T","10_A","10_S","10_G","J_T","J_A","J_S","J_G","Q_T","Q_A","Q_S","Q_G","K_T","K_A","K_S","K_G"],
    [" _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "," _____ "],
    ["|A _  |","|A_ _ |","|A .  |","|A ^  |","|2    |","|2    |","|2    |","|2    |","|3    |","|3    |","|3    |","|3    |","|4    |","|4    |","|4    |","|4    |","|5    |","|5    |","|5    |","|5    |","|6    |","|6    |","|6    |","|6    |","|7    |","|7    |","|7    |","|7    |","|8    |","|8    |","|8    |","|8    |","|9    |","|9    |","|9    |","|9    |","|10 & |","|10 v |","|10 ^ |","|10 o |","|J  ww|","|J  ww|","|J  ww|","|J  ww|","|Q  ww|","|Q  ww|","|Q  ww|","|Q  ww|","|K  WW|","|K  WW|","|K  WW|","|K  WW|"],
    ["| ( ) |","|( v )|","| /.\ |","| / \ |","|  &  |","|  v  |","|  ^  |","|  o  |","| & & |","| v v |","| ^ ^ |","| o o |","| & & |","| v v |","| ^ ^ |","| o o |","| & & |","| v v |","| ^ ^ |","| o o |","| & & |","| v v |","| ^ ^ |","| o o |","| & & |","| v v |","| ^ ^ |","| o o |","|& & &|","|v v v|","|^ ^ ^|","|o o o|","|& & &|","|v v v|","|^ ^ ^|","|o o o|","|& & &|","|v v v|","|^ ^ ^|","|o o o|","| o {)|","|   {)|","| ^ {)|","| /\{)|","| o {(|","|   {(|","| ^ {(|","| /\{(|","| o {)|","|   {)|","| ^ {)|","| /\{)|"],
    ["|(_'_)|","| \ / |","|(_._)|","| \ / |","|     |","|     |","|     |","|     |","|     |","|     |","|     |","|     |","|     |","|     |","|     |","|     |","|  &  |","|  v  |","|  ^  |","|  o  |","| & & |","| v v |","| ^ ^ |","| o o |","|& & &|","|v v v|","|^ ^ ^|","|o o o|","| & & |","| v v |","| ^ ^ |","| o o |","|& & &|","|v v v|","|^ ^ ^|","|o o o|","|& & &|","|v v v|","|^ ^ ^|","|o o o|","|o o% |","|(v)% |","|(.)% |","| \/% |","|o o%%|","|(v)%%|","|(.)%%|","| \/%%|","|o o%%|","|(v)%%|","|(.)%%|","| \/%%|"],
    ["|  |  |","|  .  |","|  |  |","|  .  |","|  &  |","|  v  |","|  ^  |","|  o  |","|  &  |","|  v  |","|  ^  |","|  o  |","| & & |","| v v |","| ^ ^ |","| o o |","| & & |","| v v |","| ^ ^ |","| o o |","| & & |","| v v |","| ^ ^ |","| o o |","| & & |","| v v |","| ^ ^ |","| o o |","|& & &|","|v v v|","|^ ^ ^|","|o o o|","|& & &|","|v v v|","|^ ^ ^|","|o o o|","|& & &|","|v v v|","|^ ^ ^|","|o o o|","| | % |","| v % |","| | % |","|   % |","| |%%%|","| v%%%|","| |%%%|","|  %%%|","| |%%%|","| v%%%|","| |%%%|","|  %%%|"],
    ["|____V|","|____V|","|____V|","|____V|","|____Z|","|____Z|","|____Z|","|____Z|","|____E|","|____E|","|____E|","|____E|","|____h|","|____h|","|____h|","|____h|","|____S|","|____S|","|____S|","|____S|","|____9|","|____9|","|____9|","|____9|","|____L|","|____L|","|____L|","|____L|","|____8|","|____8|","|____8|","|____8|","|____6|","|____6|","|____6|","|____6|","|___0I|","|___0I|","|___0I|","|___0I|","|__%%[|","|__%%[|","|__%%[|","|__%%[|","|_%%%O|","|_%%%O|","|_%%%O|","|_%%%O|","|_%%%>|","|_%%%>|","|_%%%>|","|_%%%>|"],
    ]
p1 = [[0],[],[],[0],[]]
p2 = [[1],[],[],[0],[]]
counter = 0
title = 0
def getStarted(p):
    for i in range(2):
        nk = ri(0,12)
        p[1].append(kar_val[nk])
        p[4].append(kar_val[nk]+kar_var[ri(0,3)])
def draw(p):
    nk = ri(0,12)
    vk = ri(0,3)
    p[4].append(kar_val[nk]+kar_var[vk])
    p[1].append(kar_val[nk])
    if p[0][0]==0:
        render([kar_val[nk]+kar_var[vk]])
    return kar_val[nk]
def valid(p):
    val=0
    valr=0
    for i in p[1]:
                if i=="A":
                    valr = 1
                elif i=="J" or i=="Q" or i=="K":
                    valr = 10
                else:
                    valr=i
                val+=int(valr)
                p[3][0]=val
    return val
def render(vals):
    indart = []
    for i in vals:
        indart.append(kar_art[0].index(i))
    for i in range(6):
        print(" ")
        for k in indart:
            print(kar_art[i+1][k], end=" ")
    print("\n")

def cls():
    if(sysname=='nt'):
        com('cls')
    else:
        com('posix')
def start():
    p1 = [[0],[],[],[0],[]]
    p2 = [[1],[],[],[0],[]]
    cls()
    getStarted(p1)
    getStarted(p2)
    #render(p1[4])
    tord = 0
    w=0
    msg = "Starting"
    for i in range(2):
        msg+="."
        print(msg)
        delay(1)
        cls()
    while w==0:
        delay(2)
        if tord%2==0 and len(p1[2])==0:
            print("Your turn\n--------------------------------")
            if(valid(p1)==21):
                print("BLACKJACK!")
                p1[2].append("S")
            elif(valid(p1)>21): #substituir val por valid(p1)
                print("Sorry your hand: "+str(valid(p1)))
                p1[2].append("S")
            else:
                print("Your hand: "+ str(p1[1]))
                render(p1[4])
                op = input("\nD - Draw\nS - Stop\nR:").strip()
                if op=="D":
                    print("\n--------------------------------\n")
                    print("Player 1 draw")
                    print("\n--------------------------------\n")
                    print("You received: "+draw(p1))
                    print("\n--------------------------------\n")
                    if(valid(p1)==21):
                        print("\n--------------------------------\n")
                        print("BLACKJACK!")
                        print("\n--------------------------------\n")
                        p1[2].append("S")
                    elif(valid(p1)>21):
                        print("\n--------------------------------\n")
                        print("Sorry your hand: "+str(valid(p1)))
                        print("\n--------------------------------\n")
                        p1[2].append("S")
                if op=="S":
                    print("\n--------------------------------\n")
                    print("Player 1 decided to STOP")
                    print("\n--------------------------------\n")
                    p1[2].append("S")
            #print("Tot P1: "+str(valid(p1)))
        if tord%2==1 and len(p2[2])==0:
            print("Player 2 turn")
            print("\n--------------------------------\n")
            #print(str(p2[1]))
            val = valid(p2)
            if(val>=17 or val==21):
                print("\n--------------------------------\n")
                print("Player 2 decided to STOP")
                print("\n--------------------------------\n")
                p2[2].append("S")
            else:    
                print("Player 2 draw")
                print("\n--------------------------------\n")
                draw(p2)
            #print("Tot P2: "+str(val))
        if(len(p1[2])!=0 and len(p2[2])!=0):
            val1 = p1[3][0]-21
            val2 = p2[3][0]-21
            reslt = min(val1, val2, key=abs)
            print("\n--------------------------------\n")
            print("Total Player 1: "+str(p1[3][0])+"\n")
            render(p1[4])
            print("\n--------------------------------\n")
            print("Total player 2: "+str(p2[3][0])+"\n")
            render(p2[4])
            if(val1>0 and val2>0):
                if(val1==val2):
                    w=3
                else:
                    w=4
            elif(val1==reslt):
                w=1
            elif(val1>0 and val2<0):
                w=2
            else:
                w=2
        else:
            tord+=1
    if(w==3):
        print("DRAW GAME")
    elif(w==4):
        print("BOTH PLAYERS PASSED 21")
    else:
        print("Player "+str(w)+" won!")
    delay(1)
    print("Press ENTER to back to main menu")
    print("Or SPACE to new game")
    while True:
        if keyboard.is_pressed("SPACE"):
            start()
        if keyboard.is_pressed("ENTER"):
            break
while True:
    if title==0:
        cls()
        print("Press 'SPACE' to start")
        title=1
    if keyboard.is_pressed("SPACE"):
        start()
        title=0
    if keyboard.is_pressed("ESC"):
        break
    counter+=1
print("times played: "+str(counter))
