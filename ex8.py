formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, False)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
	"ni",
	"hao",
	"bu",
	"hao"
)
