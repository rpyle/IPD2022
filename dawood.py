team_name = 'dawood'
strategy_name = 'gradual collude '
strategy_description = 'collude first two runs, betray all others untill opponent colludes'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''

    if len(my_history)<=1: # collude first round
      return 'c'
    if len(my_history)<=2:
      return 'c'
    if len(my_history)<=3:
      return 'b'
    if len(my_history)<=4:
      return 'b'
    if len(my_history)<=5:
      return 'c'
    elif their_history[-1]=='b':
        return 'b' 
    else:
        return 'c'

#cooperates the two first moves, then begins to defect after two consecutive defections of its opponent. Returns to cooperation after two consecutive cooperations of its opponent.