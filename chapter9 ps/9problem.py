with open(r"chapter9 ps/this.txt") as f:
  content = f.read()

with open(r"chapter9 ps/this_copy.txt") as fl:
  content2 = fl.read()

if(content == content2):
  print('Both files are identical')
else:
  print('Both files are diffrent')