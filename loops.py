testList = ["a","b","c",]
print(testList)
for x in range (4,8):
	testList.append(x)
print(testList)


for x in testList:
	print("At Index ",testList.index(x)," element: " ,x)

x = False
count = 0
while x==False:
	if count == 3:
		x=True
	else:	
		count=count+1
print count
#this is a comment to force a diff and test new ssh key
