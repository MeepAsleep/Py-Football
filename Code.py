######################## JAWAHAR NAVODAYA VIDYALAYA DK, MUDIPU ##########################

########################### PYTHON INVESTIGATORY PROJECT #############################

####################### FOOTBALL GAME AND SCORE MANAGEMENT SYSTEM ########################

###################### MADE BY ROHAN RAGHAVAN, SUDEEP S AND RAHUL K ########################

# Modules Used

import pdb
import random
import csv

# Global Variables used in various functions

ch = 0
a = 0
b = 0
goal = True
point = 0
new = []
cpuint = 0
na = ''

# Function Definitions

# Set Difficulty

def op():
    print('\nSet Difficulty:\n1- Easy\n2- Hard\n3- Insane')
    global ch
    ch = int(input())

# Change User

def User():

    global na
    
    na = input('Enter Username (case sensitive)>>>')
        
    with open('Highscores.csv','r',newline='') as file:
            
        fr = csv.reader(file)
        an = []
            
        for i in fr:
            an.append(i[0])
                
        if na in an:
            print('\nAlready Registered!! Welcome Back :)\n')

        else:

            with open('Highscores.csv','a',newline='') as file:
                rw=csv.writer(file)
                rw.writerow([na,0])

# Update Score in Data File

def update():
    global na
    global new
    global ch
    
    with open('Highscores.csv','r',newline='') as file:
        fr = csv.reader(file)
        new = []
        for i in fr:
            new.append(i)
        for i in new:
            if i[0]==na:
                j = int(i[1])
                if ch == 1:
                    j+=1
                elif ch == 2:
                    j+=3
                elif ch == 3:
                    j+=7
                i[1]=j
                
    with open('Highscores.csv','w',newline='') as file:
        fw = csv.writer(file)
        fw.writerows(new)

# Bubble Sorting inside the CSV file used

def sort():
    global lines
    with open('Highscores.csv','r') as file:
        fr = csv.reader(file)
        lines = []
        for i in fr:
            lines.append(i)
        n = len(lines)
        #pdb.set_trace()
        for i in range(n):
            for j in range(0,n-i-1):
                if lines[j][1] == 'Score':
                    continue
                else:
                    if int(lines[j][1]) < int(lines[j+1][1]):
                        lines[j],lines[j+1] = lines[j+1],lines[j]
                    
        with open('Highscores.csv','w',newline='') as file:
            fw = csv.writer(file)
            fw.writerows(lines)


# Main Function for Game excecution

def shoot():
    global goal
    global a
    global b
    global cpuint
    global ch

    pos = int(input('''\n  _______________________
||                                   ||
||  |1|         |2|         |3|  ||
||               ___               ||
||              {0 - 0}              ||
||  |4|       ---|_|---      |5|  ||
||               /  \               ||\n\nChoose where you want to shoot!\n\n>>>'''))
    
    l1 = []
    
    for i in range(ch):
        #pdb.set_trace()
        r = random.randint(1,5)
        l1.append(r)

    if pos in l1:
        goal = False

    elif pos > 5:
        goal = False

    else:
        goal = True
        
    if goal == True:
        print('GOAAAAAL!!!')
        a+=1
    else:
        print('You Missed :(')

    print("\n~~~Opponent's Turn~~~\n")
    l1 = []
    goal = True
    cpos = random.randint(1,5)
    cpuint = 3
    l = len(l1)
    while True:
        r = random.randint(1,5)
        if len(l1) == 3:
            break
        else:
            if r in l1:
                continue
            else:
                l1.append(r)
                l+=1
        
    if cpos in l1:
        goal = False

    else:
        goal = True
    
    if goal == True:
        print('GOAAAAAL!!!')
        b+=1
    else:
        print('It Missed :)')

            

# User Input Call

User()

# Initial Difficulty Set

op()

# Main Infinite Loop

while True:
    
    print('\t~~~KICK OFF~~~')
    print('   ~~~Penalty Shootout Game~~~\n')
    print('''1- PLAY

2- SCOREBOARD

3- CHANGE DIFFICULTY

4- INSTRUCTIONS

5- CHANGE USER

6- EXIT''')

    k = int(input('\n>>'))


    if k == 1:
        
        
        for i in range(5):

            # Main game function call
            
            shoot()

        print('\nScore-',a,'-',b)
        
        if a>b:

            print('\n  ~~~YOU WIN!!!~~~')

            # Updating Scores inside the CSV file after a win

            update()
            
        elif a<b:
            print('\n  ~~~MATCH LOST~~~')
            
        else:
            print('\n  ~~~MATCH TIED~~~')

        a,b=0,0

        print('Press Enter to continue...')

        input()

    elif k == 2:

        # Sorting the list in the CSV file before displaying
        
        sort()

        with open('Highscores.csv','r') as file:

            fr=csv.reader(file)
            print('\tLEADERBOARD\n')

            for i in fr:

                if i[0] == 'Username':
                    print(i[0]+'\t'+i[1])
                else:
                    print(i[0]+'\t\t  '+i[1])

        print('\nPress Enter to continue...')
        input()

    elif k == 3:

        op()

    elif k == 4:

        # Instructions as a multiple line string
        
        print('''\n\tWelcome to Kick Off!

Press one of the numbers displayed inside the goalpost. The keeper may or may not save it.
Player and computer get 5 tries each. The one who scores most goals out of 5 wins.
Scores will be updated for every win!

Easy mode: Win = +1 points
Hard mode: Win = +3 points
Insane mode: Win = +7 points

Press Enter to continue...''')
        input()

    elif k == 5:

        # Funtion for User Change 

        User()
    
    elif k == 6:

        print('Thank you for playing this game.\nGoodbye, See you soon :)')

        # Main loop break point
        
        break

    else:

        print('Invalid choice... Try again O-O')

################################### THE END #################################

################################## THANK YOU #################################
