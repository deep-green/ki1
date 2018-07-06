

# ai always plays the black side
inverted = False


# parse FEN into Array as specified in README.md
def parse(fen):
    global inverted
    fenlist = fen.split(" ")
    parsedlist = []
    position = fenlist[0]
    for s in position:
        if (s in ('1', '2', '3', '4', '5', '6', '7', '8')):
            i = int(s)
            for x in range(0, i):
                parsedlist.append(0)
        elif (s.islower()):
            if (s == 'p'):
                parsedlist.append(0.166)
            elif (s == 'r'):
                parsedlist.append(0.332)
            elif (s == 'n'):
                parsedlist.append(0.498)
            elif (s == 'b'):
                parsedlist.append(0.664)
            elif (s == 'q'):
                parsedlist.append(0.83)
            elif (s == 'k'):
                parsedlist.append(1)
        else:
            if (s == 'P'):
                parsedlist.append(0.083)
            elif (s == 'R'):
                parsedlist.append(0.249)
            elif (s == 'N'):
                parsedlist.append(0.415)
            elif (s == 'B'):
                parsedlist.append(0.581)
            elif (s == 'Q'):
                parsedlist.append(0.747)
            elif (s == 'K'):
                parsedlist.append(0.913)

    if (fenlist[1] == 'w'):
        parsedlist = invertFEN(parsedlist)
        inverted = True
    else:
        inverted = False
    return parsedlist


def invertFEN(parsedlist):
    invertedlist = parsedlist.reverse()
    for i in range(0, len(invertedlist)):
        if (invertedlist[i] == 0.083):
            invertedlist[i] = 0.166
        elif (invertedlist[i] == 0.249):
            invertedlist[i] = 0.332
        elif (invertedlist[i] == 0.415):
            invertedlist[i] = 0.498
        elif (invertedlist[i] == 0.581):
            invertedlist[i] = 0.664
        elif (invertedlist[i] == 0.747):
            invertedlist[i] = 0.83
        elif (invertedlist[i] == 0.913):
            invertedlist[i] = 1

        elif (invertedlist[i] == 0.166):
            invertedlist[i] = 0.083
        elif (invertedlist[i] == 0.332):
            invertedlist[i] = 0.249
        elif (invertedlist[i] == 0.498):
            invertedlist[i] = 0.415
        elif (invertedlist[i] == 0.664):
            invertedlist[i] = 0.581
        elif (invertedlist[i] == 0.83):
            invertedlist[i] = 0.747
        elif (invertedlist[i] == 1):
            invertedlist[i] = 0.913
    return invertedlist

def invertMove(move):
    templist = [8, 7, 6, 5, 4, 3, 2, 1]
    n1 = templist[int(move[1])-1]
    n2 = templist[int(move[3])-1]
    l1 = __invertstr(move[0])
    l2 = __invertstr(move[2])
    return l1 + str(n1) + l2 + str(n2)

def __invertstr(l):
    if (l == "a"):
        l = "h"
    elif (l == "b"):
        l = "g"
    elif (l == "c"):
        l = "f"
    elif (l == "d"):
        l = "e"
    elif (l == "e"):
        l = "d"
    elif (l == "f"):
        l = "c"
    elif (l == "g"):
        l = "b"
    elif (l == "h"):
        l = "a"
    return l
