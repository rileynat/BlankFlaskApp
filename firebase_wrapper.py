import requests
import json


def getPuzzle():
	return (['fish', 'woman'], 'mermaid');


def addPuzzle(clues, answer):
	if len(clues) > 0:
		result = requests.put('https://https://pictaword.firebaseio.com/' + answer + '.json', data=json.dumps(clues));