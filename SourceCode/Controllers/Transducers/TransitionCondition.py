
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
#    Key = '';
    Value = '';
    

    def __init__(self, type, attributeName, value):
        '''
        Constructor
        '''
        self.Type = type;
        self.AttributeName = attributeName;
#        self.Key = key;
        self.Value = value;
        pass
        
    
    def TestMatch(self, word, actions, charIndexes = None):  
#        print('-- TestMatch...');
        
        if charIndexes == [None]:
#            if self.Type != 'general':
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
                import Models;
                
                isSatisfiedForOne = False;
                conditionFaildForlist = [];
                for i in actions.OnInnerIndexes:
                    try:
                        if (eval('Models.Tagging.POSTags.' + self.Value) & \
                        eval('word.SurfaceFormMorphemes[i].Cliticless.POS.' + self.AttributeName) != 0):
                            isSatisfiedForOne = True;
                        else:
                            conditionFaildForlist.append(i);
                    except:
                        x=0;
#                        print('Evaluation failed! for condition value: ['+self.Value\
#                              +'] and attribute name: ['+self.AttributeName+']');
                
                for i in conditionFaildForlist:
                    actions.OnInnerIndexes.remove(i);
                return isSatisfiedForOne;
                
                
        else:
            if self.Type == 'str':
#                print('word.__getattribute__(self.AttributeName) = '+str(word.__getattribute__(self.AttributeName)));
#                print('word.__getattribute__(String) = '+str(word.__getattribute__('String')));
#                print('charIndexes = '+str(charIndexes));
#                print("self.Value == ''.join([word.__getattribute__(self.AttributeName)[x] for x in charIndexes] = " +\
#                      self.Value + '==' + ''.join([word.__getattribute__(self.AttributeName)[x] for x in charIndexes]));
                try:
                
                    if self.Value == ''.join([word.__getattribute__(self.AttributeName)[x] for x in charIndexes]):
    #                if self.Value == word.__getattribute__(self.AttributeName)[charIndex]:
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
    
