directions = ('north', 'south', 'east', 'west')
verbs = ('go', 'kill', 'eat', 'goes', 'kills', 'eats', 'went', 'killed', 'ate')
stops = ('the', 'in', 'of', 'to', 'a', 'giant')
nouns = ('bear', 'princess', 'door', 'player')

def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def scan(input):
	words = input.split()
	results = []
	for word in words:
		if word in directions:
			results.append(('direction', word))
		elif word in verbs:
			results.append(('verb', word))
		elif word in stops:
			results.append(('stop', word))
		elif word in nouns:
			results.append(('noun', word))
		elif is_number(word):
			results.append(('number', int(word)))
		else:
			results.append(('error', word))
	return results