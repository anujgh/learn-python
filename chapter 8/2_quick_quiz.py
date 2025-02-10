name = input('Who are you?')
def sayHello(name):
  print('Hello ',name,', How are u?')


sayHello(name) # type: ignore
sayHello('Ram')
sayHello('Hanuman')

# Function with return value

def avg(a,b,c):
  return (a+b+c)/3

print('average is : ',avg(3,4,3))

# Function with default value
def sum(a=1,b=2,c=3):
  return a+b+c

print('sum is: ',sum())
print(sum(33,44))