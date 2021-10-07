# -*- coding: utf-8 -*-
"""
Unsort and Sort Word Game
"""

def unsort_word(word):
    new_word=''
    list = [ i for i in range(0,len(word)) ]
    while list != []:
        pos = random.choice(range(0,len(list)))
        element = list[pos]
        new_word+=word[element]
        list.pop(pos)
    return new_word

score=0

word = get_random_word()

dict = {}

for i in range(0,10):
    dict.update(i:[word,unsort_word(word)])
    
for i in range(0,len(dict)):
    print_word(dict[1])
    given_word = get_word(word)
    if given_word == dict[0]:
        score++;

def print_word():
    

def get_random_word():
    

def create_crucigram():
    word = get_random_word()
    print_word(0,0,bool(random.getrandbits(1)))
    list_of_pos = get_random_pos(word)
    for pos in list_of_pos:
        get_random_word_with_init(letter)
        print_word(pos,0,true)
