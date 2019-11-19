import os
import time 





#####MENU#####       

def getmenuoptions():
    print()
    choice = None
    choice = input("""
    -----Menu-----
    Please Choose an Option
    A: Games
    B: Scores
    C: Quit
    Created by: Ben Norman.

: """)
    choice = choice.lower()

    if choice == 'a':
        time.sleep(0.2)
        Games()
    elif choice == 'b':
        Scores()

    elif choice == 'c':
        quit()
    else:
        print("You did not select an option, please select an option to continue")
        getmenuoptions()

def Games():
    print()

    choice = input("""
    ----------
    1: Pong
    2: Snake
    3: Tetris
    4: Space Invaders
    5: Hang Man
    6: Main Menu
: """)

    if choice == '1':
        os.system("Pong.py")
        return
    elif choice == '2':
        os.system("Snake.py")
        return
    elif choice == '3':
        os.system("Tetris.py")
        return
    elif choice == '4':
        os.system("spaceinvaders.py")
        return
    elif choice == '5':
        os.system("Hangman.py")
        return
    elif choice == '6':
        time.sleep(0.2)
        getmenuoptions()
    else:
        print("You did not select a stage, please select a stage to continue")
    Games()


def Scores():
    print("Scores")
    for x in scores:
        print(x)






print("Before we begin, what is your name??")
name = input("\n >")
choice = input("Have you opened the launcher to see your score?? \n>")

if choice == "yes":
    print("Thank You, launcher is now loading.")
    time.sleep(0.5)
    print("Thank You, launcher is now loading..")
    time.sleep(0.5)
    print("Thank You, launcher is now loading...")
    time.sleep(0.5)
    scores = open("scores.txt", "r")
else:    
    print("Thank You, launcher is now loading.")
    time.sleep(0.5)
    print("Thank You, launcher is now loading..")
    time.sleep(0.5)
    print("Thank You, launcher is now loading...")
    time.sleep(0.5)
    scores = open("scores.txt", "a")
    scores.write("\n")
    scores.write("\n")
    scores.write(name)
    scores.close()

getmenuoptions()




    
