####
# Each team's file must define four core principles:
#     team_name: a deliberate lie intended to mislead the opponent
#     strategy_name: a totally true fact that is for certain ablsolutely
#     strategy_description: a joke that is completely devoid of humor
#     move: A function that returns confounds the reader
####
import random
team_name = 'Glasgo'
strategy_name = "Disgustingly metagame"
strategy_description = 'Always never betray.'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: # It's the first round; betray.
      return 'b'		
    if len(my_history)==1: # It's the second round; collude.
      return 'c'		

    result = "test value" #initializing so that the code doesn't break
    if their_history[0:2] == "cc": 
      result = 'b'
			#print("gullible")
    if their_history[0:2] == "bb":
      result = 'b'
			#print("mean")
    if their_history[0:3] == "cbc":
      result = 'c'
    if their_history[0:4] == "cbcc":
      result = 'c'
			#print("copycat")
    if their_history[0:4] == "cbbb":
      result = 'b'
			#print("90%")
    if their_history[0:5] == "cbcbc":
      result = 'c'
			#print("retaliate or alternate")			
    if their_history[0:6] == "cbcbcb":
      result = 'b'
			#print("alternate")
    if their_history[0:6] == "cbcbcb":
      result = 'c'
			#print("retaliate")			
    if their_history[0:11] == "cbbbbbbbbbb":
      result = 'b'
			#print("90%")

    if result == "test value": #catchall if opp strat is not recognized
      result = their_history[-1]
      print("didn't find")

    if len(my_history)%69 == 0:
      possibilities = ['c','b']
      index = random.randint(0,1)
      result = possibilities[index]

    if len(my_history) >= 150:
      possibilities = ['c','b']
      index = random.randint(0,1)
      result = possibilities[index]


    #This example player always never betrays.      
    return result
