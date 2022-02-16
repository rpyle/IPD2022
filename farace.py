

team_name = 'adriana'
strategy_name = 'come out on top'
strategy_description = '''\
Check the last 3 moves and betray if I've been betrayed in any of those past 3 moves. Otherwise, collude 97% of the time. This stategy allows me to betray only if I have been betrayed and give them the oppenent mostly the benefit of the doubt.
'''

import random
    
def move(my_history, their_history, my_score, their_score):
  

  if 'b' in their_history[-3:]: # If the other player has betrayed within last 3 rounds, 
   return 'b'               # Betray.
  else:
    if random.random()<0.3: # 3% of the other rounds
     return 'b'         # Betray
    else:
      return 'c'         # but 97% of the time collude
    