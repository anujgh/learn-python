n = int(input('Enter the no: '))

def do_sum(n):
  if(n == 0):
    return 0
  return n + do_sum(n-1)

print(do_sum(n))