team_name = 'support_dawood'
strategy_name = 'support dawood'
strategy_description = 'betray everyone but dawood'
    
def move(my_history, their_history, my_score, their_score):

    '''betray everyone besides dawood.

    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''


    import example0, example1, example2, example3

    import example4, example5

    import bressler
    import Fitzgerald
    import graham
    import Lowell
    import mcmullen
    import miner
    import stacks
    import whitney
    import wisley
    import dawood
  
    modules = [example0, example1, example2, example3, example4, example5,          bressler, Fitzgerald, graham, Lowell, mcmullen, miner, whitney, wisley, stacks]
  
    support = [dawood]
  
    if len(my_history)<=1:
      for mod in modules:
        return 'b'

      for fan in support:
        return 'c'

