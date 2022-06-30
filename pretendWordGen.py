import random

vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

#word size between 3 and 10 letters
#have no triple vowels or triple consonants
# TODO LATER:
# - add different chances for each letter e.g higher chance for E and lower for J

numWrds = int(input("how many words to generate: "))

for i in range(numWrds):
	wrd_sz = random.randint(3, 10)
	wrd = ""
	startVorC = random.randint(0,1) # 0 = vowel
	if startVorC == 0:
		wrd += vowels[random.randint(0,len(vowels)-1)]
	elif startVorC == 1:
		wrd += consonants[random.randint(0,len(consonants)-1)]

	for j in range(wrd_sz-1):
		if j >= 1:
			if wrd[j] in vowels and wrd[j-1] in vowels: # if the last 2 letters were vowels
				# we can't have a 3rd vowel so make next letter a consonant
				wrd += consonants[random.randint(0,len(consonants) - 1)]
			elif wrd[j] in consonants and wrd[j-1] in consonants: # if last 2 letters were consonants
				# no 3rd consonant for u
				wrd += vowels[random.randint(0,len(vowels)-1)]
			else:
				#1 in 2 chance of vowel
				if random.randint(0,1) == 0: # then yes repeat vowel
					wrd += str(vowels[random.randint(0,len(vowels)-1)])
				else:
					wrd += str(consonants[random.randint(0,len(consonants)-1)])
				
		else: # affects 2nd letter only
			#1 in 2 chance of vowel
			if random.randint(0,1) == 0: # then yes repeat vowel
				wrd += str(vowels[random.randint(0,len(vowels)-1)])
			else:
				wrd += str(consonants[random.randint(0,len(consonants)-1)])
			

	print("[", i+1, "]:  " + wrd)


