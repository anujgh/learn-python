# PROPERTIES OF SETS
# 1. Sets are unordered [ Element order dosn't matter.]
# 2. Sets are unindexed [ Can not access by index. ]
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.
# 
# Sets functions.
# len()
# remove()
# pop() : It pops rendom value from set.
# clear()
# union() : Return new set with values of both sets.
# intersection(): Return a set of items which contains only item in both sets.
# issubset()
# issuperset()
# ----------------------------------------------------------------------------


a_set = {1,'one',2,'two',3,'three',3,3,3,3,2,2,1,1}
print(a_set)
print(type(a_set))
a_set.add('one more')
print(a_set)
print(type(a_set))
a_set.remove('two')
print(a_set)
print('size of set: ',len(a_set))
pop_item = a_set.pop()
print('after pop : ',a_set)
print('poped Item: ', pop_item)
b_set = {1,4,2,3,99,'three'}
union_set = a_set.union(b_set)
print('union set : ', union_set)
intersect_set = a_set.intersection(b_set)
print('intersection set: ', intersect_set)
intersect_set.clear()
print('after clear intersection_set: ', intersect_set)
next_popel = a_set.pop()
print('after next pop: ', next_popel, a_set)

a = {1,2,3,4,5,6}
b = {5,6,7,8}
print(a-b)
child_set = {2,3}
print(child_set.issubset(a))
print(a.issuperset(child_set))