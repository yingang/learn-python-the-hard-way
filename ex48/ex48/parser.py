class ParserError(Exception):
	pass
	
class Sentence(object):
	def __init__(self, subj, verb, obj):
		self.subj = subj[1]
		self.verb = verb[1]
		self.obj = obj[1]

def peek(word_list):
	if word_list:
		word = word_list[0]
#		print '[peek]', word
		return word[0]
	else:
		return None
		
def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)
		
#		print '[match]', word
		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None
		
def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)
		
def parse_verb(word_list):
	skip(word_list, 'stop')
	
	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError("Expected a verb next.")
		
def parse_object(word_list):
	skip(word_list, 'stop')
	next = peek(word_list)
	
	if next == 'noun':
		return match(word_list, 'noun')
	if next == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or direction next.")
		
def parse_subject(word_list, subj):
	verb = parse_verb(word_list)
	obj = parse_object(word_list)
	
#	print 'subj=', subj, ', verb=', verb, ', obj=', obj
	return Sentence(subj, verb, obj)
	
def parse_sentence(word_list):
	skip(word_list, 'stop')
	
	start = peek(word_list)
	
	if start == 'noun':
		subj = match(word_list, 'noun')
#		print 'subj=', subj
		return parse_subject(word_list, subj)
	elif start == 'verb':
		return parse_subject(word_list, ('noun', 'player'))
	else:
		raise ParserError("Must start with subject, object, or verb not: %s" % start)
		