####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'amanda schoonover'
strategy_name = 'copycat'
strategy_description = 'collude first round. If you and your opponent answered the same on the previous round, you will reuse your answer in the next round. If you and your opponent answered differently in the previous round, you will use their answer from the previous round.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif my_history[-1] == their_history[-1]:
        return my_history[-1]
    elif my_history[-1] == "c" and their_history[-1] == "b":
      return their_history[-1]
    elif my_history[-1] == "b" and their_history[-1] == "c":
      return their_history[-1]