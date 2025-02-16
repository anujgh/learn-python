with open(r"chapter9 ps/file_to_rename.txt","r") as f:
  content = f.read()
  

with open(r"chapter9 ps/renamed_file.txt", "w") as fl:
  fl.write(content)

