import math
import os
from Logo import logo

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    EXTIT = '\033[34m'
    WARNING = '\033[93m'
    PROCESS = '\033[36m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def pause():
    print(bcolors.WARNING + "Press [Enter] key to continue. " + bcolors.END)
    try:
        input()
    except:
        pass

clear = lambda: os.system('clear')

clear()

print(bcolors.WARNING + "This programm must not be used to cheat during a test or exam unless with the agreement of the teacher." + bcolors.END)
pause()
clear()
logo()
pause()

def main():
    clear()
    print(bcolors.OKBLUE + "-------Main menu-------" + bcolors.END)
    print(bcolors.EXTIT + "1) " + bcolors.END + "Pythagore menu")
    print(bcolors.EXTIT + "2) " + bcolors.END + "Trigonometry menu")
    print(bcolors.OKBLUE + "-----------------------" + bcolors.END)
    print(bcolors.WARNING + "Please choose one of the numbers in the menu, or press [CTRL+C] to exit. " + bcolors.END)
    try:
        command = ""
        command = input()
    except SyntaxError:
        print(bcolors.FAIL + "Please enter a number. " + bcolors.END)
        pause()
        main()
    except KeyboardInterrupt:
        clear()
        print("Have a pleasent day. ")
        pause()
        clear()
        exit()
    if command == 1:
        Pythagore()
    elif command == 2:
        Trigonometry()
    else:
        print(bcolors.FAIL + "Please chosse one of the numbers in the menu. " + bcolors.END)
        main()

def Pythagore():
    clear()
    print(bcolors.OKBLUE + "-------Pythagore menu-------" + bcolors.END)
    print(bcolors.EXTIT + "1) " + bcolors.END + "Find the length of the hypothenus")
    print(bcolors.EXTIT + "2) " + bcolors.END + "Find the length of an adjacent side")
    print(bcolors.EXTIT + "3) " + bcolors.END + "Main menu")
    print(bcolors.OKBLUE + "-----------------------" + bcolors.END)
    print(bcolors.WARNING + "Please choose one of the numbers in the menu, or press [CTRL+C] to exit. " + bcolors.END)
    try:
        command = ""
        command = input()
    except SyntaxError:
        print(bcolors.FAIL + "Please enter a number. " + bcolors.END)
        pause()
        main()
    except KeyboardInterrupt:
        clear()
        print("Have a pleasent day. ")
        pause()
        clear()
        exit()
    if command == 1:
        hypothenus()
    elif command == 2:
        adjacent()
    elif command == 3:
        main()
    else:
        print(bcolors.FAIL + "Please chosse one of the numbers in the menu. " + bcolors.END)
        Pythagore()

def Trigonometry():
    clear()
    print(bcolors.OKBLUE + "-------Trigonometry menu-------" + bcolors.END)
    print(bcolors.EXTIT + "1) " + bcolors.END + "Calculate the sinus")
    print(bcolors.EXTIT + "2) " + bcolors.END + "Calculate the cosinus")
    print(bcolors.EXTIT + "3) " + bcolors.END + "Calculate the tangeante")
    print(bcolors.OKBLUE + "-----------Reciprocal----------")
    print(bcolors.EXTIT + "4) " + bcolors.END + "Calculate the angle of a sinus")
    print(bcolors.EXTIT + "5) " + bcolors.END + "Calculate the angle of a cosinus")
    print(bcolors.EXTIT + "6) " + bcolors.END + "Calculate the angle of a tangeante")
    print(bcolors.OKBLUE + "-----------------------" + bcolors.END)
    print(bcolors.EXTIT + "7) " + bcolors.END + "Main menu")
    print(bcolors.OKBLUE + "-----------------------" + bcolors.END)
    print(bcolors.WARNING + "Please choose one of the numbers in the menu, or press [CTRL+C] to exit. " + bcolors.END)
    try:
        command = ""
        command = input()
    except SyntaxError:
        print(bcolors.FAIL + "Please enter a number. " + bcolors.END)
        pause()
        main()
    except KeyboardInterrupt:
        clear()
        print("Have a pleasent day. ")
        pause()
        clear()
        exit()
    if command == 1:
        sin()
    elif command == 2:
        cos()
    elif command == 3:
        tan()
    elif command == 4:
        asin()
    elif command == 5:
        acos()
    elif command == 6:
        atan()
    elif command == 7:
        main()
    else:
        print(bcolors.FAIL + "Please chosse one of the numbers in the menu. " + bcolors.END)
        Trigonometry()
    Trigonometry()

def sin():
    clear()
    print(bcolors.WARNING + "Please enter the angle in degrees. " + bcolors.END)
    angle = math.radians(float(input()))
    try:
        sin = math.sin(angle)
        clear()
        print("The sinus of " + math.degrees(str(angle)) + " is " + str(sin))
        pause()
    except Exception as e:
        clear()
        print(bcolors.FAIL + str(e) + bcolors.END)
        pause()

def cos():
    clear()
    print(bcolors.WARNING + "Please enter the angle in radians. " + bcolors.END)
    angle = float(input())
    try:
        cos = math.cos(angle)
        clear()
        print("The cosinus of " + str(angle) + " is " + str(cos))
        pause()
    except Exception as e:
        clear()
        print(bcolors.FAIL + str(e) + bcolors.END)
        pause()

def tan():
    clear()
    print(bcolors.WARNING + "Please enter the angle in radians. " + bcolors.END)
    angle = float(input())
    try:
        tan = math.tan(angle)
        clear()
        print("The tangeante of " + str(angle) + " is " + str(tan))
        pause()
    except Exception as e:
        clear()
        print(bcolors.FAIL + str(e) + bcolors.END)
        pause()

def asin():
    clear()
    print(bcolors.WARNING + "Please enter the sinus. " + bcolors.END)
    sin = float(input())
    try:
        angle = math.asin(sin)
        clear()
        print("The angle of " + str(sin) + " is " + str(angle))
        pause()
    except Exception as e:
        clear()
        print(bcolors.FAIL + str(e) + bcolors.END)
        pause()

def acos():
    clear()
    print(bcolors.WARNING + "Please enter the cosinus. " + bcolors.END)
    cos = float(input())
    try:
        angle = math.acos(cos)
        clear()
        print("The angle of " + str(cos) + " is " + str(angle))
        pause()
    except Exception as e:
        clear()
        print(bcolors.FAIL + str(e) + bcolors.END)
        pause()

def atan():
    clear()
    print(bcolors.WARNING + "Please enter the tangeante. " + bcolors.END)
    tan = float(input())
    try:
        angle = math.atan(tan)
        clear()
        print("The angle of " + str(tan) + " is " + str(angle))
        pause()
    except Exception as e:
        clear()
        print(bcolors.FAIL + str(e) + bcolors.END)
        pause()

def hypothenus():
    clear()
    print(bcolors.WARNING + "Please enter the length of the first side. " + bcolors.END)
    fs = float(input())
    print(bcolors.WARNING + "Please enter the length of the second side. " + bcolors.END)
    ss = float(input())
    try:
        interval = (fs * fs) + (ss * ss)
        h = math.sqrt(interval)
        clear()
        print("The length of the hypothenus is: " + bcolors.EXTIT + str(h) + bcolors.END)
    except Exception as e:
        clear()
        print(bcolors.FAIL + str(e) + bcolors.END)
        pause()
        Pythagore()
    pause()
    Pythagore()

def adjacent():
    clear()
    print(bcolors.WARNING + "Please enter the length of the hypothenus. " + bcolors.END)
    h = float(input())
    print(bcolors.WARNING + "Please enter the length of the other adjacent side. " + bcolors.END)
    os = float(input())
    try:
        interval = (h * h) - (os * os)
        s = math.sqrt(interval)
        clear()
        print("The length of the other side is: " + bcolors.EXTIT + str(s) + bcolors.END)
    except ValueError:
        clear()
        print(bcolors.FAIL + "Hypothenus must be bigger than the other sides. " + bcolors.END)
        pause()
        Pythagore()
    pause()
    Pythagore()

main()
