team_name = 'Kauffman'
strategy_name = 'Whatever Works'
strategy_description = 'Betray unitl all parties have betrayed and then switch tactics'
    
def move(my_history, their_history, my_score, their_score):
   
    if len(my_history)==0: 
        return 'b'
    elif my_history[-1]=='b':
      return 'b'

    elif my_history[-1]=='b' and their_history[-1]=='b':
        return 'c' # Betray if they were severely punished last time,
    else:
        return 'b' # otherwise collude.