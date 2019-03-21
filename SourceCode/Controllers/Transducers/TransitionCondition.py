
'''
Created on 19‏/03‏/2010

@Created by: Muhammad Altabba
'''

import re;

class TransitionCondition(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_qzIId435Ed-gg8GOK1TmhA
    """
    '''
    State Condition Class
    '''
    Type = '';
    AttributeName = '';
    Value = '';
    

    def __init__(self, type, attributeName, value):
        '''
        Constructor
        '''
        self.Type = type;
        self.AttributeName = attributeName;
        self.Value = value;
        pass
        
    
    def TestMatch(self, word, actions, charIndexes = None): 
        
        if charIndexes == [None]:
#            if self.Typej != 'general':
#                try:
#                    word.__getattribute__(self.AttributeName);
#                except:
#                    raise Exception('The Word does not have attribute: "'+self.Type+'"!'); 
            if self.Type == 'str':
                if re.search(self.Value, word.__getattribute__(self.AttributeName), re.UNICODE) != None:
                    return True;
            elif self.Type == 'dict':
                if self.Key in word.__getattribute__(self.AttributeName).keys():
                    if re.search(self.Value, str(word.__getattribute__(self.AttributeName)[self.Key]), re.UNICODE) != None:
                        return True;

            
            elif self.Type == 'set':
            #Test Needed ------------------------------------------------------------------------------------------------------
                if re.search(self.Value, str(word.__getattribute__(self.AttributeName)[int(self.Key)]), re.UNICODE) != None:
                    return True;
            elif self.Type == 'general':
            #Test Needed ------------------------------------------------------------------------------------------------------
                if re.search(self.Value, str(eval(self.AttributeName)), re.UNICODE) != None:
                    return True;
            elif self.Type == 'pos.rules':
			
                exec('from ...Models.Tagging.POSTags import *;');

                isSatisfiedForOne = False;
                conditionFaildForlist = [];
                for i in actions.OnInnerIndexes:
                    try:
                        if (eval(self.Value) & \
                        eval('word.SurfaceFormMorphemes[i].Cliticless.POS.' + self.AttributeName) != 0):
                            isSatisfiedForOne = True;
                        else:
                            conditionFaildForlist.append(i);
                    except AttributeError:
                       pass;
                
                for i in conditionFaildForlist:
                    actions.OnInnerIndexes.remove(i);
                return isSatisfiedForOne;
                
                
        else:
            if self.Type == 'str':
                try:                
                    if self.Value == ''.join([word.__getattribute__(self.AttributeName)[x] for x in charIndexes]):
                        return True;
                except:
                    print('word.String = ' + word.String);
                    print('word.__getattribute__(self.AttributeName) = '+str(word.__getattribute__(self.AttributeName)));
                    print('word.__getattribute__(String) = '+str(word.__getattribute__('String')));
                    print('charIndexes = '+str(charIndexes));
                    raise Exception('Error at TransducerCondition.TestMatch');
            else:
                print('Not implemented!');
        
        return False;
        pass
    
