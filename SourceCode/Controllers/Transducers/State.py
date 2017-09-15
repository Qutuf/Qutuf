
'''
Created on ١٩‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''
from Transducers.TransitionActions import TransitionActions

class State(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qzIH5I35Ed-gg8GOK1TmhA
    """
    '''
    State of Graph
    '''
    Id = None;
#    
#    NextStates = dict();
#    #Mapping between Sates  and Conditions .
#    #Move to a desired state on some conditions.
#    #NextStates[NEXT_STATE] = [[CONDITIONS_LIST_1, ACTIONS_LIST_1], [CONDITIONS_LIST_2, ACTIONS_LIST_2],...]
#    #Note: all CONDITIONS_LIST_1 must be satisfied to do ACTIONS_LIST_1. Or all CONDITIONS_LIST_2 must be satisfied to do ACTIONS_LIST_2.

    Transitions = [];

    IsStart = False;

    IsEnd = False;

    def __init__(self, id = None, transitions = None):
        '''
        Constructor
        '''
        self.Id = id;
        if transitions == None:
            self.Transitions = [];
        self.IsStart = False;    
        self.IsEnd = False;
    
    def NextStateWithActions(self, word, charIndex = None, charIndexForward = True):
        '''
        [charIndexForward] is used to specify the look ahead direction is it forward or backward.
        '''
        
#        print('-- NextStateWithActions...');
        for l in range(len(self.Transitions)):
            conditions = self.Transitions[l].Conditions;
            transitionActions = TransitionActions([], []); 
            transitionActions.Actions = [action for action in self.Transitions[l].Actions.Actions];
            transitionActions.OnInnerIndexes = [i for i in range(len(word.SurfaceFormMorphemes))];
            nextState = self.Transitions[l].NextState;
            numberToConsume = self.Transitions[l].Consume;
            
            conditionSatisfied = True;
#            print('-- Transitions loop...');
            for j in range(len(conditions)):
                if(charIndex == None):
#                    print('-- charIndex == None');
                    result = conditions[j].TestMatch(word, transitionActions, [charIndex]);
                else:
#                    print('-- charIndex != None');
                    if(charIndexForward == True):
#                        print('-- charIndexForward == True');
                        if(charIndex < 0 or charIndex+numberToConsume >= len(word.String)):
                            conditionSatisfied = False;
                            break;
#                        print('-- TestMatch');
                        result = conditions[j].TestMatch(word, transitionActions, range(charIndex, charIndex+numberToConsume));
                    elif(charIndexForward == False):
#                        print('-- charIndexForward == False');
#                        print('-- charIndex = '+str(charIndex));
#                        print('-- numberToConsume = '+str(numberToConsume));
#                        print('-- len(word.String) = '+str(len(word.String)));
                        if(charIndex-numberToConsume+1 < 0 or charIndex+1 > len(word.String)):
                            conditionSatisfied = False;
                            break;
                        
#                        print('-- TestMatch');
                        result = conditions[j].TestMatch(word, transitionActions, range(charIndex-numberToConsume+1, charIndex+1));
                    else:
                        raise Exception('Unexpected value ['+charIndexForward+'] for variable: charIndexForward');
                if result != True:
                    conditionSatisfied = False;
                    break;

                        
                            
            if conditionSatisfied == True:
                return [nextState, transitionActions, numberToConsume];
        return [None, None, None];
        pass
