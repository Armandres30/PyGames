def createCrucigram(size):

    size = 13

    crucigram = [[ 0 for i in range(size)] for j in range(size)]

    word = getRandomWord()
    dir = randombool!!!!!!!!!!!!!!
    printWord(x, y, word, dir)
    listOfPositions = getRandomPosition(word)

    grater = 0

    for pos in listOfPositions:

        crossingWord = getRandomWordWithInitial(word[0])
        printWord(x, y, word, !dir)
        if len(crossingWord) > greater:
            greater = len(crossingWord)
    
    numberOfCrossingWords = greater/3 + 1
    
    y = 2

    while y < greater
        while true
            x = random.randrange(listOfPositions[-1])
            if x + 1 <= len(crucigram):
                break
        y += random.randrange(0, 2)

        for i in 3:
            conditions = getConditions(crucigram, x, y, dir ? len(crucigram) - x : len(crucigram) - y, dir)
            new_word = getRandomCrossingWord(conditions)

            if len(new_word) > greater2:
                greater2 = len(new_word)

            printWord(x, y, new_word, dir)
            while i<=3:
                x_new = random.randrange(listOfPositions[-1])
                if x_new > x - 3 or x_new < x + len(new_word):
                    i++
                else:
                    x = x_new
                    break
    
    x = 2

     while x < greater2
        while true
            y = random.randrange(listOfPositions[-1])
            if y + 1 <= len(crucigram):
                break
        x += random.randrange(0, 2)

        for i in 3:
            conditions = getConditions(crucigram, x, y, !dir ? len(crucigram) - x : len(crucigram) - y, !dir)
            new_word = getRandomCrossingWord(conditions)

            if len(new_word) > greater2:
                greater2 = len(new_word)
                
            printWord(x, y, new_word, dir)
            while i<=3:
                y_new = random.randrange(listOfPositions[-1])
                if y_new > y - 3 or y_new < y + len(new_word):
                    i++
                else:
                    y = y_new
                    break
        



def getConditions(crucigram, x, y, size, dir):

     if !dir:
            
            aux = x
            x = y
            y = aux

    condition = {}
    for pos in size:
        if crucigram[x + pos][y] != 0:
            conditions[pos] = crucigram[x + pos]
    return conditions

def getRandomPositions(word):

    list = []
    number_of_crossings = len(word)/3

    if number_of_crossings == 0:
        number_of_crossings = 1

    for i in number_of_crossings:

        keep = true

        while keep:

            pos = random.choice(range(0,len(word)))

            if list[] == [] or !(pos in list or pos-1 in list or pos+1 in list):
                list.pop(pos)
                keep = false

    return list

def getRandomWordWithInitial(letter):
    list = getListOfWords()
    while true:
        word = random.choice(list)
        if word[0] == letter:
            return word


def getRandomCrossingWord(conditions):
    list = getListOfWords()
    while true:
        word = random.choice(list)
        i=0
        for i in len(word):
            if i in conditions:
                if conditions[i] != word[i]:
                    break
            if i == len(word):
                return word
