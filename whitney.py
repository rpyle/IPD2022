team_name = 'W8'
strategy_name = 'ez win'
strategy_description = '''\
Check the last 3 moves and betray if I've been betrayed in any of them. Otherwise, collude 70% of the time.
'''

import random

def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history[-3:]: # If the other player has betrayed within last 3 rounds, 
        return 'b'               # Betray.
    else:
        if random.random()<0.30: # 30% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'         # but 70% of the time collude