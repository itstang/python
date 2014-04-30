import argparse
import string

parser = argparse.ArgumentParser()
parser.add_argument('Rack', help='The letters you own')

arg = parser.parse_args()
arg = vars(arg)['Rack']
arg = arg.lower()

rack = []

for letter in arg:
	rack.append(letter)

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

dictFile = open('sowpods.txt', 'r')
dict = []
validWord = []

for line in dictFile:
	dict.append(line.lower().strip())

for dictWord in dict:
	checkWord = list(dictWord)
	tempRack = list(rack)
	for checkLetter in dictWord:
		#for letter in dictWord:	
		if checkLetter in tempRack:
			checkWord.remove(checkLetter)
			tempRack.remove(checkLetter)
		if len(checkWord) == 0:
			validWord.append(dictWord)

wordList = {}

for valid in validWord:
	score = 0
	for letter in valid:
		score += scores[letter]

	wordList[valid] = score

sortList = sorted(wordList.items(), key=lambda x: x[1], reverse=True)

for key, value in sortList:
	print(str(value) + " " + key)