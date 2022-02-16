team_name = 'support_dawood'
strategy_name = 'support dawood'
strategy_description = 'betray everyone but dawood'
    
def move(my_history, their_history, my_score, their_score):

    '''betray everyone besides dawood.

    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''

    if len(their_history)<=1 == 'c' and len(their_history)<=2 == 'c' and len(their_history)<=3 == 'b' and len(their_history)<=4 == 'b' and len(their_history)<=5 == 'c':
      return 'c'
    else: 
      return 'b'