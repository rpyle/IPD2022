team_name = 'roxy'
strategy_name = 'betray but sympathize'
strategy_description = 'betray unless they collude then collude'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; collude.
        return 'b'
    elif my_history[-1]=='b' and their_history[-1]=='c':
        return 'c' # Betray if they were severely punished last time,
    else:
        return 'b' # otherwise collude.