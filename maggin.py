####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'maggin'

strategy_name = 'Pattern Recongnition'
strategy_description = 'Identify pattern that each player engages in.'

    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # This player always adapts then either colludes or betrays based on opponent's   historical pattern.
    return 'c'


#Idea: run your own historical simulation before you play against anyone. This will allow you to determine how your opponent will play and give the percentage chances. Then I will play according to what the best play is against my opponent, based on the data from the simulation.

