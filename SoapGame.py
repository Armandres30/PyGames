
import string
import random

number_of_words = 10

size = 15 #number of rows and columns in soap table

def createSoapMatrix(size):

    soap = [ 0 for i in range(size)] for j in range(size) ]  #Initiate soap matrix with size number of rows and columns
    x, y = getRandomPos(size, soap)
    word = getRandomWord()
    insertWord(x, y, word, soap) #Insert word in random position

    while number_of_words > 0:
        insertConditionedWord(x, y, word, soap)



def getRandomPos(size, soap):

    x = random.randrange(0, size-1 )
    y = random.randrange(0, size-1 )

    if soap[x,y] != 0:
        insertConditionedWord()

def insertWord(x, y, word, soap):

    dir = random.randrange(0, 3)

    switch(dir)
    {
        case 0: 
            if len(soap) - len(word) - x >= 0:
                for letter in word:
                    soap[x, y] = letter
                    x++
        case 1: 
            if 1 + x - len(word) >= 0:
                for letter in word:
                    soap[x, y] = letter
                    x--
        case 2: 
            if len(soap) - len(word) - y >= 0:
                for letter in word:
                    soap[x, y] = letter
                    y++
        case 3: 
            if 1 + y - len(word) >= 0:
                for letter in word:
                    soap[x, y] = letter
                    y--
    }

def insertConditionedWord(x, y, soap, word_size):

    dir = random.randrange(0, 3)
    wordConditioned = [ 0 for i in range(word_size) ]

    switch(dir)
    {
        case 0: 
            if len(soap) - word_size - x >= 0:
                for i in word_size:
                    if soap[x + i][y] != 0:
                        wordConditioned[i] = soap[x + i, y]
                insertMatchingWord(wordConditioned, soap, dir)
        case 1: 
            if 1 + x - len(word) >= 0:
                for i in word_size:
                    if soap[x - i][y] != 0:
                        wordConditioned[i] = soap[x - i, y]
                insertMatchingWord(wordConditioned, soap, dir)
        case 2: 
            if len(soap) - len(word) - y >= 0:
                for i in word_size:
                    if soap[x][y + i] != 0:
                        wordConditioned[i] = soap[x, y + i]
                insertMatchingWord(wordConditioned, soap, dir)
        case 3: 
            if 1 + y - len(word) >= 0:
                for i in word_size:
                    if soap[x][y - i] != 0:
                        wordConditioned[i] = soap[x, y - i]
                insertMatchingWord(wordConditioned, soap, dir)
    }

def insertMatchingWord(wordConditioned, soap, dir):

    list = getListOfWords()

    for word in list:

        for i in len(wordConditioned):

            if wordConditioned != 0:

                if wordConditioned[i] != word[i]:
                    break

            if i == len(wordConditioned):

                switch(dir)
                {
                    case 0:
                        for letter in word:
                            soap[x, y] = letter
                            x++
                    case 1:
                        for letter in word:
                            soap[x, y] = letter
                            x--
                    case 2:
                        for letter in word:
                            soap[x, y] = letter
                            y++
                    case 3:
                        for letter in word:
                            soap[x, y] = letter
                            y--
                }

def fillSoap(soap):
    
    for i in len(soap):
        for j in len(soap):
            if soap[x, y] == 0:
                soap[x, y] = lower(random.choice()<string.ascii_letters)
        
def getListOfWords():
