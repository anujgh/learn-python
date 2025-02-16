with open(r"chapter9 ps/this.txt") as f:
  content = f.read()

with open(r"chapter9 ps/this_copy.txt", "w") as fl:
  fl.write(content)