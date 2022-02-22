####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'shotton'
strategy_name = 'betray'
strategy_description = 'betray most the time'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: 
      return 'b' 
    elif their_history[-1]=='c' and their_history[-2]=='c':
      return 'c'
    else:
      return 'b'
    
