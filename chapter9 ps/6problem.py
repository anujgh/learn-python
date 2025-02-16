with open(r"chapter9 ps/log.txt") as f:
  data = f.read()
  if("Python" in data):
    print("Python exists!")
  else:
    print("Python not exists!")