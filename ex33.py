def while_func(total):
	i = 0
	numbers = []
	while i < total:
		print "at the top i is %d" % i
		numbers.append(i)
		
		i += 1
		print "numbers now: ", numbers
		print "at the bottom i is %d" % i
	return numbers

numbers = while_func(6)
	
print "the numbers: "

for num in numbers:
	print num
