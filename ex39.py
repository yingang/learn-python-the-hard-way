states = {
	'Jiang Xi' : 'JX',
	'Hu Nan' : 'HN',
	'Shang Hai' : 'SH',
	'Jiang Su' : 'JS'
}

cities = {
	'JS' : 'Zhen Jiang',
	'JX' : 'Ping Xiang',
	'SH' : 'Shang Hai'
}

cities['HN'] = 'Chang Sha'

print '-' * 10
print "JX has: ", cities['JX']
print "HN has: ", cities['HN']

print '-' * 10
print "Jiang Xi's abbreviation is: ", states['Jiang Xi']
print "Hu Nan's abbreviation is: ", states['Hu Nan']

print '-' * 10
print "Jiang Xi has: ", cities[states['Jiang Xi']]

print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])
		
print '-' * 10
state = states.get('Shan Xi', None)

if not state:
	print "sorry, no Shan Xi."

city = cities.get('SX', 'Does not exist')
print "the city for the state 'SX' is: %s" % city
