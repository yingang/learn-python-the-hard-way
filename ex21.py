def add(a, b):
	print "added %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "subtracting %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "multiplying %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "dividing %d / %d" % (a, b)
	return a / b

age = add(30, 5)
height = subtract(200, 21.5)
weight = multiply(75, 2)
iq = divide(10, 2)

print "age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)

print "here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "that becomes: ", what, "can you do it by hand?"

print "24 + 34 / 100 - 1023 = %d" % subtract(add(24, divide(34, 100)), 1023)

print "24 + 34.0 / 100 - 1023 = %d" % subtract(add(24, divide(34.0, 100)), 1023)
