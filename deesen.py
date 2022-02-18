####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'Deesen'
strategy_name = 'Betray or collude w Homie'
strategy_description = 'betray and collude based on other dudes move'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # This player always colludes.
    if 'b' in their_history[-4:]: # player has betrayed within last 4 rounds,
        return 'b'               # Betray.
    else:
        if random.random()<0.50: # 50 percent of the other rounds
          return 'c'               #collude w the boys
    