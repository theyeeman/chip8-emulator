from msvcrt import getwch

def getKey():
    keystroke = getwch()
    if (keystroke == "1"):
        return("1")
    elif (keystroke == "2"):
        return("2")
    elif (keystroke == "3"):
        return("3")
    elif (keystroke == "4"):
        return("C")
    elif (keystroke == "q"):
        return("4")
    elif (keystroke == "w"):
        return("5")
    elif (keystroke == "e"):
        return("6")
    elif (keystroke == "r"):
        return("D")
    elif (keystroke == "a"):
        return("7")
    elif (keystroke == "s"):
        return("8")
    elif (keystroke == "d"):
        return("9")
    elif (keystroke == "f"):
        return("E")
    elif (keystroke == "z"):
        return("A")
    elif (keystroke == "x"):
        return("0")
    elif (keystroke == "c"):
        return("B")
    elif (keystroke == "v"):
        return("F")
    else:
        print("getKey: Invalid char")

def hexToInt(hexchar):
    if (hexchar == "0"):
        return 0
    elif (hexchar == "1"):
        return 1
    elif (hexchar == "2"):
        return 2
    elif (hexchar == "3"):
        return 3
    elif (hexchar == "4"):
        return 4
    elif (hexchar == "5"):
        return 5
    elif (hexchar == "6"):
        return 6
    elif (hexchar == "7"):
        return 7
    elif (hexchar == "8"):
        return 8
    elif (hexchar == "9"):
        return 9
    elif (hexchar == "A"):
        return 10
    elif (hexchar == "B"):
        return 11
    elif (hexchar == "C"):
        return 12
    elif (hexchar == "D"):
        return 13
    elif (hexchar == "E"):
        return 14
    elif (hexchar == "F"):
        return 15
    else:
        print("hexToInt: Invalid char")