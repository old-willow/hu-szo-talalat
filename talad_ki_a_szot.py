#! /usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys, os

#letter = u'aáeéiíoóöőuúüűAÁEÉÍOÓÖŐUÚÜŰ'
twoLetters = [u'sz', u'zs', u'gy',
              u'ty', u'ly', u'ny',
              u'dz', u'ggy', u'ssz',
              u'cs', u'tty', u'dzs']
positions = []

def open_vocabulary(filename):
    f = open(filename, 'r')
    words = f.readlines()
    f.close()
    return words


def choose_word(list):
    return random.choice(list)


def find_letter(secretWord, letter, resultList):
    global positions
    letterLen = len(letter)

    if letterLen == 1: # If we have letter with only one char.
        if not positions: # First lookup for letter.
            pos = secretWord.find(letter)
            currPos = pos + 1
        elif positions: # We allready have at least one position saved.
            if positions[-1] == 0: # If the previous letter was on a first place.
                currPos = secretWord.find(letter) + 1
                pos = currPos
            else:
                currPos = secretWord.find(letter) + 1
                pos = positions[-1] + currPos

        if pos != -1:
            positions.append(pos)
        #print pos,

        if letter in secretWord[currPos:]:
            find_letter(secretWord[currPos:], letter, resultList)

        #print in appropriate position/s the corresponding letter/s.
        for p in positions:
            resultList[p] = letter

    elif letterLen > 1: # If we have letter with more then one char.
        if not positions: # First lookup for letter.
            pos = secretWord.find(letter)
            currPos = pos + letterLen
        elif positions:
            if positions[-1] == 0: # If the previous letter was on a first place.
                pos = secretWord.find(letter) + letterLen
                currPos = pos
            else:
                currPos = secretWord.find(letter) + letterLen
                pos = currPos + positions[-1]

        if pos != -1:
            positions.append(pos)

        if letter in secretWord[currPos:]:
            find_letter(secretWord[currPos:], letter, resultList)

        #print in appropriate position/s the corresponding letter/s
        for p in positions:
            for ip in range(letterLen): # sequently put each char in it's appropriate place.
                resultList[p+ip] = letter[ip]

    #print '\n', 'before reset:', positions
    positions = [] # Reset the positions for new letter.
    #print 'after reset:', positions


def main():
    os.system('clear')
    words = open_vocabulary('hu_words')

    while True: # The main game loop.
        secretWord = choose_word(words)
        secretWord = secretWord[:-1] # Delete '\n' character.
        #secretWord = 'fölöslegesség'
        #secretWord = 'amalackamalacka'
        #secretWord = 'nyaranyvalaganyevalyaanyanya'
        #secretWord = 'madzagocska'
        
        #print secretWord
        sw = secretWord.decode('utf-8')

        # Decode the unicode string for appropriate length
        secretLen = len(secretWord.decode('utf-8'))
        resultList = []
        for i in range(secretLen):
            resultList.append('_')

        print(u'A titkos szónak ' + str(secretLen) + u' betüje van.')

        max = False
        # If the word is long then have more possibilities
        if secretLen < 6:
            counter = 8
            finalCounter = 5
        elif secretLen >= 6 and secretLen < 11:
            counter = 10
            finalCounter = 7
        elif secretLen >= 11 and secretLen < 16:
            counter = 15
            finalCounter = 8
        elif secretLen >= 16:
            counter = 15
            finalCounter = 10

        print unicode(counter) + u' tippelhetsz.'
        print(u'Vagy beírhatod az eredményt ha biztos vagy benne.')

        collectedLetters = []

        # Infinite loop for actual letter search.
        while True:
            #print secretWord
            if not max:
                print u'A hátramaradt tippek száma: ' + unicode(counter)
                letter = raw_input('Tippelj egy betüt/szót: ')
            elif max:
                letter = raw_input('Találd ki a szót: ')
                finalCounter -= 1

            if letter:
                letter = letter.decode('utf-8')

                if max:
                    if letter == sw:
                        print(u'Gratulálok, eltaláltad a szót!')
                        break
                    elif finalCounter != 0:
                        print(u'Még csak ' + unicode(finalCounter) + u' tippelhetsz.')
                    elif finalCounter == 0:
                        print('Sajnos nem találtad el.')
                        print u'A titkos szó: ',  secretWord
                        break

                elif sw == ''.join(resultList) or letter == sw:
                    print(u'Gratulálok, eltaláltad a szót!')
                    break

                # If letter is 2 or 3 length.
                elif len(letter) == 2 or len(letter) == 3:
                    if letter in collectedLetters:
                        print(u'Ezt a betűt már kérdezted!')

                    elif letter not in twoLetters:
                        print(u'Na, na!! Csak egy betűt lehet.')

                        for i in resultList:
                            print i,

                        print('\n')

                    else:
                        os.system('clear')
                        if counter != 0:
                            counter -= 1
                        collectedLetters.append(letter.encode('utf-8'))
                        print(collectedLetters)
                        find_letter(sw, letter, resultList)

                        for i in resultList:
                            print i,

                        if sw == ''.join(resultList):
                            print(u'\nGratulálok, eltaláltad a szót!')
                            break

                        if counter == 0:
                            max = True
                            print(u'\nElérted a megengedet tippek számát.')
                            print(u'Most már csak találd ki a szót.')

                        print('\n')

                        if letter in collectedLetters:
                            print(u'Ezt a betűt már kérdezted!')

                elif letter not in collectedLetters:
                    os.system('clear')
                    if counter != 0:
                        counter -= 1
                    collectedLetters.append(letter.decode('utf-8'))
                    print(collectedLetters)
                    find_letter(sw, letter, resultList)

                    for i in resultList:
                        print i,

                    if sw == ''.join(resultList):
                        print(u'\nGratulálok, eltaláltad a szót!')
                        break

                    if counter == 0:
                        max = True
                        print(u'\nElérted a megengedet tippek számát.')
                        print(u'Most már csak találd ki a szót.')

                    print('\n')

                elif letter in collectedLetters:
                    print(u'Ezt a betűt már kérdezted!')


            else:
                continue # If you hit enter with an empty input.

        # Infinte loop for asking to play again.
        while True:
            choice = raw_input('Akarsz még játszani? ')
            if choice == 'i':
                playAgain = True
                os.system('clear')
                break
            elif choice == 'n':
                print(u'Szia!')
                sys.exit(0)
            else:
                print(u'Csak \'igen/nem\' [i/n], kérem.')


if __name__ == '__main__':
    main()
