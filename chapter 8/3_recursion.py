n = int(input('Enter the no: '))
def factorial(n):
  if(n == 0 or n == 1):
    return 1
  return n * factorial(n-1)
  
res = factorial(n)
print('factorial is : ',res)