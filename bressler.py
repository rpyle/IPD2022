####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Cameron'
strategy_name = 'Betray Method'
strategy_description = 'If they betray on third round, collude on next, if not, betray them'
    
def move(my_history, their_history, my_score, their_score):
  if 'b' in their_history[3:]: #If player betrays on third round, collude
    return 'c'
  else:
    return 'b'
    