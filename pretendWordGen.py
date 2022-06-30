import random

vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']


#word size between 3 and 10 letters
#have no triple vowels or triple consonants

# TODO LATER ---- DONE NOW:
# - add different chances for each letter e.g higher chance for E and lower for J

def ReturnVowel():
        # e = 12.49 | 13
        # a = 8.04  | 8
        # i = 7.57  | 8
        # o = 7.64  | 8
        # u = 2.73  | 3

        # chance of E = 13 / 40
        # chance of A, I, O = 8 / 40   = 1/5
        # chance of U = 3 / 40

        if random.randint(1,5) == 2: # 2 has a 1/5 chance
                return 'a'
        elif random.randint(1,5) == 2: # 2 has a 1/5 chance
                return 'i'
        elif random.randint(1,5) == 2: # 2 has a 1/5 chance
                return 'o'
        elif random.randint(1,40) <= 12: # has an unrounded chance of 12.49 so if no value matches selection, then default should be E
                return 'e'
        elif random.randint(1,40) <= 3: # 3/40 chance
                return 'u'
        else:
                return 'e'

def ReturnConsonant():
        # total chance of a consonant: 65 (although letters such as X, J, Q and Z are below 0.5%, I still rounded to 1
        if random.randint(1,65) <= 9: # 9/65 chance
                return 't'
        elif random.randint(1,65) <= 7:
                return 'n'
        elif random.randint(1,65) <= 7:
                return 's'
        elif random.randint(1,65) <= 6:
                return 'r'
        elif random.randint(1,65) <= 5:
                return 'h'
        elif random.randint(1,65) <= 4:
                return 'l'
        elif random.randint(1,65) <= 4:
                return 'd'
        elif random.randint(1,65) <= 3:
                return 'c'
        elif random.randint(1,65) <= 3:
                return 'm'
        elif random.randint(1,65) <= 2:
                return 'f'
        elif random.randint(1,65) <= 2:
                return 'p'
        elif random.randint(1,65) <= 2:
                return 'g'
        elif random.randint(1,65) <= 2:
                return 'w'
        elif random.randint(1,65) <= 2:
                return 'y'
        elif random.randint(1,65) == 1: # gets rounded down from 1.48 to 1 so should have a higher chance,
                                        # so in the rare case of no number matching one of these if statements,
                                        # the default return value for consonants will be B
                return 'b'
        elif random.randint(1,65) == 1:
                return 'v'
        elif random.randint(1,65) == 1:
                return 'k'
        elif random.randint(1,65) == 1:
                return 'x'
        elif random.randint(1,65) == 1:
                return 'j'
        elif random.randint(1,65) == 1:
                return 'q'
        elif random.randint(1,65) == 1:
                return 'z'
        else:
                return 'b'



numWrds = int(input("how many words to generate: "))

for i in range(numWrds):
        wrd_sz = random.randint(3, 10)
        wrd = ""
        startVorC = random.randint(0,1) # 0 = vowel
        if startVorC == 0:
                wrd += ReturnVowel() #vowels[random.randint(0,len(vowels)-1)]
        elif startVorC == 1:
                wrd += ReturnConsonant() #consonants[random.randint(0,len(consonants)-1)]

        for j in range(wrd_sz-1):
                if j >= 1:
                        if wrd[j] in vowels and wrd[j-1] in vowels: # if the last 2 letters were vowels
                                # we can't have a 3rd vowel so make next letter a consonant
                                wrd += ReturnConsonant() #consonants[random.randint(0,len(consonants) - 1)]
                        elif wrd[j] in consonants and wrd[j-1] in consonants: # if last 2 letters were consonants
                                # no 3rd consonant for u
                                wrd += ReturnVowel() #vowels[random.randint(0,len(vowels)-1)]
                        else:
                                #1 in 2 chance of vowel
                                if random.randint(0,1) == 0: # then yes repeat vowel
                                        wrd += ReturnVowel() #str(vowels[random.randint(0,len(vowels)-1)])
                                else:
                                        wrd += ReturnConsonant() #str(consonants[random.randint(0,len(consonants)-1)])

                else: # affects 2nd letter only
                        #1 in 2 chance of vowel
                        if random.randint(0,1) == 0: # then yes repeat vowel
                                wrd += ReturnVowel() #str(vowels[random.randint(0,len(vowels)-1)])
                        else:
                                wrd += ReturnConsonant() #str(consonants[random.randint(0,len(consonants)-1)])


        print("[", i+1, "]:  " + wrd)
