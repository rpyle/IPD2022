####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'moyer'
strategy_name = 'Sacrifice2'
strategy_description = ':)'
  
import random
round = 0
state = 0

def move(my_history, their_history, my_score, their_score):
  global round
  global state
  try:
    if(my_history[round - 1]):
      pass
  except IndexError:
    round = 0
    state = 0
  
  if round < 10:
    pass
  elif ((their_history[0] == 'c') and (their_history[1] == 'b') and (their_history[2] == 'c') and (their_history[3] == 'c') and (their_history[4] == 'b') and (their_history[5] == 'b') and (their_history[6] == 'b') and (their_history[7] == 'c') and (their_history[8] == 'b') and (their_history[9] == 'c')):
    state = 2
  #else:
    #state = 1

  #if round == 11:
  #  print(their_history[0] + their_history[1] + their_history[2] + their_history[3] + #their_history[4] + their_history[5] + their_history[6] + their_history[7] + #their_history[8] + their_history[9])

  #print(str(state) + ', ' + str(round))
  round = round + 1

  if (state == 1):
    pass
  elif (state == 2):
    return 'c'
  elif (state == 0):
    if (round == 1):
      return 'c'
    elif (round == 2):
      return 'b'
    elif (round == 3):
      return 'c'
    elif (round == 4):
      return 'c'
    elif (round == 5):
      return 'b'
    elif (round == 6):
      return 'b'
    elif (round == 7):
      return 'b'
    elif (round == 8):
      return 'c'
    elif (round == 9):
      return 'b'
    elif (round == 10):
      return 'c'
    elif (round > 10):
      return 'b'
    