with open(r"chapter9 ps/paragraph.txt", "r") as f:
  data = f.read()
  print('data is: ',data)
  new_data = data.replace('donkey', 'VAISHAKHNANDAN (replaced to donkey)')
  # print('new data: ', new_data)
  # f.write(new_data)

with open(r"chapter9 ps/paragraph.txt", "w") as f:
  f.write(new_data)