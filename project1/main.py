# 1: stone
# 0: paper
# -1: sicser

import random

actions = {'stone':1, 'paper':0, 'sicser':-1}
actions_str = {1: 'stone', 0:'paper', -1: 'sicser'}
computer = random.choice([1,0,-1])
user = input('Enter your move: ')
user_move = actions[user]

print('Your action: ', user)
print('Computer move is : ',actions_str[computer])

if(( computer == 1 and user_move == 1 ) or 
  ( computer == 0 and user_move == 0 ) or 
  ( computer == -1 and user_move == -1 )):
    print('Draw')

elif ( ( computer == 1 and user_move == 0 ) or 
        ( computer == 0 and user_move == -1) or
        ( computer == -1 and user_move == 1) ) :
        print('You Wine!')
elif ( ( computer == 0 and user_move == 1 ) or 
        ( computer == -1 and user_move == 0) or
        ( computer == 1 and user_move == -1) ) :
        print('Cpmputer wine!')
else:
  print('Something went wrong!')