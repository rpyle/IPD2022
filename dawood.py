team_name = 'dawood'
strategy_name = 'gradual collude '
strategy_description = 'collude first two runs, betray all others until opponent colludes'

#cooperates the first move, then begins to defect after two consecutive defections of its opponent. Returns to cooperation if opponent does not defect after the previous two moves

def move(my_history, their_history, my_score, their_score):
    '''Collude the very first round
    
     Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''

    if len(my_history)<=1: # collude first round
        return 'c'
    elif their_history[-1]=='b' and their_history[-2]=='b':
        return 'b' 
    else: 
      return 'c'

