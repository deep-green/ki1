def getMoves():
    list = []
    letters = ["a","b","c","d","e","f","g","h"]
    numbers = ["1","2","3","4","5","6","7","8"]
    templist = makelist(letters,numbers)
    list = makelist(templist,templist)
    return list

def makelist(li1,li2):
    retlist = []
    for val1 in li1:
        for val2 in li2:
            if(val1 != val2):
                retlist.append(val1+val2)
    return retlist

