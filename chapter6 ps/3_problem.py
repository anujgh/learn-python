a1 = 'Make a lot of mony'
a2 = 'buy now'
a3 = 'subscribe this'
a4 = 'click this'

str = input('Enter the text: ')

if(a1 in str or a2 in str or a3 in str or a4 in str):
  print('wront text')
else:
  print('Text is fine')