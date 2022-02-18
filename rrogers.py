####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Rogers'
strategy_name = 'Backstab only if they do'
strategy_description = 'Collude with everyone except for when last round they colluded and/or I betrayed.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round: collude
        return 'c'
    else:
        # If in the last round they betrayed me, betray them
      
        
        # Reference last round
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]
                    
        # Look at rounds before that one
        for round in range(len(my_history)-1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            # If one matches
            if (prior_round_me >= recent_round_me) and \
                    (prior_round_them >= recent_round_them):
                return their_history[round]
        # No match found
        if my_history[-1]=='c' and their_history[-1]=='b':
            return 'c' # If I colluded last time and they betrayed last time, collude
        else:
            return 'b' # Otherwise betray
    