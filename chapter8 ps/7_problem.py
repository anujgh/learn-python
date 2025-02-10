l = ['abc','pqr','xyz','lmn']

def rem(l, word):
  n = []
  for i in l:
    if not(i == word):
      n.append(i)
  return n

print(rem(l,'xyz'))
