from array import array

# ai always plays the black side
inverted = False


# parse FEN into Array as specified in README.md
def parse(fen):
    fenlist = fen.split(" ")
    parsedlist = []
    position = fenlist[0]
    if (fenlist[1] == 'w'):
        position = invertPosition(position)
        global inverted
        inverted = True
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

    return parsedlist


def invertPosition(fen):
    fenlist = fen.split(" ")
    invertedPosition = ""
    for s in fenlist[0]:
        if (s.islower()):
            s = s.upper()
        elif (s.isupper()):
            s = s.lower()
        invertedPosition += s
    return invertedPosition
