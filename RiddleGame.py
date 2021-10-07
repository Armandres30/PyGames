import itertools

SIZE = 10

def create_riddle():
    vowel = getRandomVowel()
    for i in SIZE:
        letters[i] = getRandomLetter()

def getRandomVowel():
    vowels = 'aeiou'
    return random.choice(vowels)

def getRandomLetter():
    letters='abcdefghijklmnopqrstuvwxyz'
    return random.choice(letters)
faes
def getRandomLetras():
    letras = 'abcdefghijklmnñopqrstuvwxyz'
    return random.choice(letras)

def getWords(vowel, letters):
    comb = getAllCombinations(vowel, letters)
    words = getRealWords(comb)
    return words

def getAllCombinations(vowel,letters):
    new_word = ''
    letters.append(vowel)
    list_comb=[]
    for L in range(0, len(letters) + 1)
        for subset in itertools.combinations(letters, L):
                list_comb.append(subset)
    return list_comb

def getRealWords(comb):
    real_list = []
    list = getListOfWords()
    for word in comb:
        if word in list:
            real_list.append(word)
    return real_list
