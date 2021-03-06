####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Logan'
strategy_name = 'Adapt and Overcome'
strategy_description = '''\
Check the last move, if the other player colluded then I collude, and if the other player betrayed me, then I betray.
'''

import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''

    if 'c' in their_history[-1:]: # If the other player has betrayed within last 10 rounds, 
        return 'c'               # Betray.
    else:
        if random.random()<0.95: # 70% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'         # but 5% of the time collude
    if 'b' in their_history[-1:]: # If the other player has betrayed within last 10 rounds, 
        return 'b'               # Betray.
    else:
        if random.random()<0.95: # 70% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'         # but 5% of the time collude
    