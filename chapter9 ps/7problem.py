line_no = 1
with open(r"chapter9 ps/log.txt") as f:
  lines = f.readlines()
  for line in lines:
    if("Python" in line):
      print(f"Python exists in line no {line_no}!")
      break
    line_no += 1
  else:
    print("Python not exists!")