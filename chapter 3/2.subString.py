str = "Hello World"
#  H   e   l   l   o       W   o   r   l   d
#  0   1   2   3   4   5   6   7   8   9   10
# -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
subStr = str[2:-3]
print(subStr)
print(str[-3:-1])
print(str[:4]) # same as str[0:4]
print(str[1:]) # same as str[1:10]
# print(str[-1,-4]) This is invalid, because left index must be less then right
