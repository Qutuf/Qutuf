
'''
Created on ١٩‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from .State import State
from .TransitionCondition import TransitionCondition

class StatesGraph(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qzIIAo35Ed-gg8GOK1TmhA
    """
    '''
    Store Graph of States of on-memory Tagging rules 
    '''
    
    States = dict(); 
    
    Start = None;
    
    ActionsToApply = dict();
    #Dictionary maps between each end and the desired action.
    #Keys are RELATIVE_WORD_INDEX and values are list of ACTIONS.
    
    
    def __init__(self, start = None, states = None):
        '''
        Constructor
        '''
        if states == None:
            self.States = dict();  
        self.Start = start;        
        self.ActionsToApply = dict();
    pass
    
    def Match(self, currentState, sentence, wordNumber, charIndex = None, charIndexForward = True):
#        print('-- Match...');
        [nextState, actions, numberToConsume] = currentState.NextStateWithActions(sentence.Words[wordNumber], charIndex, charIndexForward);
#        print('-- [nextState, actions, numberToConsume] = '+str([nextState, actions, numberToConsume]));
        if nextState != None:
            if wordNumber not in self.ActionsToApply.keys():
                self.ActionsToApply[wordNumber] = actions;
            else:
                self.ActionsToApply[wordNumber].Actions.append(actions);

            return [nextState, numberToConsume];
        
        return [None, None];
        
    pass
    
