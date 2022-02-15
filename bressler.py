####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E711'
strategy_name = 'Betray method'
strategy_description = 'If they betray every third round, collude on next, if not, betray them'
    
def move(my_history, their_history, my_score, their_score):
  if len(their_history)%3 == 'b':
    return 'c'
  else:
    return 'b'
    