# functions:
# 1. len()
# 2. .endswith()
# 3. .startswith()
# 4. .capitalize()
# 5. .lower()
# 6. .upper()
# 7. .replace(-,-)
# 8. .find() // return index else -1 if not found
# 9. .split() // just like exclude in php
# 10. .join() // just like implode in php
# 11. .isdigit()
# 12. .isdecimal()
# 13. .isspace()
# 14. .title()
# 15. .casefold
# 16. .format
# 17. .count
# 18. .partition // Splits the string into three parts: the part before the separator, the separator itself, and the part after.
# 19. .encode
str = "Jay Siya Ram"
str2 = "jay siya ram"
str3 = 'JAY SIYA RAM'
print(len(str))
print(str.endswith('Ram'))
print(str.startswith('Jay'))
print(str2.capitalize())
print(str3.lower())
print(str2.upper())

str4 = 'Jay Shree Ram'
print(str4.replace('Shree', "Siya"))
print(str.find('Ram'))
print(str.find('rama'))
print(str4.split())
arr = ['Jay', 'Shree', 'Ram']
print("-".join(arr))

numStr = '12345'
decStr = '12.21'
print(numStr.isdigit())
print(numStr.isdecimal())

spaceStr =  "   "
print(spaceStr.isspace())

titleStr = "this is title"
print(titleStr.title())
print(str2.casefold())

str5 = 'Jay {} Ram'
print(str5.format('Siya'))
print(titleStr.count('t'))
print(titleStr.partition(" "))
print(str4.encode())