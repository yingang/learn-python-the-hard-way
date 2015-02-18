from nose.tools import *
from ex48 import lexicon
from ex48 import parser

def test_sentense():
	sentence = parser.parse_sentence(
		lexicon.scan("bear eats princess"))
	assert_equal(sentence.subj, 'bear')
	assert_equal(sentence.verb, 'eats')
	assert_equal(sentence.obj, 'princess')
	
def test_sentense_with_stops():
	sentence = parser.parse_sentence(
		lexicon.scan("a giant bear goes to the east"))
	assert_equal(sentence.subj, 'bear')
	assert_equal(sentence.verb, 'goes')
	assert_equal(sentence.obj, 'east')

def test_default_subject():
	sentence = parser.parse_sentence(
		lexicon.scan("kill bear"))
	assert_equal(sentence.subj, 'player')
	assert_equal(sentence.verb, 'kill')
	assert_equal(sentence.obj, 'bear')

def test_error_only_verb():
	assert_raises(parser.ParserError,
		parser.parse_sentence,
		lexicon.scan("kill"))
	
def test_error_only_subject():
	assert_raises(parser.ParserError,
		parser.parse_sentence,
		lexicon.scan("princess"))

def test_error_no_verb():
	assert_raises(parser.ParserError,
		parser.parse_sentence,
		lexicon.scan("princess bear"))

def test_error_no_object():
	assert_raises(parser.ParserError,
		parser.parse_sentence,
		lexicon.scan("princess kills"))
	
def test_error_bad_subject():
	assert_raises(parser.ParserError,
		parser.parse_sentence,
		lexicon.scan("prince killed the bear"))