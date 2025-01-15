friends =  ['Apple', 5, True, 5.6, "Orrange", None, 'XYZ','abc']
print(friends)
friends.append('Aag')
print(friends)

numbers = [2,1,23,32,23,43,435,11]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
res = numbers.insert(2,777)
print(numbers)
print(res)

popno = numbers.pop(3)
print(popno)
print(numbers)

numbers.remove(23)
print(numbers)