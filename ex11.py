print "what's your name?"
name = raw_input()

print "how old are you?"
age = int(raw_input())

print "how tall are you?"
height = raw_input()

print "how much do you weight?"
weight = raw_input()

print "oh, i see. you are %r. you are %r years old, %r tall and %r heavy" % (
	name, age, height, weight
)

