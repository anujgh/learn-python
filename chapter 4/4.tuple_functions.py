# 1. Creating a Tuple:          | a=(1,2,3,4,5,2,2,2,2,2,None,2)
# 2. Accessing Elements:        | first_element = my_tuple[0]
# 3. Counting Elements:         | count_of_twos = my_tuple.count(2)  # Count the number of times 2 appears
# 4. Finding Index:             | index_of_two = my_tuple.index(2)  # Find the index of the first occurrence of 2
# 5. Length of Tuple:           | length = len(my_tuple)  # Get the length of the tuple
# 6. Concatenating Tuples:      | combined = tuple1 + tuple2 # Concatenate two tuples
# 7. Slicing Tuples:            | sliced_tuple = my_tuple[1:3]  # Slicing a tuple from index 1 to 3 (exclusive)
# 8. Checking Membership:       | is_two_present = 2 in my_tuple  # Check if 2 is in the tuple
# 9. Iterating Through a Tuple: | for loop in tuple.
# 10. Unpacking Tuples:         | a, b, c = my_tuple # Unpacking the tuple into variables like distructring in javascript
# ----------------------------------------------------------------------------------------------------------------------

a=(1,2,3,4,5,2,2,2,2,2,None,2)
print(a.count(2))
first_el = a[0]
print(first_el)
indexOf2 = a.index(2)
print(indexOf2)
lengthOfTuple = len(a)
print(lengthOfTuple)

tupleFirst = (1,2,3,4,5,6,7)
tupleSecond = (6,5,4,3,2,1)
bothTuples = tupleFirst + tupleSecond
print('concatinated tuples: ',bothTuples)

slicedTuple = a[1:5]
print(slicedTuple)
skipedTuple = a[1:5:2]
print(skipedTuple)

is_2_present = 2 in a
print(is_2_present)

# loop of tuple
for x in a:
  print('item of tuple is: ',x)

abc = (3,2,1,4,3)
p,q,r,s,t = abc # distructing of tuple
print(abc)
print(p)
print(q)
print(r)
print(s)
print(t)
print(abc)