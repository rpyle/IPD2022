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


    import mucher
    import Kauffman

    import pacheco
    import bressler
    import dawood


    import Fitzgerald
    import graham
    import Lowell
    import maggin
    import mcmullen
    import miner
    import schoonover
    import stacks
    import whitney
    import wisley
    import moyer
    import moyertrolling1
    import moyertrolling2
    import moyertrolling3
    import Logan
    import farace
    import phipps
    import tanner
    import ford

    import deesen
    import rrogers
  
    modules = [bressler, Fitzgerald, graham, Lowell, maggin, miner, schoonover, whitney, wisley, mucher, Kauffman, moyer, moyertrolling1, moyertrolling2, moyertrolling3, Logan, farace, phipps, tanner, ford, mcmullen, graham, deesen, rrogers, stacks, pacheco]

      
    support = [dawood]
  
    if len(my_history)<=1:
      for mod in modules:
        return 'b'


      for fan in support:
        return 'c'
