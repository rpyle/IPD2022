####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'mucher'
strategy_name = 'Betray but collude after they do'
strategy_description = '''\
Deafault to betray, only collude if they colluded last round.'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; betray.
        return 'b'
        
    elif my_history[-1]=='b' and their_history[-1]=='b':
        return 'b' # Betray after severe punishment, opponent will be scared and will likely collude in fear of another severe punishment,
    else:
        return 'c' # Collude if they colluded last round.