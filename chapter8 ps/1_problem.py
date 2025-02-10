a = 3
b = 2
c = 7

def gretest(a, b, c):
  gn = 0
  if(a > b):
    gn = a
  else:
    gn = a

  if(gn > c):
    return gn
  else:
    return c

no = gretest(a,b,c)

print(no)