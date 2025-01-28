no = int(input('Enter the no'))

i = 2
status = 'no is prime'
while(i < no):
  print(no % i)
  if ( no % i == 0):
    status = 'no is not prime'
    break;
  i += 1

print (status)

print('---------------------')
# same thing using for loop

for i in range (2, no):
  if( no % i == 0):
    print('no is not prime')
    break
else:
  print('no is prime')