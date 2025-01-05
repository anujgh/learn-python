str = "Hello World"
#  H   e   l   l   o       W   o   r   l   d
#  0   1   2   3   4   5   6   7   8   9   10
# -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
print(str[1:6:2])  # op: 'el '
print(str[1:9:3])  # op: 'eoo'
print(str[0:7:3])  # op: 'HlW'

# Explain : print(str[0:7:3])  # op: 'HlW'
# -> take str[0:7] = "Hello Wo"
# -> skip 3 letters = "HlW"