####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'alli'
strategy_name = 'collude unless betrayed'
strategy_description = 'always collude unless the other player betrays you twice'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # collude first round
        return 'c'
    elif my_history[-1]=='c' and their_history[-2]=='b':
        return 'b' # Betray if they were severely punished last time,
    else:
        return 'c' # otherwise collude.