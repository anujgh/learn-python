# Arithmic Operators

a=2
b=3
c=a+b
print(c)


# Assignment Operators
a = 4-3 # Assign 4-3 to a
print(a)
b = 6 # Assign 6 into b
c += b # increment the value of c by b and assign it into variable
print(c)

c -= 3 # Decrement the value of c by 3
print(c)

p = 3
p *= 8 # multiply value of p by 8
print(p)

p /= 2
print(p) # devide the value of p / 2


# COMPARISON OPERATOR [always return boolean value]
d = 5<4
print(d)
x = 5 >= 5 # true
print(x)
y = 5 <= 5 # True
print(y)

z = 7!=8 # Treu
print(z)

o = 6==6 # True
p = 6==7 # False
print(o)
print(p)

# LOGICAL OPERATORS

t = True or False # Treu
print(t)

# Trouth table of or [ if any True in or then result will be Rrue]
print('True or False', True or False)
print('True or True', True  or True)
print('False or True', False or True)
print ( 'False or False', False or False)

# Truth table of and [ if any False in and then result will be False]
print('True and False', True and False)
print('True and True', True  and True)
print('False and True', False and True)
print ( 'False and False', False and False)

print ( not(True))
print(not(False))