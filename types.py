print("python has types including:")
testInteger = 4
testFloat = 2.505
testLong=3000000000000
testComplex = 3+1j
testString = "TestTest"
testList = [1,2,3,'a',"b","c"]
testTup = ("a","tuple","is","an","immutable","list")


print("int")
print(testInteger)

print("float")
print(testFloat)

print("long")
print(testLong)

print("complex number")
print(testComplex)

print("string")
print(testString)

print("Bytes and byte array")

print("lists")
print("list:")
print(testList)
print("element 5: "+ testList[5])
testList[5] = 'z'
print("element 5 should now be z")
print("element 5: "+ testList[5])
del testList[5]
print("element 5 should now be gone")
print(testList)

print("Tuples")
for x in testTup:
	print(x)

print("Boolean")

print("sets s")

print("dictionaries d")

print("Class e")

print("Method M")

print("File f")
input()


