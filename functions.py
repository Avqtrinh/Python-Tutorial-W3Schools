def test(numIn):
	x = numIn%2
	if x == 0:
		return "even"
	else:
		return "odd"

print test(input("input a number"))

