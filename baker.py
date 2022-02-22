####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'baker'
strategy_name = 'Vengance'
strategy_description = 'Give em a dose of their own medicine. Always collude, unless a single person betrays. Then, always betray.'

def move(my_history, their_history, my_score, their_score):
  if 'b' in their_history[1:]: 
    return 'b'
  else:
    return 'c'