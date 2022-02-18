####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import random

team_name = 'claytoon'
strategy_name = 'nah'
strategy_description = 'Collude at random unless betrayed'
def move(my_history, their_history, my_score, their_score):
    

  if 'b' in their_history[-3:]: 
        return 'b'
  elif random.random()<0.50: 
        return 'c'        
  else:
        return 'b'         
       