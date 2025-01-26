a = set()
a.add(18)
a.add(18.0) # 18, 18.0 are same, take only one element in set.
a.add('18')
print(len(a))
print(a)