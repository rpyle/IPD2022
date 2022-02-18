####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

#Idea: run your own historical simulation before you play against anyone. This will allow you to determine how your opponent will play and give the percentage chances. Then I will play according to what the best play is against my opponent, based on the data from the simulation.

team_name = 'maggin'

strategy_name = 'Pattern Recognition'
strategy_description = 'Identify pattern that each player engages in.'


    # This player always adapts then either colludes or betrays based on opponent's   historical pattern.

def data_collection(my_history, their_history, my_score, their_score):

      if len(my_history)==0: 
          return 'b'
      else:
          # View last round
          recent_round_them = their_history[-2]
          recent_round_me = my_history[-2]
        
          # Examine rounds before that one
          for round in range(len(my_history)-1):
              prior_round_them = their_history[round]
              prior_round_me = my_history[round]
              # If one matches
              if (prior_round_me == recent_round_me) and \
                      (prior_round_them == recent_round_them):
                  return their_history[round]
          # No match found
          if my_history[-1]=='c' and their_history[-1]=='b':
              return 'b'
            





