print('and is a keyword') #see OperatorsAndOperands

print()
print('assert is a keyword')
print('assert 1==1 will pass')
assert(1==1)
print('assert 1==2 will throw an assertion error')
print('try is a keyword; except is a keyword : try( )  except: print( )')
try:assert(1==2)
except: print('assert(1==2) throws error so try --> except')

# this assert is has the same use idea as an assert from n-unit
print()
print('in is a keyword') #see OperatorsAndOperands

print()
print('del is a keyword')
a = 'hello world'
print('a is: '+a)
del a
print ('del a')
try:print('a is: '+a)
except:print("name 'a' is not defined error is thrown try --> except")
input()
#endinf file for now
