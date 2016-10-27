#!/usr/bin/env python3

import sys

""" Analysis of Alice in Wonderland text book 
with word count and more
TODO: add argument parsing (how many words to list)
TODO: how to use argument to choose reverse sorting or not
"""

try:
    counter = int(sys.argv[1])
except:
    print('You need to enter number of words to list')
    sys.exit()

book = "./alice_in_wonderland.txt"

def bookreader(bk):
    with open(bk) as b:
        bk_words = []
        for line in b.readlines():
            words = line.split(' ')
            for  word in words:
                for sign in [ '"', "'", ' ', "'s", ',', '.', ':', ";", 
                    '?', '!' ]:
                    word = word.replace(sign, '')
                word.lower      # not working fully?
                bk_words.append(word.strip())
    return bk_words

def wordcounter(wordlist):
    words = {}
    for word in wordlist:
        words[word] = words.get(word, 0) + 1
    return words

def header():
    print(5 * ' ' + 'Word ' + 10 * ' ' + 'Ocurrance')
    print(35 * '=')

def print_topX(words, counter=10, top=True):
    print('*** Printing top %s words ***\n' % str(counter))
    header()
    count = 0
    for w in sorted(words, key=words.get, reverse=top):    # sorting dict/hash
         if count < counter:
            print(5 * ' ' + w + (15 - len(w)) * ' ' + str(words[w]))
            count = count + 1

wordlist = bookreader(book)
words = wordcounter(wordlist)
print_topX(words, counter, True)
