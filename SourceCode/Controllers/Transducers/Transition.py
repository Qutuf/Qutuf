
'''
Created on ٠٢‏/٠٤‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Transducers.State import State

class Transition(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qzIIGo35Ed-gg8GOK1TmhA
    """
    '''
    Store one Transition from state to state. It contains Conditions and Actions.
    '''
    
    Conditions = [];
    
    Actions = [];
    
    NextState = State();
    
    Consume = 0;

    def __init__(self, conditions, actions, nextState, consume):
        '''
        Constructor
        '''
        self.Conditions = conditions;
        self.Actions = actions;
        self.NextState = nextState;
        self.Consume = consume;
