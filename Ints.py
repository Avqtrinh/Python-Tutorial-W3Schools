x = 10.5
y = 5

print('x: '+str(x)+' y: '+str(y))

print('x+y no cast')
print(x+y)

print('x+y with cast')
print(int(x)+y)

print("useing del on y then printing y should throw an error")
del y
print y
