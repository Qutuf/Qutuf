
'''
Created on ٢٣‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''
import re;

class TransitionAction(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qzIINI35Ed-gg8GOK1TmhA
    """
    '''
    State Action
    '''
    Type = '';
    AttributeName = '';
    Value = '';
    OnRelativeIndex = 0;

    def __init__(self, attributeName, type, value, onRelativeIndex):
        '''
        Constructor
        '''
        self.AttributeName = attributeName;
        self.Type = type;
        self.Value = value;
        self.OnRelativeIndex = onRelativeIndex;
    pass
    
    def ApplyToWord(self, sentence, wordIndex):
#        print('-- apply...');
        word = sentence.Words[wordIndex + self.OnRelativeIndex];
        if self.Type == 'str':
            setattr(word, self.AttributeName, self.Value);
        elif self.Type == 'set.append':
#            print('-- apply:')
            eval('word.'+self.AttributeName).append(eval(self.Value));
#            word.__getattribute__(self.AttributeName).append(eval(self.Value));
                
        elif self.Type == 'dict':
#        #Test Needed -------------------------------------------------------------
            #value has the shape: {key1: value1, key2: value2}
            dictionary = eval(self.Value);
            for key, value in dictionary.items():
                word.__getattribute__(self.AttributeName)[key] = value;   
                    
        elif self.Type == 'general':
                setattr(word, self.AttributeName, eval(self.Value));    
#        #Test Needed -------------------------------------------------------------

    pass
    
    def ApplyToWordSurfaceFormMorphemes(self, sentence, wordIndex, surfaceFormMorphemesIndexes):
#        print('-- apply ApplyToWordSurfaceFormMorphemes...');
        word = sentence.Words[wordIndex + self.OnRelativeIndex];
        if self.Type == 'method':
            for i in range(len(surfaceFormMorphemesIndexes)):                
                eval('word.SurfaceFormMorphemes[surfaceFormMorphemesIndexes[i]].'+self.AttributeName+'('+self.Value+')'); 
    pass
