f = open(r"chapter9 ps\file.txt")
data = f.read()

if("Hello" in data):
  print('Hello present in data')
else:
  print('Hello is not present in data')
f.close()