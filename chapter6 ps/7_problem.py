name = "Xyz"
msg = input('Enter your text: ')

if(msg.startswith(name) or msg.startswith(name.lower())):
  print('You are talking about ', name)
else:
  print('You are not talking about ', name)