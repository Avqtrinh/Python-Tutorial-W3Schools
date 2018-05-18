from pathlib import Path
testString =  "hello world"
my_file = Path("/testFile.txt")
try:
	file =  open("testFile.txt","rw")
else: 
	with open("testFile.txt","rw") as file:
		file.write(testString) 

print("this program prints to a document the line: " + testString)

