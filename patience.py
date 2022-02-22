team_name = 'Gavin'
strategy_name = 'Deceptively Nice'
strategy_description = 'Collude on the first few turns to get people to trust me then betray them every time.'
    
def move(my_history, their_history, my_score, their_score):
  while len(my_history) < 4:
    return 'c'
  return 'b'