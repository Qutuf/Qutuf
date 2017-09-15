
'''
Created on ٢١‏/٠٦‏/٢٠١٠

@Created by: Muhammad Altabba
'''

class TransitionActions(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qzIIYI35Ed-gg8GOK1TmhA
    """
    '''
    Contains a List of Transition Action
    '''
    Actions = [];

    OnInnerIndexes = [];
    
    
    def __init__(self, actions, onInnerIndexes):
        '''
        Constructor
        '''
        self.Actions = actions;
        self.OnInnerIndexes = onInnerIndexes;
    pass

    def ApplyToWord(self, sentence, wordIndex):
#        print('-- apply TransitionActions... '+str(self.Actions));
        if (self.OnInnerIndexes == []):
            for k in range(len(self.Actions)):
#                print('len(self.Actions)' + str(len(self.Actions)));
                self.Actions[k].ApplyToWord(sentence, wordIndex);
        else:
            for k in range(len(self.Actions)):
                self.Actions[k].ApplyToWordSurfaceFormMorphemes(sentence, wordIndex, self.OnInnerIndexes);
            
    pass
