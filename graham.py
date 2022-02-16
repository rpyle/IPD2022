####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####


team_name = 'step_teo'

strategy_name = 'Always collude unless betrayed within last 10 rounds.'
strategy_description = '''\
Check the last 10 moves and betray if I've been betrayed in any of them. Otherwise, collude 100% of the time.
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


    if 'b' in their_history[-10:]: # If the other player has betrayed within last round, 

        return 'b'               # Betray.
    else:
        if random.random()<0.1: 
            return 'b'         # Betray
        else:
            return 'c'         #collude

    
    
    