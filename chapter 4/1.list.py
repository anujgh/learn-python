friends =  ['Apple', 5, True, 5.6, "Orrange", None, 'XYZ','abc']
print(friends)
print(friends[0])

name="Ajay Singh"
print(name[8])

# name[0] = "H" # invalid because string are immutable.
friends[0] = 'H' # unlike lists are mutable
print(friends)

# Slicing of list

print(friends[1:4])
print(friends[1:7:2])