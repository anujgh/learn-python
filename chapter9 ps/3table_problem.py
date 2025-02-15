str_data = ''
for x in range(1,11):
  for i in range(2, 21):
    dgt = x * i
    if(len(str(dgt)) == 1):
      str_data = str_data + f"{dgt}   |   "
    elif (len(str(dgt)) == 2):
      str_data = str_data + f"{dgt}  |   "
    elif (len(str(dgt)) == 3):
      str_data = str_data + f"{dgt} |   "
    print(f"{x * i}   |   ", end="")
  str_data = str_data + '\n'
  print("")

print(str_data)

with open(r"chapter9 ps\tables.txt", "w") as f:
  f.write(str_data)
