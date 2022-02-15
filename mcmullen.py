####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Zacharie'
strategy_name = 'Betray then Forgive'
strategy_description = 'Betray in the first and second round. If opponent colludes and then betrays, next round collude. Otherwise betray.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if (len(my_history) <= 1): # If it is the 1st or 2nd round
      return "b" # Betray
    else:
      if (their_history[-1] == "b") and (their_history[-2] == "c"): # If they colluded and then betrayed me
        return "c" # Forgive them and collude
      else:
        return "b" # Otherwise betray