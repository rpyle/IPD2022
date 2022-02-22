####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'bacon'
strategy_name = 'History'
strategy_description = '''\
Use the other players history to fuel my turn.'''
    
def move(my_history, their_history, my_score, their_score):

  if len(my_history)==0: # It's the first round: collude
   return 'c'
  else:
    if my_history[-1]=='c' and their_history[-1]=='b':
      return 'b' # Betray if they were severely punished last time
    if my_history[-1] == 'c' and their_history[-1] == 'c' :
      return 'c'
    if my_history[-1] == 'b' and their_history[-1] == 'c':
      return 'c'
    if my_history[-1] == 'b' and their_history[-1] == 'b':
      return 'b'