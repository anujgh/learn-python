words_list = ["bustling", "famous", "delicious", "freshly", "cozy"]

with open(r"chapter9 ps/para.txt", "r") as f:
  data = f.read()
  new_data = data
  for word in words_list:
    new_data = new_data.replace(word, 'XXXXX')

print(new_data)
with open(r"chapter9 ps/para.txt", "w") as fl:
  fl.write(new_data)