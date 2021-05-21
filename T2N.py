from time import sleep
import os
from os import name
from typing import Protocol

Alphabet = "abcdefghijklmnopqrstuvwxyz"

#Clear shit in ur terminal
def clear():
    #Windows
    if name == 'nt':
        _ = os.system('cls')

    #Linux, Unix & Mac
    else:
        _ = os.system('clear')

def Menu():
    global Answer,Locate
    clear()
    print ("Convert text to number and backwards \n")
    print ("c2n             convert text to numbers")
    print ("n2c             convert numbers to text")
    print ("exit            i don't think we need to explain about this one \n")
    Info = str(input (">>  ").lower())
    if Info ==("c2n"):
        Answer = ""
        Convert = input("Input text: ").lower()
        for Tracker in range(len(Convert)):
            if Convert[Tracker] in Alphabet:
                RealLocate = Alphabet.index(Convert[Tracker]) + 1
                Locate = str(RealLocate)
                Answer += Locate + "-"
            elif Convert[Tracker] == " ":
                pass
            else:
                Answer += Convert[Tracker] + "/"
        print ("The text coverted to:", Answer)
        exit (0)

    elif Info == ("n2c"):
            Answer = ""
            Locate = str()
            print ('Use "-" to separate each number. Use "/" to keep it as number. Others characters will be ignored.')
            Covert = input("Input number: ")
            Number = list(range(len(Covert)))
            Endash = list()
            Slash = list()
            for Tracker in range(len(Covert)):
                CheckNum = Covert[Tracker]
                CheckNum.isnumeric()
                if CheckNum.isdigit() == True:
                    if Tracker in Number:
                        Locate += str(Covert[Tracker])
                        if int(Locate) > len(Alphabet):
                            print ("ProcessCorrupted: Invalid string!")
                            exit(0)
                        
                else:
                    if Covert[Tracker] == "-":
                        Number.remove(Tracker)
                        Endash.append(Tracker)
                        StringLocate = int(Locate) - 1
                        Answer += Alphabet[StringLocate]
                        Locate = str()
                    elif Covert[Tracker] == "/":
                        Number.remove(Tracker)
                        Slash.append(Tracker)
                        Answer += str(Locate)
                        Locate = str()
                    else:
                        pass
            print ("The text is: ",Answer)
            exit(0)
    elif Info == "exit":
        exit(0)
    else:
        print ("SyntaxError: Unknow command")
        sleep (1)
        clear()
        Menu()

Menu()
