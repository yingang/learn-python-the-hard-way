from sys import argv

script, file_name = argv

txt = open(file_name)

print "here is your file %r:" % file_name
print txt.read()

print "type the file name again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

