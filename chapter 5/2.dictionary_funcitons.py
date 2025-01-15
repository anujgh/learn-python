# 1. dic.items()
# 2. dic.keys()
# 3. dic.values()
# 4. dic.update()
# 5. dic.get()
# 6. Checking for Key Existence: | is_name_in_dict = "name" in my_dict  # Check if the key "name" exists in the dictionary
# 7. Adding or Updating an Item: | my_dict["email"] = "alice@example.com"  # Add a new key-value pair or update an existing key
# 8. Removing an Item:           | removed_item = my_dict.pop("age")  # Remove the key "age" and get its value
# 9. dic.clear()                 | my_dict.clear()  # Remove all items from the dictionary
# 10. for loop in dictionary


dic = {
  'name':'Ram',
  'age': 23,
  'no':7
}

dic.update({'no':100})

print(dic.get('name'))

# -----------------------------------------------------
# print(dic.get('not_exists_key')) # return None
# print(dic['not_exists_key']) # return error
# ----------------------------------------------------
print(dic.items())
print(dic.keys())
print(dic.values())

print(type(dic.items()))
print(type(dic.keys()))
print(type(dic.values()))
print(dic.pop('no'))
print(dic)
print(dic.popitem())
for key, value in dic.items():
  print(key, value)

dic.clear()
print(dic)