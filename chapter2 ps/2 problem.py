a = input("Enter a number: ")
print('Type of a is: ', type(a))
a = int(a)
b = 2
remender = a % b
if remender > 0:
    print(a, " is not devided by ", b)
else:
    print(a, " is devided by ", b)
