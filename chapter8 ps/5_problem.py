def show_star(n):
  for i in range(1,n+1):
    print('*'* ((n+1)-i), end='')
    print('')

n = int(input('Enter the no: '))
show_star(n)

def pattern(n):
  if(n==0):
    print('')
    return
  print('*'*n)
  pattern(n-1)

pattern(n)